import unittest
from random import shuffle
from random import random
from PriorityQueue import PriorityQueue

class PriorityQueueTest(unittest.TestCase):
    def setUp(self):
        self.p_queue = PriorityQueue()

    def test(self):
        elements = []
        for i in range(1000):
            x = random()
            elements.append(x)
            self.p_queue.insert(x)
        elements.sort(reverse=True)
        for elem in elements:
            self.assertEqual(elem, self.p_queue.pop())


if __name__ == '__main__':
    unittest.main()
