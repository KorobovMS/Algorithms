from heapsort import heapsort
import unittest
import random

class HeapsortTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_empty(self):
        source = []

    def test_random(self):
        sizes = [10**i for i in range(5)]
        for size in sizes:
            source = [random.random() for i in range(size)]
            excpected = sorted(source)
            actual = source[:]
            heapsort(actual)
            self.assertEqual(excpected, actual)

if __name__ == '__main__':
    unittest.main()
