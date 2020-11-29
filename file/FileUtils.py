import os
import sys


class FileUtils:

    def readFile(self, file):
        with open(file, 'r') as f:
            content = f.read()
            print("content: {}".format(content))

    def writeFile(self, file, content):
        with open(file, 'w') as f:
            f.write(content)

    def listFile(self, dir):
        sonFiles = os.listdir(dir)
        for f in sonFiles:
            print(f)




if __name__ == '__main__':

    """
    可以直接读取同级目录下的文件
    """
    file = 'test.txt'

    """
    class 方法有self参数的作为成员方法，也就是非static方法，需要构造类实例进行调用，
    不带self的方法为static方法，可以使用类名直接调用
    """
    fileUtils = FileUtils()

    fileUtils.readFile(file)

    fileUtils.writeFile(file, 'some value 2')

    fileUtils.readFile(file)

    dir = 'C:/Users/dangdang/PycharmProjects/python-learn/file'
    fileUtils.listFile(dir)
