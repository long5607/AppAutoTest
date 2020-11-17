# -*- coding: utf-8 -*-
# @Time    : 2018/12/4 9:26
# @Author  : Guo
# @Email   : 314171455@qq.com
# @File    : test.py
# @Software: PyCharm

import time

from appium import webdriver

capabilities = {
    "deviceName": "127.0.0.1:21503",
    "app": "C:\\Users\\Huyc\\Desktop\\APP\\app-yyb-release-2.7.3-201811230932.apk",
    "platformName": "Android"
    }
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub",capabilities)
time.sleep(10)