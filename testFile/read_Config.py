import os
import configparser # 读取ini配置文件模块
from testFile.getPath import get_Path # 自己写的gepPath获取配置文件路径方法


config_path = get_Path()+'\config.ini'
config = configparser.ConfigParser()  # 调用读取配置文件的方法
config.read(config_path, encoding='utf-8')

'''
读取配置
'''
class ReadConfig():

    # 读取http配置
    def get_http(self, name):
        value = config.get('HTTP', name)
        return value

    # 读取email配置
    def get_email(self, name):
        value = config.get('EMAIL', name)
        return value

    # 读取数据库配置
    def get_mysql(self, name):
        value = config.get('DATABASE', name)
        return value


if __name__ == '__main__':  # 测试

    print('HTTP中的baseurl值为：', ReadConfig().get_http('baseurl'))
    print('EMAIL中的开关on_off值为：', ReadConfig().get_email('on_off'))