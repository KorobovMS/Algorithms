import unittest
from HashTable import HashTable

class HashTableTest(unittest.TestCase):
    def setUp(self):
        self.ht = HashTable()

    def test_basic(self):
        self.ht.insert('entry1', 'value1')
        self.ht.insert('entry2', 'value2')

        self.assertEqual(self.ht.search('entry1'), 'value1')
        self.assertEqual(self.ht.search('entry2'), 'value2')
        self.assertEqual(self.ht.search('entry3'), None)

        self.ht.delete('entry1')
        self.ht.delete('entry2')

        self.assertEqual(self.ht.search('entry1'), None)

    def test_ins_del(self):
        count = 10000

        for i in range(count):
            self.ht.insert(i, i)
            self.assertEqual(self.ht.search(i), i)

        for i in range(count):
            self.ht.delete(i)
            self.assertEqual(self.ht.search(i), None)

if __name__ == '__main__':
    unittest.main()

