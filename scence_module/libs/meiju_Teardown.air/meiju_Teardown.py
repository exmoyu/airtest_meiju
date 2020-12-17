# -*- encoding=utf8 -*-
__author__ = "ex_moyu"

from airtest.core.api import *

meiju_App = 'com.midea.ai.appliances'

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True,screenshot_each_action=False)

def meiju_Stop():
    stop_app(meiju_App)