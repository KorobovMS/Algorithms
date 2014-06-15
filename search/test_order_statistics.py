import unittest
from random import shuffle
from selection_algorithm import select_by_sorting

class OrderStatisticsTest(unittest.TestCase):
    def setUp(self):
        self.functions = [select_by_sorting]

    def test_found(self):
        arr = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 5]
        cases = [(arr, i, i) for i in range(1,6)]
        for case in cases:
            for select in self.functions:
                self.assertEqual(select(case[0], case[1]), case[2])

    def test_not_found(self):
        arr = [1, 2, 3, 4, 5]
        cases = [(arr, 0), (arr, 10), ([], 1)]
        for case in cases:
            for select in self.functions:
                self.assertRaises(ValueError, select, case[0], case[1])

if __name__ == '__main__':
    unittest.main()
