import sys
sys.path.append("D:\python")

import unittest
import swap_tuple

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(swap_tuple.tep((1,2,3),(9,8,7)),((9,8,7),(1,2,3)))
    def testcase2(self):
        self.assertEqual(swap_tuple.tep((1,2,3),(3,5,9)),((3,5,9),(1,2,3)))


if __name__=="__main__":
    unittest.main()
