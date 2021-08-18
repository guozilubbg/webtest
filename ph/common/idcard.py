import random
import datetime
import openpyxl
from faker import Faker
import pandas
import os
import time
from ph.common.phonenum import creat_phone


# 功能：从csv文件中读取一个区域编码字典
# 输入：文件名称
def areaCodeDict(fileName):
    dataDict = {}
    key = 0
    value = 1
    dataLine = open(fileName, encoding="utf-8").read().splitlines()
    for line in dataLine:
        tmpLst = line.split(",")
        dataDict[tmpLst[key]] = tmpLst[value]
    return dataDict


# 功能：随机生产一个区域码
def areaCode(Dict, areanum=None):
    codeList = []
    codeList1 = []
    for key in Dict.keys():
        if areanum == None:
            codeList1.append(key)
            lenth = len(codeList1) - 1
            i = random.randint(0, lenth)
        elif areanum[0] == key[0] and areanum[1] == key[1]:  # 生成某一地区身份证号
            codeList.append(key)
            lenth = len(codeList) - 1
            i = random.randint(0, lenth)
    if areanum == None:
        return codeList1[i]
    else:
        return codeList[i]


# 功能：随机生成1930年之后的出生日期
def birthDay():
    d1 = datetime.datetime.strptime('1930-01-01 00:00:00', '%Y-%m-%d %H:%M:%S')
    d2 = datetime.datetime.now()
    delta = d2 - d1
    dys = delta.days
    i = random.randint(0, dys)
    dta = datetime.timedelta(days=i)
    bhday = d1 + dta
    return bhday.strftime('%Y%m%d')


# 功能：随机生成3位序列号
def ordrNum():
    odNum = random.randint(100, 999)  # 随机生成100到999之间的3为数据
    sex = odNum % 2
    return (str(odNum), sex)


# 功能：生成校验码 https://www.jb51.net/article/53784.htm
def check(id_num):
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                 '10': '2'}  # 校验码映射
    for i in range(0, len(id_num)):
        count = count + int(id_num[i]) * weight[i]
    return checkcode[str(count % 11)]  # 算出校验码


# 每次生成一个生份证号
def creatidcard(write_type=None, areanum=None):
    '''
    write_type: a(append) ,w(write)
    areanum is str
    eg areanum = "54
    '''
    areanum = areanum
    idcard_list = []
    fake = Faker('zh_CN')
    fileName = "./国家地区数据表.csv"  # 区域文件地址
    areaCodeDt = areaCodeDict(fileName)  # 调用生成字典
    areaCd = areaCode(areaCodeDt, areanum=areanum)  # 生成区域码
    areaCdName = areaCodeDt[areaCd]  # 获取区域名称
    birthDy = birthDay()  # 生成出生日期
    (ordNum, sex) = ordrNum()  # 生成顺序号和性别
    checkcode = check((areaCd + birthDy + ordNum))  # 生产校验码
    id_card = areaCd + birthDy + ordNum + checkcode  # 拼装身份证号
    dict = (fake.simple_profile(sex=None))  # 随机生成一个名字
    phonenum = creat_phone()
    idcard_list.append([dict.get('name'), id_card, phonenum, fake.company()])
    if write_type == 'a':
        # 追加写入到本地
        append_excel(idcard_list)
    elif write_type == 'w' or write_type == None:
        # 保存到本地
        saveexcel(idcard_list)
    # print(idcard_list)
    return idcard_list


# 生成多组身份证号，不限制地区
def creatidcards(num):
    '''
    num is int
    '''
    idcareds_list = []
    for _ in range(num):
        fake = Faker('zh_CN')
        dict1 = (fake.simple_profile(sex=None))
        phonenums = creat_phone()
        idcareds_list.append([dict1.get('name'), fake.ssn(), phonenums, dict1.get('address')])
    savelocal = saveexcel(idcareds_list)

    print(idcareds_list)
    return idcareds_list


# 创建excel并将list写入excel
def saveexcel(list):
    cur_path = os.path.dirname(os.path.realpath(__file__))
    idcard_path = os.path.join(os.path.dirname(cur_path), 'data')
    # 如果不存在这个文件夹，就自动创建一个
    if not os.path.exists(idcard_path): os.mkdir(idcard_path)
    df = pandas.DataFrame(list, columns=['id_name', 'id_card', 'telephonenumber', 'address'])
    # idcardname = os.path.join(idcard_path, '%s.xlsx' % time.strftime('%Y_%m_%d %H_%M_%S'))
    idcardname = os.path.join(idcard_path, 'id_card.xlsx')
    df.to_excel(idcardname, sheet_name="Sheet1", index=False)


# 追加写入excel
def append_excel(content_list):
    """
    excel文件中追加内容
    :return:
    content_list:待追加的内容列表
    """
    ds = pandas.DataFrame(content_list)
    excel_name = "/id_card.xlsx"
    cur_path = os.path.dirname(os.path.realpath(__file__))
    # print(cur_path)
    idcard_path = os.path.join(os.path.dirname(cur_path), 'data')
    # print(idcard_path)
    excel_path = os.path.abspath(idcard_path) + excel_name
    # print(excel_path)
    df = pandas.read_excel(excel_path, header=None)
    df = df.append(ds, ignore_index=True)
    df.to_excel(excel_path, index=False, header=False)


# 从excel读出数据
def read_excel_xlsx(path, sheet_name, num=None):
    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]
    if num == None:
        for row in list(sheet.rows)[1:]:
            for cell in row:
                print(cell.value, "\n", end="")
            print()
    else:
        b = sheet["%s"%str(num)]
        # print(f'{b.value}')
        return (f'{b.value}')
    # print(sheet.rows)


# if __name__ == "__main__":
    # creatidcard("a", "54")
    # read_excel_xlsx('/Users/guoxilu/PycharmProjects/webtest/ph/data/id_card.xlsx', "Sheet1",'B2')
    # a = creatidcard("54")
    # name = [c[0] for c in a][0]
    # id = [c[1] for c in a][0]
    # tell = [c[2] for c in a][0]
    # add = [c[3] for c in a][0]
    #
    # print(name, id, tell, add)
