import sys
sys.path.append("D:\python")

import unittest
import string_slicing

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(string_slicing.string("bharath",3),"rath")
    def testcase2(self):
        self.assertEqual(string_slicing.string("bharath",8),"this index value not exist")


if __name__=="__main__":
    unittest.main()
