from maximum_subarray import maximum_subarray
import unittest

class MaximumSubarrayTestCase(unittest.TestCase):
    def setUp(self):
        self.tests = [
            ([1], (0, 1)),
            ([1, 2, 3], (0, 3)),
            ([4, -5, 6, -17], (2, 3)),
            ([-3, -25, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4], (5, 9))
        ]

    def test_arrays(self):
        for data, result in self.tests:
            print(maximum_subarray(data))
            self.assertEqual(maximum_subarray(data)[0:2], result)

if __name__ == '__main__':
    unittest.main()
