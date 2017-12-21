#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : log_configer2.py.py
# @Author: Derek
# @Date  : 2017/12/21
# @Desc  :

import logging

import sys

import os

filepth = os.path.dirname(os.path.realpath(__file__))

hand01 = logging.StreamHandler(stream=sys.stdout)
hand02 = logging.FileHandler(filename=filepth + '/../logs/application.log', mode='a')
hand03 = logging.FileHandler(filename=filepth + '/../logs/application_current.log', mode='w')

handers_= [hand01, hand02, hand03]
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s %(funcName)s [line:%(lineno)d] %(levelname)s %(message)s',
                handlers=handers_
                )

logger = logging.getLogger()

#logger.debug('This is debug message')
