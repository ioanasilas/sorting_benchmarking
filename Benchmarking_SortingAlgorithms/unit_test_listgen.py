import unittest
from unittest.mock import patch
from generate_lists import *

"""
Unit Tests for List Generation Functions
------------------------------------------------
Purpose:
These unit tests validate the functionality of the list generation functions, ensuring they produce lists of correct sizes and types.
"""

class TestListGeneration(unittest.TestCase):

    def test_small_medium_large_lists(self):
        # test sizes to represent small, medium, and large
        test_sizes = {10: 100, 1000: 10, 1000000: 2}

        for size, expected_count in test_sizes.items():

        # test for random lists    
            with patch('generate_lists.random.randint', return_value=1) as mock_randint:
                lists = [generate_random_list(size) for _ in range(expected_count)]
                self.assertEqual(mock_randint.call_count, size * expected_count)
                for lst in lists:
                    self.assertEqual(len(lst), size)

        # test for ordered lists
            lists = [generate_ordered_list(size) for _ in range(expected_count)]
            for lst in lists:
                self.assertTrue(all(lst[i] <= lst[i+1] for i in range(len(lst) - 1)))

        # test for reversed lists
            lists = [generate_reverse_list(size) for _ in range(expected_count)]
            for lst in lists:
                self.assertTrue(all(lst[i] >= lst[i+1] for i in range(len(lst) - 1)))
        
        # test for duplicated lists
            with patch('generate_lists.random.choice', return_value=1):
                lists = [generate_duplicates_list(size) for _ in range(expected_count)]
                for lst in lists:
                    self.assertEqual(len(lst), size)

        # test for nearly sorted lists
            lists = [generate_nearly_sorted_list(size) for _ in range(expected_count)]
            num_swaps = max(1, int(0.01 * size))
            for lst in lists:
                self.assertEqual(len(lst), size)
                sorted_lst = sorted(lst)
                diff_count = sum(1 for i, j in zip(lst, sorted_lst) if i != j)

                # account for potential overlap in swapping effects
                self.assertTrue(abs(diff_count - 2 * num_swaps) <= 300) 
            
        # test for nearly sorted lists with one swap    
            lists = [generate_sortedlist_one_swap(size) for _ in range (expected_count)]
            for lst in lists:
                self.assertEqual(len(lst), size)
                sorted_lst = sorted(lst)
                diff_count = sum(1 for i, j in zip(lst, sorted_lst) if i != j)
                self.assertEqual(diff_count, 2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
