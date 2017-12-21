#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : run_test.py.py
# @Author: Derek
# @Date  : 2017/12/21
# @Desc  :

import unittest
from common.HTMLTestRunner import HTMLTestRunner
import time

if __name__ == "__main__":
    # test_data.init_data() # 初始化接口测试数据
    # 指定测试用例为当前文件夹下的 test_case 目录
    test_dir = './testcase'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Test*.py')

    now = time.strftime("%Y-%m-%d")
    filename = './report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='Test Result',
                            description='The results are following:')
    runner.run(discover)
    fp.close()