import unittest
import bTest.bCase.bmathCase as case


def suit():
    suit = unittest.TestSuite()
    suit.addTest(case.MathTestCase('test_sum_1'))
    suit.addTest(case.MathTestCase('test_sum_2'))
    suit.addTest(case.MathTestCase('test_sum_3'))
    suit.addTest(case.MathTestCase('test_sum_4'))
    return suit

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    res = runner.run(suit())
    print(res)
