import sys
sys.path.append("D:\python")

import unittest
import anagram

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(anagram.string("listen", "nestil"),"It is an anagram")
    def testcase2(self):
        self.assertEqual(anagram.string("lisen", "newstl"),"It is not an anagram")


if __name__=="__main__":
    unittest.main()
