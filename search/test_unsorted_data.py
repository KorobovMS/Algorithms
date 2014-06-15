import unittest
from linear_search import linear_search

class UnsortedDataSearchTest(unittest.TestCase):
    def setUp(self):
        self.search_functions = [linear_search]

    def assert_found_for_all_functions(self, case):
        for search in self.search_functions:
            self.assertEqual(search(case[0], case[1]), case[2])

    def assert_raises_for_all_functions(self, case):
        for search in self.search_functions:
            self.assertRaises(ValueError, search, case[0], case[1])

    def test_found(self):
        cases = [
            ([1], 1, 0),
            (list(range(100)), 33, 33),
            ([5, 1, 2, 7, 4], 7, 3)
        ]
        for case in cases:
            self.assert_found_for_all_functions(case)

    def test_not_found(self):
        cases = [
            ([], 1),
            ([1], 2),
            (list(range(100)), 123),
            ([3, 1, 2, 1, 8, 5], 9)
        ]
        for case in cases:
            self.assert_raises_for_all_functions(case)

if __name__ == '__main__':
    unittest.main()