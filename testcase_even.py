import sys
sys.path.append("D:\python")

import unittest
import even_odd_check

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(even_odd_check.check(22),"even")
    def testcase(self):
        self.assertEqual(even_odd_check.check(21),"odd")


if __name__=="__main__":
    unittest.main()
