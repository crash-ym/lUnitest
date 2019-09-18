import unittest
import bFunction.bmath as mh

class MyTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(3, mh.mul(5,2))

    def test_case_2(self):
        self.assertEqual(3, mh.mul(3,0))

    def test_case_3(self):
        self.assertEqual(3, mh.mul(0,-3))

if __name__ == '__main__':
    unittest.main(verbosity=2)

