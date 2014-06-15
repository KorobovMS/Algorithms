import unittest
from linear_search import linear_search
from binary_search import binary_search

class SortedDataSearchTest(unittest.TestCase):
    def setUp(self):
        self.search_functions = [linear_search, binary_search]

    def assert_found_for_all_functions(self, case):
        for search in self.search_functions:
            self.assertEqual(search(case[0], case[1]), case[2])

    def assert_raises_for_all_functions(self, case):
        for search in self.search_functions:
            self.assertRaises(ValueError, search, case[0], case[1])

    def test_found(self):
        cases = sum([[(list(range(s)), i, i) for i in range(s)]
            for s in range(1, 7)], [])
        for case in cases:
            self.assert_found_for_all_functions(case)

    def test_not_found(self):
        cases = [
            ([], 1),
            (list(range(10)), 200),
            (list(range(10)), -10),
            ([1, 2, 4, 5], 3),
            ([1, 3, 5], 2),
            ([1, 3, 5], 4)
        ]
        for case in cases:
            self.assert_raises_for_all_functions(case)

if __name__ == '__main__':
    unittest.main()
