# -*- coding: utf-8 -*-

'''
封装一些基本函数
'''


# 写入txt文件
def write_txt(path, content,type):
    '''
    path : '/tmp/test.txt'
    content: 'hello boy'
    type : "r" w a r+ a+ w+ b
    '''
    fw = open(path, type)
    fw.write(content)
    fw.close()

#读取txt
def read_txt(path,type):
    '''
        path : '/tmp/test.txt'
        type : "r" w a r+ a+ w+ b
        '''
    fw = open(path, type)
    list = []
    for i in fw:
        list.append(i)
    a = len(list)
    print(list[(len(list) - 1)])
    return list[(len(list) - 1)]

#
if __name__ == '__main__':
    read_txt("/Users/guoxilu/PycharmProjects/webtest/ph/data/packagename.txt", "r")


# list = []
    # list.append(pacname)
    # fw = open("/Users/guoxilu/PycharmProjects/webtest/ph/data/packagename.txt", 'w')  # 将要输出保存的文件地址
    # for line in list:
    #     fw.write("\"pacName\":\"" + line.rstrip("\n") + "\"")  # 将字符串写入文件中
    #     fw.write("\n")  # 换行