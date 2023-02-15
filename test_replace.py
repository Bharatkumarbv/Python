import sys
sys.path.append("D:\python")

import unittest
import replace_letter

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(replace_letter.rpl("bharath","a","v"),"bhvrvth")
    def testcase1(self):
        self.assertEqual(replace_letter.rpl("hello","l","a"),"heaao")


if __name__=="__main__":
    unittest.main()
