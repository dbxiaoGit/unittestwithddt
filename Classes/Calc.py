#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Calc.py
# @Author: Derek
# @Date  : 2017/12/19
# @Desc  :

from common.log_configer2 import logger

class Calc():
    def __init__(self):
        logger.info("Calc init ")
        pass

    def add(self,param1,param2):
        logger.info("excute add ")
        logger.info("param1:%s,param2:%s"%(param1,param2))
        return param1 + param2
