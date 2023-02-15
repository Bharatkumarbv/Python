import sys
sys.path.append("D:\python")

import unittest
import swapping

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(swapping.swap("ha","mm"),('mm', 'ha'))
    def testcase2(self):
        self.assertEqual(swapping.swap("welcome","bye"),("bye","welcome"))


if __name__=="__main__":
    unittest.main()
