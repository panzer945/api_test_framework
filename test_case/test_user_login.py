import unittest
import requests
from common.read_excel import *  # 导入read_excel中的方法
import json  # 用来转化excel中的json字符串为字典
from config.log_conf import *
from test_case.basecase import *
from config.config_params import *

class TestUserLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):   # 整个测试类只执行一次
        cls.data_list = excel_to_list(data_file, "TestUserLogin")  # 读取该测试类所有用例数据
        # cls.data_list 同 self.data_list 都是该类的公共属性

    def test_user_login_normal(self):
        case_data = get_test_data( self.data_list,'test_user_login_normal')   # 从数据列表中查找到该用例数据
        if not case_data:   # 有可能为None
            logging.error("用例数据不存在")

        case_name=case_data.get('case_name')
        url = case_data.get('url')   # 从字典中取数据，excel中的标题也必须是小写url
        method=case_data['method']
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据
        # headers=case_data.get('headers')

        res=requests.request(url=url,method=method,data=json.loads(data))  # 表单请求，数据转为字典格式
        res_text=res.text

        log_case_info(case_name,url,method,data,expect_res,res_text)        #输出用例日志信息
        self.assertEqual(res.text, expect_res)  # 改为assertEqual断言

    def test_user_login_password_wrong(self):
        case_data = get_test_data( self.data_list,'test_user_login_password_wrong')
        if not case_data:
            print('用例数据不存在')


        case_name=case_data.get('case_name')
        url = case_data.get('url')   # 从字典中取数据，excel中的标题也必须是小写url
        method=case_data.get('method')
        data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
        expect_res = case_data.get('expect_res')  # 期望数据

        res=requests.request(url=url,method=method,data=json.loads(data))
        res_text=res.text

        log_case_info(case_name,url,method,data,expect_res,res_text)           #输出用例日志信息

        self.assertEquals(res.text,expect_res)


# if __name__ == '__main__':   # 非必要，用于测试我们的代码
#     unittest.main(verbosity=2)