import unittest
import time
import os
import bTest.HTMLTestRunner
import bTest.sendEmail

if __name__ == '__main__':

    test_dir = '../bcase'
    report_dir = '../report'

    now = time.strftime("%Y-%m-%d %H-%M-%S")
    filename = report_dir + '/' +  'test_result'+ now + '.html'

    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')

    #print(discover)
    fp = open(filename,'wb')
    runner = bTest.HTMLTestRunner.HTMLTestRunner(stream =  fp, title = u"接口测试报告", description = u"测试用例执行情况：")
    runner.run(discover)
    fp.close()

    bTest.sendEmail.mail(filename)
    #runner = unittest.TextTestRunner()
    #result = runner.run(discover)
    #print(result.testsRun)