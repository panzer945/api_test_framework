import logging
import os
from config.config_params import *


# file_path=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'/log_file/'

logging.basicConfig(level=logging.DEBUG,  # log level
                    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',  # log格式
                    datefmt='%Y-%m-%d %H:%M:%S',  # 日期格式
                    # filename=file_path+'log.txt',  # 日志输出文件
                    filename=log_path,
                    filemode='a')  # 追加模式

if __name__ == '__main__':
    logging.info("hello")