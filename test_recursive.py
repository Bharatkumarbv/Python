import sys
sys.path.append("D:\python")

import unittest
import rcursive

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(rcursive.rec(0,10),55)
    def testcase1(self):
        self.assertEqual(rcursive.rec(0,5),15)


if __name__=="__main__":
    unittest.main()
