import sys
sys.path.append("D:\python")

import unittest
import list_of_palindromes

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(list_of_palindromes.palin(["mom", "bhahb"]),['mom','bhahb'])
    def testcase1(self):
        self.assertEqual(list_of_palindromes.palin(["bhbhbh nnm kikk"]),"No palindromes")


if __name__=="__main__":
    unittest.main()
