import unittest
from itertools import permutations

from randomized_select import randomized_select
from select_by_sorting import select_by_sorting
from select_with_medians import select_with_medians

class OrderStatisticsTest(unittest.TestCase):
    def setUp(self):
        self.functions = [
            select_by_sorting,
            randomized_select,
            select_with_medians]

    def test_found(self):
        length = 8
        array = list(range(1, length + 1))
        all_permutations = permutations(array)
        for permutation in all_permutations:
            seq = list(permutation)
            for k in range(1, length + 1):
                for select in self.functions:
                    self.assertEqual(select(seq, k), k)

    @unittest.skip('Consider order statistic exists')
    def test_not_found(self):
        arr = [1, 2, 3, 4, 5]
        cases = [(arr, 0), (arr, 10), ([], 1)]
        for case in cases:
            for select in self.functions:
                self.assertRaises(ValueError, select, case[0], case[1])

if __name__ == '__main__':
    unittest.main()
