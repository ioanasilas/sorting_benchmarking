import csv
import timeit
import os
import signal
from generate_lists import generate_nearly_sorted_list
from sorting_algorithms import *
from utilities import *
import sys
sys.setrecursionlimit(10**9)

# dictionary mapping list sizes to the number of times each should be run for benchmarking
list_sizes = {10: 10000, 100: 1000, 1000: 1000, 10000: 100, 100000: 10, 500000: 5, 1000000: 5, 10000000: 3}
list_type = generate_nearly_sorted_list  # function to generate nearly_ordered lists for sorting.
sorting_timeout = {bubble_sort: 0, insertion_sort: 0, selection_sort: 0, merge_sort: 0, quick_sort_wrapper: 0, timsort: 0, heap_sort_wrapper: 0}

# file paths for output csv files
output_directory = "./csv_outputs"
os.makedirs(output_directory, exist_ok=True)
detailed_csv_path = os.path.join(output_directory, "detailed_nearly_ordered_runs_round2.csv")
summary_csv_path = os.path.join(output_directory, "summary_nearly_ordered_runs_round2.csv")

def time_sorting_algorithm(function, data, timeout):
    """Measure execution time of a sorting function with timeout handling.
    
    Args:
        function: The sorting function to be benchmarked.
        data: The list of data to sort.
        timeout: The timeout limit in seconds after which the function should be terminated.

    Returns:
        The execution time in seconds or None if the execution timed out.
    """
    try:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout)
        start_time = timeit.default_timer()
        function(data)
        end_time = timeit.default_timer()
        signal.alarm(0)
        return end_time - start_time
    except TimeoutError:
        return None

def perform_benchmark(function, generator, size, runs, writer, results, timeout=300):
    """Benchmark a sorting function over several runs and record performance."""
    list_type_name = format_list_name(generator.__name__)
    algo_name = format_algorithm_name(function.__name__)
    print(f"Benchmarking {algo_name} for {size} elements ({list_type_name}).")
    execution_times = []

    for _ in range(runs):
        data = generator(size)
        if sorting_timeout[function] == 1:
            execution_time = None
        else:
            execution_time = time_sorting_algorithm(function, data, timeout)
        if execution_time is None:
            sorting_timeout[function] = 1
            print(f"Timeout: {function.__name__} at size {size}")
            results[size][algo_name] = "> 300 seconds"
            # set timeout for larger sizes as well
            for larger_size in [s for s in list_sizes if s > size]:
                results[larger_size][algo_name] = "> 300 seconds"
            break
        execution_times.append(execution_time)
        writer.writerow([list_type_name, size, algo_name, f"{execution_time:.8f}"])
        
        if execution_times:
            average_time = f"{sum(execution_times) / len(execution_times):.8f}"
            results[size][algo_name] = average_time

def prepare_csv_files():
    """Setup CSV files for recording detailed and summary benchmark results.
    
    Returns:
        A tuple containing file objects and CSV writer objects for detailed and summary results.
    """
    detailed_file = open(detailed_csv_path, "w", newline='')
    summary_file = open(summary_csv_path, "w", newline='')

    detailed_writer = csv.writer(detailed_file)
    detailed_writer.writerow(['List Type', 'List Size', 'Algorithm', 'Run Time'])

    summary_writer = csv.writer(summary_file)
    summary_writer.writerow(['List Type', 'List Size'] + [format_algorithm_name(func.__name__) for func in sorting_timeout])

    return detailed_file, summary_file, detailed_writer, summary_writer

def main():
    detailed_file, summary_file, detailed_writer, summary_writer = prepare_csv_files()

    # data structure to hold the results
    results = {size: {format_algorithm_name(func.__name__): None for func in sorting_timeout} for size in list_sizes}
    for size in list_sizes:
        for algorithm in sorting_timeout:
            perform_benchmark(algorithm, list_type, size, list_sizes[size], detailed_writer, results, timeout=300)

    # writing results to summary CSV
    for size, algorithms in results.items():
        row = [format_list_name(list_type.__name__), size] + [algorithms.get(format_algorithm_name(algorithm.__name__), "No data") for algorithm in sorting_timeout]
        summary_writer.writerow(row)

    detailed_file.close()
    summary_file.close()

if __name__ == '__main__':
    main()

