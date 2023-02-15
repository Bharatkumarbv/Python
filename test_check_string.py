import sys
sys.path.append("D:\python")

import unittest
import sup

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(sup.search(["bharath","bhiryani","bhoom"],"bha"),["bharath"])
    def testcase1(self):
        self.assertEqual(sup.search(["bharathkumar", "bhimavaram"],"a"),[])


if __name__=="__main__":
    unittest.main()
