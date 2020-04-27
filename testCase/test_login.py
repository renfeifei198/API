from common.configHttp import RunMain
from testFile.read_Excel import readExcel
from testFile.get_urlParams import geturlParams
from testFile.write_Excel import writeExcel
from testFile.generateData import generate
import json
import unittest
import paramunittest # unittest参数化模块
import urllib.parse
import ast


url = geturlParams().get_Url() # 获取url：http://127.0.0.1:8888
login_xls = readExcel().get_row('login_case.xlsx','login')
caseID = generate().generateCaseID('login')
write = writeExcel()

@paramunittest.parametrized(*login_xls) # 使用paramunittest传入获取的参数
class testUserLogin(unittest.TestCase):
    '''登录接口'''
    def setParameters(self,case_id,case_name,path,query,method,ExpectResult,TestResult):
        self.case_id = str(case_id)
        self.case_name = str(case_name)
        self.path = str(path)
        self.query = str(query)
        self.method = str(method)
        self.ExpectResult = ast.literal_eval(ExpectResult)
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def CheckResult(self):
        '''调用RunMain().run_main()发送请求'''
        url_path = url+self.path+'?'
        new_url = url_path+self.query
        request_url = url+self.path
        data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(new_url).query))
        send_request = RunMain().run_main(self.method,request_url,data)
        self.response = json.loads(send_request)

    def test_login(self):
        '''登录成功'''
        self.CheckResult()
        for i in caseID:
            if self.case_id == i:
                print(i)
                self.assertEqual(self.response,self.ExpectResult)
                print(self.response,self.ExpectResult)

if __name__ == '__main__':
    unittest.main()
