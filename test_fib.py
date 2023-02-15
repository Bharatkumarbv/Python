import sys
sys.path.append("D:\python")

import unittest
import fibonacci_series

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(fibonacci_series.fib(7),(11235813))
    def testcase2(self):
        self.assertEqual(fibonacci_series.fib(6),(112358))


if __name__=="__main__":
    unittest.main()
