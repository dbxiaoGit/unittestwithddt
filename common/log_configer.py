#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : log_configer.py
# @Author: Derek
# @Date  : 2017/12/21
# @Desc  :

import logging.config
import logging

logging.config.fileConfig("../config/logger.conf")
logger = logging.getLogger()

#logger.debug('This is debug message')
#logger.info('This is info message')
#logger.warning('This is warning message')