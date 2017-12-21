#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : TestYaml.py
# @Author: Derek
# @Date  : 2017/12/21
# @Desc  :
import unittest

from ddt import ddt, file_data

from Classes.Calc import Calc
from common.log_configer2 import logger


@ddt
class TestYaml(unittest.TestCase):

    @file_data('../testdata/testdata.yaml')
    def test_add1(self,p1,p2,r):
        logger.info("test_add1 p1:%s,p2:%s,r:%s"%(p1,p2,r))
        calc = Calc()
        self.assertEqual(r,calc.add(p1,p2))

if __name__ == '__main__':
    unittest.main()