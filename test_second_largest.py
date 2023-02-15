import sys
sys.path.append("D:\python")

import unittest
import second_largest_list

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(second_largest_list.lst([1,2,3,5,2,7,9,21,11,22]),21)
    def testcase1(self):
        self.assertEqual(second_largest_list.lst([1,2,3,4,5,6,7]),6)


if __name__=="__main__":
    unittest.main()
