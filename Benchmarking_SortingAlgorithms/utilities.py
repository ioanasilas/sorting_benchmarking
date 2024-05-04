from sorting_algorithms import *
from generate_lists import *
import signal

"""
Functions:
    quick_sort_wrapper(array) & heap_sort_wrapper(array): wrappers for sorting algorithms to simplify their usage by abstracting away unnecessary parameters during routine calls.
    format_algorithm_name(name): converts raw algorithm function names into a human-readable format for improved clarity in logs.
    format_list_name(func_name): maps function names generating lists to descriptive labels for clearer output.
    timeout_handler(signum, frame): handles timeout signals by raising a `TimeoutError`. It's useful in scenarios with very large datasets or less efficient algorithms.
"""


def quick_sort_wrapper(array):
    quick_sort(array, 0, len(array) - 1)

def heap_sort_wrapper(array):
    heap_sort(array, 0, len(array) - 1)

def format_algorithm_name(name):
    """ Format the algorithm's name for output readability. """
    if name == "timsort":
        return "Timsort"
    elif name.endswith("_wrapper"):
        return name[:-8].replace('_', ' ').title()
    else:
        return name.replace('_', ' ').title()

def format_list_name(func_name):
    """Format the list generator function's name for clearer and more descriptive output."""
    mappings = {
        "generate_random_list": "Random Data",
        "generate_ordered_list": "Ordered Data",
        "generate_reverse_list": "Reverse Ordered Data",
        "generate_duplicates_list": "Duplicates Data",
        "generate_nearly_sorted_list": "Nearly Sorted Data"
    }
    return mappings.get(func_name, "Unknown List Type")

def timeout_handler(signum, frame):
    """ Handle the signal sent from a timeout event. """
    raise TimeoutError
