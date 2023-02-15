import sys
sys.path.append("D:\python")

import unittest
import tuple_convert_dict

class Bharat(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(tuple_convert_dict.convert(('1','2'),('9','8'),('7','6'),('5','2')),({'1':'2', '9': '8', '7': '6', '5': '2'}))
    def testcase2(self):
        self.assertEqual(tuple_convert_dict.convert(('1','2'),("3",'4'),("bha","2"),('bh','df')),({'1': '2', '3': '4', 'bha': '2', 'bh': 'df'}))


if __name__=="__main__":
    unittest.main()
