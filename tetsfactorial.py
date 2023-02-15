import sys
sys.path.append("D:\python")

import unittest
import factorial

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(factorial.fac(5),120)
    def testcase2(self):
        self.assertEqual(factorial.fac(4),24)


if __name__=="__main__":
    unittest.main()
