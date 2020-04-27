from common.configHttp import RunMain
from testFile.read_Excel import readExcel
from testFile.get_urlParams import geturlParams
import json
import unittest
import urllib.parse

class login(unittest.TestCase):
    '''登录接口测试'''

    def setUp(self):
        self.url = str(geturlParams().get_Url()) # 获取url：http://127.0.0.1:8888
        self.login_api = str(readExcel().get_xls('login_case.xlsx', 'login')[0][1]) # 获取接口/login
        self.login_params = str(readExcel().get_xls('login_case.xlsx', 'login')[0][2]) # 获取请求参数
        self.method = str(readExcel().get_xls('login_case.xlsx', 'login')[0][3]) # 获取请求方式
        self.new_url = self.url+self.login_api
        self.complete_url = self.new_url+'?'+self.login_params # 完整的url：http://127.0.0.1:8888/login?name=lizonglin&pwd=888888
        self.data = dict(urllib.parse.parse_qsl(urllib.parse.urlsplit(self.complete_url).query)) # 把complete_url中的name=&pwd=转换为{'name':'XXX','pwd':'XXX'}

    def test_loginSuccess(self):
        '''账号密码正确'''
        info = RunMain().run_main(self.method,self.new_url,self.data)
        ss = json.loads(info)
        if ss['code'] == 200:
            self.assertEqual(ss['code'],200)
        else:
            print('写入FAIL')

    def tearDown(self):
        pass

if __name__ == '__main__':

    unittest.main()