import logging
import os
import time

# 项目路径
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)) ) # 当前文件的绝对路径的上一级，__file__指当前文件
# 数据路径
data_path = prj_path+'/data'
#文件名
data_file="test_user_data.xlsx"
# 用例路径
test_path = prj_path+'/test_case'
#报告路径
report_path=prj_path+'/test_report'
# #日志路径
# log_path=prj_path+'/log_file'

#日志保存路径，按天生成日志文件
today = time.strftime('%Y%m%d', time.localtime())
log_path = os.path.join(prj_path+'/log_file', 'log_{}.txt'.format(today))
# report_file = os.path.join(prj_path+'/test_report', 'report.html')  # 也可以每次生成新的报告


# 数据库配置
db_host = '127.0.0.1'   # 自己的服务器地址
db_port = 3306
db_user = 'admin'
db_passwd = ''
db_db = 'api_test'
db_charset='utf8'

# 邮件配置
smtp_server = 'smtp.163.com'
smtp_user = '18307202665@163.com'
smtp_password = 'panzer123'

sender = smtp_user  # 发件人
# receiver = '2312097011@qq.com' # 单个收件人
receiver=[ '2312097011@qq.com','1729884593@qq.com']   # 多个收件人
subject = '接口测试报告'  # 邮件主题
att_filename="report.html"     #附件名字

#增加邮件发送开关
send_email_after_run=True

#测试内容
test_case='test_user_login.py'     #测试标题


#报告内容
report_title=' API Test '
report_desc='测试描述'
tester='marble'
