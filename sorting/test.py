from heapsort import heapsort
from mergesort import mergesort
from insertion_sort import insertion_sort
import unittest
import random

class SortingTest(unittest.TestCase):
    def setUp(self):
        self.sort_functions = [heapsort, mergesort, insertion_sort]

    def test_empty(self):
        for sort_func in self.sort_functions:
            A = []
            sort_func(A)
            self.assertEqual([], A)

    def test_random(self):
        sizes = [10 for x in range(10)]
        for sort_func in self.sort_functions:
            for size in sizes:
                source = [random.random() for i in range(size)]
                excpected = sorted(source)
                actual = source[:]
                sort_func(actual)
                self.assertEqual(excpected, actual)

if __name__ == '__main__':
    unittest.main()
