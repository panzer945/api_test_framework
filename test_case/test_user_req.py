import json
import unittest
import requests
from common.read_excel import *
from config.db_conf import *
from config.log_conf import *
from test_case.basecase import *


class TestUserReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list((os.path.join(data_path,"test_user_data.xlsx")), "TestUserReg")  # 读取TestUserReg工作簿的所有数据

    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list, 'test_user_reg_normal')
        if not case_data:
            logging.error("用例数据不存在")


        case_name=case_data.get('case_name')
        url = case_data.get('url')
        method=case_data['method']
        data = json.loads(case_data.get('data'))  # 转为字典，需要取里面的name进行数据库检查
        expect_res = json.loads(case_data.get('expect_res'))  # 转为字典，断言时直接断言两个字典是否相等
        name = data.get("name")  # 范冰冰

        # 环境检查
        if check_user(name):
            del_user(name)
        # 发送请求
        res = requests.request(method=method,url=url, json=data)  # 用data=data 传字符串也可以
        res_text=res.text

        log_case_info(case_name,url,method,data,expect_res,res_text)           #输出用例日志信息

        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), expect_res)
        # 数据库断言
        self.assertTrue(check_user(name))
        # 环境清理（由于注册接口向数据库写入了用户信息）
        del_user(name)

    def test_user_reg_exist(self):
        case_data=get_test_data(self.data_list,'test_user_reg_exist')
        if not case_data:
            print("用例数据不存在")
        case_name=case_data.get('case_name')
        url=case_data.get('url')
        method=case_data.get('method')
        data=case_data.get('data')
        expect_res=data_list('except_res')

         # 环境检查
        if not check_user(case_data):
            add_user(case_name,'123456')


        # 发送请求
        res = requests.request(url=url,method=method, json=data)
        res_text=res.text

        # 期望响应结果，注意字典格式和json格式的区别（如果有true/false/null要转化为字典格式）
        
        log_case_info(case_name,url,method,data,expect_res,res_text)           #输出用例日志信息

        # 响应断言（整体断言）
        self.assertDictEqual(res.json(), expect_res)

        # 数据库断言(没有注册成功，数据库没有添加新用户)

        # 环境清理（无需清理）

if __name__ == '__main__':    # 非必要，用于测试我们的代码
    unittest.main(verbosity=2)