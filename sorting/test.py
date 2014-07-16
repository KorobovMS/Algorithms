from heapsort import heapsort
from mergesort import mergesort
from insertion_sort import insertion_sort
from bubble_sort import bubble_sort
from quicksort import quicksort
from quicksort import tail_recursion_quicksort

from counting_sort import counting_sort

import unittest
import random

class SortingTest(unittest.TestCase):
    def setUp(self):
        self.sort_functions = [
            heapsort,
            mergesort,
            insertion_sort,
            bubble_sort,
            quicksort,
            tail_recursion_quicksort]

    def test_empty(self):
        for sort_func in self.sort_functions:
            A = []
            sort_func(A)
            self.assertEqual([], A)

    def test_comparison_sorts(self):
        sizes = [100 for x in range(10)]
        for sort_func in self.sort_functions:
            for size in sizes:
                source = [random.random() for i in range(size)]
                excpected = sorted(source)
                actual = source[:]
                sort_func(actual)
                self.assertEqual(excpected, actual)

    def test_counting_sort(self):
        from itertools import permutations
        k = 4
        sorted_array = list(range(k + 1))
        for permutation in permutations(sorted_array):
            array = list(permutation)
            counting_sort(array, k)
            self.assertEqual(sorted_array, array)


if __name__ == '__main__':
    unittest.main()
