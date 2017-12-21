#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : TestJson.py
# @Author: Derek
# @Date  : 2017/12/20
# @Desc  :


import unittest
from ddt import ddt, file_data
from common.log_configer2 import logger
from Classes.Calc import Calc


@ddt
class TestJson(unittest.TestCase):

    @file_data('../testdata/testdata.json')
    def test_add1(self,p1,p2,r):
        logger.info("test_add1 p1:%s,p2:%s,p3:%s"%(p1,p2,r))
        calc = Calc()
        self.assertEqual(r,calc.add(p1,p2))

if __name__ == '__main__':
    unittest.main()