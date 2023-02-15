import sys
sys.path.append("D:\python")

import unittest
import fibonacci_series_someValue

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(fibonacci_series_someValue.fibb(6),5)
    def testcase1(self):
        self.assertEqual(fibonacci_series_someValue.fibb(8),13)


if __name__=="__main__":
    unittest.main()
