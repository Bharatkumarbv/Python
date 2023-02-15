import sys
sys.path.append("D:\python")

import unittest
import palindrome

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(palindrome.stt("heleh"),"It is Palindrome")
    def testcase1(self):
        self.assertEqual(palindrome.stt("cool"),"Not a Palindrome")


if __name__=="__main__":
    unittest.main()
