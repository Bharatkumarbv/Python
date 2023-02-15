import sys
sys.path.append("D:\python")

import unittest
import index_position_remove

class Bharat(unittest.TestCase):
    def testcase(self):
        self.assertEqual(index_position_remove.ind("bharat",3),"bhrat")
    def testcase1(self):
        self.assertEqual(index_position_remove.ind("kumar",2),"kmar")


if __name__=="__main__":
    unittest.main()
