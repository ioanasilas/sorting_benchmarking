# Sorting benchmarking
This project focuses on benchmarking the following sorting algorithms: Bubble Sort, Insertion Sort, Selection Sort, Merge Sort, Quick Sort, Timsort, Heap Sort. The benchmarking process is focused solely on the execution time of the algorithms on various data sets.
## What each file contains
This is a summary of the contents of each file / directory. Additional details may be found inside the actual files.

`generate_lists.py`: contains functions designed to generate lists with specific properties for benchmarking sorting algorithm.

`sorting_algorithms.py`: contains the implementation of the sorting algorithms that were benchmarked.

`unit_test_listgen.py` and `unit_testing_algorithms.py`: contain the unit tests that validate the correctness of the list generator functions and the correctness of the implementation of the sorting algorithms respectively.

`benchmarking_scripts`: this directory contains the actual code for benchmarking the algorithms on the varying list sizes and types. The benchmarking scripts are organized by list types (random, ordered, reversed, partial, duplicated).

`paper_csv_results`: this directory contains the results of the benchmarking that were done on the various data sets. The detailed csv files includes results for every individual run, and the summary csv files contain the overrall average execution time in seconds for every algorithm on every data set.

`utilities.py`: contains utilities that are used inside the benchmarking scripts.

`main.py` centralizes the benchmarking process.

## How the benchmarking is done
This is a simplified version of how the benchmarking is done:
```python
execution_time = time_sorting_algorithm(bubble_sort, data, 300)
if execution_time:
    print(f"Execution time: {execution_time} seconds")
else:
    print("Benchmarking timed out.")
```
If a sorting operation exceeds the timeout limit (300 seconds in this example), the function captures this as a timeout event and handles it accordingly: as instant response, the execution time for this specific run is recorded as a timeout. Moreover, it's assumed that if a particular algorithm cannot sort a dataset of a certain size within 300 seconds, it is unlikely to handle larger datasets of that time efficiently. Therefore, the script marks all larger dataset sizes as timeouts for that algorithm and list type.

## How to run the benchmarking scripts
To ensure proper execution of the `main.py` script for this project, since the platform-specific feature SIGALRM is used in the benchmarking scripts, it is necessary to use a Unix-like environment.
For Windows users, this necessitates the use of the Windows Subsystem for Linux (WSL) to provide a compatible Unix environment. 

### Setting Up the Environment
Install WSL on Windows via PowerShell with administrative privileges:
```powershell
wsl --install
```
Follow the installation prompts to set up a preferred Linux distribution, such as Ubuntu.

### Configuring PYTHONPATH
The project directory must be added to the PYTHONPATH to allow Python to locate and import the necessary modules. This configuration can be set by:
```bash
export PYTHONPATH="/path/to/your/project:$PYTHONPATH"
```
`/path/to/your/project` should be adjusted to the actual project path. This command should be executed in the Unix terminal where main.py will be run. For a persistent setup, add this line to the shell's startup file (e.g., .bashrc or .bash_profile).

### Running `main.py`
After setting up the environment, main.py can be executed directly from the terminal. The script requires a command-line argument specifying the type of list data:
```bash
python3 main.py [type]
```
Here, [type] can be replaced with random, ordered, reversed, partial, or duplicated, depending on the desired benchmarking scenario.
After running `main.py`, a new directory will be created where the 2 csv files will be outputted. The summary_csv file is created after the script finishes, while the detailed_csv is created dynamically.

Just a heads up, be prepared for varying execution times:

Fastest Results: ~1 hour for already sorted lists.

Longer Wait Times: ~2 hours for random, reversed, partial, or duplicated lists.

This is because of a combination of a large number of runs on data sets with a considerable size and the high execution time of certain sorting algorithms. (e.g. Selection Sort on lists sorted in reverse😮‍💨)
