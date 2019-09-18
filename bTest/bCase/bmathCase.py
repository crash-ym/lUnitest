import unittest
import bFunction.bmath as t

class MathTestCase(unittest.TestCase):
    def setUp(self):
        self.a=1
        self.b=2

    def test_sum_1(self):
        self.assertEqual(3, t.sum(self.a,self.b))

    @unittest.skip("暂不执行")
    def test_sum_2(self):
        self.assertNotEqual(3,t.sum(self.a,self.b))

    @unittest.skipIf(t.__version__()<2.0,"版本低于2.0时不执行")
    def test_sum_3(self):
        self.assertEquals(4,t.sum(self.a,self.b))

    @unittest.skipUnless(t.__version__()<2.0,"版本低于2.0时执行")
    def test_sum_4(self):
        self.assertEquals(3,t.sum(self.a,self.b))

if __name__ == '__main__':
    unittest.main(verbosity=2)