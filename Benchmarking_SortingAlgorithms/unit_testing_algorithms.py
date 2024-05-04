from sorting_algorithms import *
import unittest
import random
import sys
sys.setrecursionlimit(10**9)

"""
Unit Tests for the Sorting Algorithms
------------------------------------------------
These tests validate the correctness of the sorting algorithms.
Each sorting algorithm must exactly produce the expected sorted order as verified against predefined results for each type of test array.
"""


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.test_arrays = [
            [],  # empty array
            [1],  # single element
            [2, 1],  # two elements reversed
            [1, 2, 3, 4, 5],  # already sorted
            [5, 4, 3, 2, 1],  # reverse order
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5],  # random order with duplicates
            [random.randint(0, 10000) for i in range(10000)],  # large random list
            [i for i in range(10000)],  # ordered list
            sorted([random.randint(0, 10000) for i in range(10000)], reverse=True),  # reverse sorted list
            [random.choice([5, 10, 15, 20, 25]) for i in range(10000)]  # list with many duplicates
        ]

        # nearly sorted list with random swaps
        nearly_sorted_list = [i for i in range(10000)]
        num_swaps = 66
        for _ in range(num_swaps):
            index1 = random.randint(0, 9999)
            index2 = random.randint(0, 9999)
            nearly_sorted_list[index1], nearly_sorted_list[index2] = nearly_sorted_list[index2], nearly_sorted_list[index1]
        self.test_arrays.append(nearly_sorted_list)

        self.expected_results = [
            [],
            [1],
            [1, 2],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9],
            sorted(self.test_arrays[6]),  # for the large random list
            sorted(self.test_arrays[7]),  # for the ordered list
            sorted(self.test_arrays[8]),  # for the reverse sorted list
            sorted(self.test_arrays[9]),  # for the list with many duplicates
            sorted(self.test_arrays[10])  # for the nearly sorted list
        ]

    def test_bubble_sort(self):
        for i, array in enumerate(self.test_arrays):
            with self.subTest(i=i):
                bubble_sort(array)
                self.assertEqual(array, self.expected_results[i])

    def test_insertion_sort(self):
        for i, array in enumerate(self.test_arrays):
            with self.subTest(i=i):
                insertion_sort(array)
                self.assertEqual(array, self.expected_results[i])

    def test_selection_sort(self):
        for i, array in enumerate(self.test_arrays):
            with self.subTest(i=i):
                selection_sort(array)
                self.assertEqual(array, self.expected_results[i])

    def test_merge_sort(self):
        for i, array in enumerate(self.test_arrays):
            with self.subTest(i=i):
                merge_sort(array)
                self.assertEqual(array, self.expected_results[i])

    def test_quick_sort(self):
        for i, array in enumerate(self.test_arrays):
            with self.subTest(i=i):
                quick_sort(array, 0, len(array)-1)
                self.assertEqual(array, self.expected_results[i])

    def test_timsort(self):
        for i, array in enumerate(self.test_arrays):
            with self.subTest(i=i):
                timsort(array)
                self.assertEqual(array, self.expected_results[i])

    def test_heap_sort(self):
        for i, array in enumerate(self.test_arrays):
            with self.subTest(i=i):
                heap_sort(array, 0, len(array)-1)
                self.assertEqual(array, self.expected_results[i])

if __name__ == '__main__':
    unittest.main(verbosity=2)
