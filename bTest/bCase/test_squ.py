import unittest
import bFunction.bmath as mh

class MyTestCase(unittest.TestCase):
    @unittest.expectedFailure
    def test_case_1(self):
        self.assertEqual(1, mh.squ(1,0),msg='ZERO EXCEPTION')


class SquTestCase(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(1,mh.squ(1,1))

    def test_case_2(self):
        self.assertEqual(0,mh.squ(0,2))


if __name__ == '__main__':
    unittest.main(verbosity=2)
