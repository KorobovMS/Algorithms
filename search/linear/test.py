import unittest
from linear_search import linear_search

class LinearSearchTest(unittest.TestCase):
    def setUp(self):
        self.search_functions = [linear_search]
    
    def make_test(self, seq, elem, pos):
        for search in self.search_functions:
            self.assertEqual(search(seq, elem), pos)
    
    def test_empty_sequence(self):
        seq = []
        self.make_test(seq, 1, len(seq))
        
    def test_one_element_sequence_found(self):
        seq = [1]
        self.make_test(seq, 1, 0)

    def test_one_element_sequence_not_found(self):
        seq = [1]
        self.make_test(seq, 2, len(seq))
        
    def test_on_range_found(self):
        seq = list(range(100))
        self.make_test(seq, 33, 33)
        
    def test_on_range_not_found(self):
        seq = list(range(100))
        self.make_test(seq, 123, len(seq))
        
    def test_on_array_found(self):
        seq = [5, 1, 2, 7, 4]
        self.make_test(seq, 7, 3)
        
    def test_on_array_not_found(self):
        seq = [3, 1, 2, 1, 8, 5]
        self.make_test(seq, 9, len(seq))

if __name__ == '__main__':
    unittest.main()