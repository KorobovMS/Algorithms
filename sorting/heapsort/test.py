from heapsort import heapsort
import unittest
import random
from time import clock

class HeapsortTest(unittest.TestCase):
    def SetUp(self):
        pass
    
    def test_empty(self):
        source = []
    
    def test_random(self):
        sizes = [10**i for i in range(6)]
        for size in sizes:
            print('----- Size: {:6d} -----'.format(size))
            source = [random.random() for i in range(size)]
            clk = clock()
            excpected = sorted(source)
            clk = clock() - clk
            print('Internal sort: {}'.format(clk))
            
            clk = clock()
            actual = source[:]
            heapsort(actual)
            clk = clock() - clk
            print('Heapsort: {}'.format(clk))
            
            self.assertEqual(excpected, actual)

if __name__ == '__main__':
    unittest.main()
    