import os
from config.log_conf import *
from config.config_params import *

def latest_report():
    #报告存放位置
    report_dir=report_path
    print(report_dir)
    #返回文件夹中包含的文件或列表
    lists=os.listdir(report_dir)
    print(lists)
    # 按时间顺序对该目录文件夹下的文件进行排序(从最近开始)
    lists.sort(key=lambda fn:os.path.getatime(report_dir+"\\"+fn))
    # print("latest report is %s"%lists[-1])

    # 输出最新报告的路径
    file=os.path.join(report_dir,lists[-1])
    # logging.DEBUG('发送测试报告:{}'.format(str(file)))

    return file


# if __name__ == '__main__':
    # file=latest_report()



