"""
健康档案数据
"""
import time
import os
from ph.common.idcard import *
from ph.data.address import *

class JkdaData:
    ju_zhu_di_xiang_xi_di_zhi = '居住地详细地址'
    hu_ji_di_xiang_xi_di_zhi = '户籍地详细地址'
    da_yin_dang_an = '打印档案'

    cur_path = os.path.dirname(os.path.realpath(__file__))
    # 存放文件的上级目录
    idcard_path = os.path.join(os.path.dirname(cur_path), 'data')
    # id_card文件存放和读取的位置
    excel_name = "/id_card.xlsx"
    excel_path = os.path.abspath(idcard_path) + excel_name
    #居民身份证号
    ju_ming_shen_fen_zheng_hao = read_excel_xlsx('/Users/guoxilu/PycharmProjects/webtest/ph/data/id_card.xlsx', 'Sheet1', "B2")
    print('%s'%excel_path)
    print(excel_path)
    # 居民姓名
    ju_min_xing_ming = read_excel_xlsx('/Users/guoxilu/PycharmProjects/webtest/ph/data/id_card.xlsx', 'Sheet1', "A2")
    #居民电话
    ju_ming_dian_hua = read_excel_xlsx('/Users/guoxilu/PycharmProjects/webtest/ph/data/id_card.xlsx', 'Sheet1', "C2")
    #居民工作单位
    ju_min_gong_zuo_dan_wei = read_excel_xlsx('/Users/guoxilu/PycharmProjects/webtest/ph/data/id_card.xlsx', 'Sheet1', "D2")


if __name__ == '__main__':
    print(JkdaData.ju_ming_shen_fen_zheng_hao)
