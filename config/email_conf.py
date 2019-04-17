import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart  # 混合MIME格式，支持上传附件
from email.header import Header  # 用于使用中文邮件主题
from config.log_conf import *
from config.report_conf import *
from config.config_params import *


def send_email():
    report_file=latest_report()
    msg = MIMEMultipart()  # 混合MIME格式
    msg.attach(MIMEText(open(report_file, encoding='utf-8').read(), 'html', 'utf-8'))  # 添加html格式邮件正文（会丢失css格式）

    msg['From'] = sender  # 发件人

    if isinstance(receiver,list):
        msg['To'] = ','.join(receiver)  # 多个收件人
    else:
        msg['To']=receiver            #单个收件人


    msg['Subject'] = Header(subject, 'utf-8')  # 中文邮件主题，指定utf-8编码

    att1 = MIMEText(open(report_file, 'rb').read(), 'base64', 'utf-8')  # 二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename={}'.format(att_filename)  # filename为邮件中附件显示的名字
    msg.attach(att1)

    try:
        smtp = smtplib.SMTP_SSL('smtp.163.com',465)  # smtp服务器地址 使用SSL模式
        smtp.login(smtp_user, smtp_password)  # 用户名和密码
        logging.info(("-----------开始发送邮件----------"))
        smtp.sendmail(sender,receiver, msg.as_string())     #发送邮件
        logging.info("-----------邮件发送完成！-----------")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()