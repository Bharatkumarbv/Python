import sys
sys.path.append("D:\python")

import unittest
import armstrong_number

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(armstrong_number.arm(153),True)
    def testcase2(self):
        self.assertEqual(armstrong_number.arm(10),False)


if __name__=="__main__":
    unittest.main()
