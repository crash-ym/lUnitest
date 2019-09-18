import unittest
import bFunction.bmath as mh

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.a=2
        self.b=3

    def test_case_1(self):
        self.assertEqual(3, mh.sum(1,2))

    @unittest.skip("暂不执行")
    def test_sum_2(self):
        self.assertNotEqual(3,mh.sum(self.a,self.b))

    @unittest.skip(mh.__version__()<2.0)
    def test_sum_3(self):
        self.assertEquals(4,mh.sum(self.a,self.b))

if __name__ == '__main__':
    unittest.main(verbosity=2)