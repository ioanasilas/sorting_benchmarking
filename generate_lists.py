import random

'''
List Generation for Sorting Algorithm Benchmarks
------------------------------------------------
This module contains functions designed to generate lists with specific properties for benchmarking sorting algorithms. 
Each function returns a list constructed according to the following criteria:

generate_random_list(size): Returns a list of 'size' random integers ranging from 0 to 10 million.
generate_ordered_list(size): Returns a list of integers from 0 to 'size-1', sorted in ascending order.
generate_reverse_list(size): Returns a list of integers from 'size-1' to 0, sorted in descending order.
generate_duplicates_list(size): Returns a list where the number of unique elements is at least 5 or 'size / 1000', with duplicates randomly scattered.
generate_nearly_sorted_list(size): Returns a nearly sorted list with 1% of its elements (minimum 1) randomly swapped.
generate_sortedlist_one_swap(size): Returns a sorted list with exactly one random swap of elements.
'''


def generate_random_list(size):
    return [random.randint(0, 10000000) for _ in range(size)]

def generate_ordered_list(size):
    return list(range(size))

def generate_reverse_list(size):
    return list(range(size, 0, -1))

def generate_duplicates_list(size):
    num_unique = max(5, size // 1000)  # so number of unique elements grows with list size
    unique_elements = [random.randint(0, 10000000) for _ in range(num_unique)]
    return [random.choice(unique_elements) for _ in range(size)]

def generate_nearly_sorted_list(size):
    lst = list(range(size))
    num_swaps = max(1, int(0.01 * size))  # 1% of the size
    for _ in range(num_swaps):
        index1 = random.randint(0, size - 1)
        index2 = random.randint(0, size - 1)
        while index2 == index1:
            index2 = random.randint(0, size - 1)
        lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

def generate_sortedlist_one_swap(size):
    lst = list(range(size))
    index1 = random.randint(0, size - 1)
    index2 = random.randint(0, size - 1)
    while index2 == index1:
        index2 = random.randint(0, size - 1)
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst