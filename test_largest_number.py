import sys
sys.path.append("D:\python")

import unittest
import largest_number_in_list

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(largest_number_in_list.lst([1,2,3,44,11,12,54,23]),54)
    def testcase1(self):
        self.assertEqual(largest_number_in_list.lst([1,2,3,4,7,11,3]),11)


if __name__=="__main__":
    unittest.main()
