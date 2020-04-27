import os

'''
获取绝对路径
'''

def get_Path():
    path = os.path.split(os.path.realpath(__file__))[0]
    return path


if __name__ == '__main__':  # 测试

    print('测试路径是否正确，路径为：'+get_Path())