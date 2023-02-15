import sys
sys.path.append("D:\python")

import unittest
import odd_place_value

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(odd_place_value.string("bharathkumar"),"hrtkmr")
    def testcase1(self):
        self.assertEqual(odd_place_value.string("cool"),"ol")


if __name__=="__main__":
    unittest.main()
