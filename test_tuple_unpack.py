import sys
sys.path.append("D:\python")

import unittest
import tuple_modify

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(tuple_modify.tup((1,2,3),("hai","hello","how")),(1,2))
    def testcase2(self):
        self.assertEqual(tuple_modify.tup((5,6,7),("bharat","sandeep","vamsi")),(5,6))


if __name__=="__main__":
    unittest.main()
