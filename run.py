from testCase.test_login import testUserLogin
from testFile.getPath import get_Path
import common.HTMLTestRunner as HTMLTestRunner
import unittest
import os
import time

testunit = unittest.TestSuite()
testunit.addTest(testUserLogin('test_login'))
now_time = time.strftime('%Y-%m-%d %H%M%S')
filename = (os.getcwd()+'\\result\\'+now_time+'.html')
TestReport = open(filename,'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=TestReport,description='TestCase Implementation Situation')
runner.run(testunit)
TestReport.close()
