import sys
sys.path.append("D:\python")

import unittest
import merge_and_sort

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(merge_and_sort.lst([1,2,3,7,9],[4,5,6,8]),[1,2,3,4,5,6,7,8,9])
    def testcase1(self):
        self.assertEqual(merge_and_sort.lst([1,3,5],[2,8,4]),[1,2,3,4,5,8])


if __name__=="__main__":
    unittest.main()
