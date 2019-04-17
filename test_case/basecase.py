import json
from config.log_conf import *
import unittest
from common.read_excel import *
from config import *
import requests


def log_case_info(case_name,url,method,data,expect_res,res_text):

    logging.info("测试用例:{}".format(case_name))
    logging.info("url:{}",format(url))
    logging.info("method:{}".format(method))
    logging.info("请求参数:{}".format(data))
    # logging.info("数据类型:{}".format(data_type))
    logging.info("预期结果:{}".format(expect_res))
    logging.info("实际结果:{}".format(res_text))

    # def send_request(self):
    #     case_name=case_data.get('case_name')
    #     url = case_data.get('url')   # 从字典中取数据，excel中的标题也必须是小写url
    #     args = case_data.get('args')
    #     method=case_data['method']
    #     data = case_data.get('data')  # 注意字符串格式，需要用json.loads()转化为字典格式
    #     expect_res = case_data.get('expect_res')  # 期望数据
    #     headers=case_data.get('headers')
    #     data_type=case_data.get('data_type')
    #
    #     if method.upper()=='GET':
    #         res = requests.get(url=url,headers=headers, params=json.loads(args))
    #
    #     elif data_type.upper()=='FORM':
    #         res=requests.post(url=url,headers=json.loads(headers),params=json.loads(data))
    #         res_text=res.text
    #         self.log_case_info(case_name,url,method,data,expect_res,res_text)
    #         self.assertEqual(res.text, expect_res)
    #
    #     else:
    #         res = requests.post(url=url, json=json.loads(args), headers=json.loads(headers))   # JSON格式请求
    #         self.log_case_info(case_name, url, args, json.dumps(json.loads(expect_res), sort_keys=True),
    #                       json.dumps(res.json(), ensure_ascii=False, sort_keys=True))
    #         self.assertDictEqual(res.json(), json.loads(expect_res))

