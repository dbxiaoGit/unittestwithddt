# coding:utf-8

'''
project:ddt数据驱动
'''
import unittest
from ddt import ddt,data
from common.ExcelData import Excel
from common.log_configer2 import logger
from Classes.Calc import Calc

# 测试数据
excel_data = Excel()
testdata = excel_data.get_list('Sheet1')
print(testdata)

@ddt
class TestExcel(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('开始测试---------------')

    @data([1,2,3][2,2,4])
    def test_add1(self,p1,p2,r):
        logger.info("test_add1 p1:%s,p2:%s,p3:%s"%(p1,p2,r))
        calc = Calc()
        self.assertEqual(r,calc.add(p1,p2))

    @classmethod
    def tearDownClass(cls):
        print('结束测试---------------')

if __name__=='__main__':
    unittest.main()