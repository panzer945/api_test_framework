import time
# from BSTestRunner import BSTestRunner
from test_case.test_user_login import *
import os
import unittest
from config.email_conf import *
from config.config_params import *
from common.HTMLTestRunnerCN import HTMLTestRunner

test_dir=test_path
report_dir=report_path

logging.info('---------测试开始---------------')
# discover=unittest.defaultTestLoader(test_dir,'test_user_*.py')
discover=unittest.defaultTestLoader.discover(test_dir,pattern=test_case)

now=time.strftime('%Y-%m-%d %H_%M_%S')
report_name=report_dir+'/'+now+' test_report.html'
#打开文件并写入执行后的报告
with open(report_name,'wb') as f:
    runner=HTMLTestRunner(stream=f,title=report_title,description=report_desc,tester=tester)
    runner.run(discover)

#发送测试报告邮件
if send_email_after_run:     #判断是否需要发送邮件
    send_email()

logging.info('--------------测试结束---------------')

