import sys
sys.path.append("D:\python")

import unittest
import swap_first_and_last

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(swap_first_and_last.lst([1,2,3,4,5,6,7]),[7,2,3,4,5,6,1])
    def testcase2(self):
        self.assertEqual(swap_first_and_last.lst([11,12,31,22]),[22,12,31,11])


if __name__=="__main__":
    unittest.main()
