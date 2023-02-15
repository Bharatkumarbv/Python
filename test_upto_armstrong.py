import sys
sys.path.append("D:\python")

import unittest
import upto_given_range_Armstrong_numbers

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(upto_given_range_Armstrong_numbers.arm(1000),[1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
    def testcase2(self):
        self.assertEqual(upto_given_range_Armstrong_numbers.arm(200),[1, 2, 3, 4, 5, 6, 7, 8, 9, 153])


if __name__=="__main__":
    unittest.main()
