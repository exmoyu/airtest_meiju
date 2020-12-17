# -*- encoding=utf8 -*-
__author__ = "ex_moyu"

# import logging
# logger = logging.getLogger("airtest")
# logger.setLevel(logging.ERROR)

auto_setup(__file__)

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


tab_smartCenter = "com.midea.ai.appliances:id/tab_smartCenter"#场景主页tab


# using("meiju_Setup.air")
# from meiju_Setup import *
# testcase_Setup()


using("comm_Keywords.air")
from comm_Keywords import *

# switch_home('音箱家')
# select_bussi_mould(tab_smartCenter)
# # select_scence_mould("定时进入安防模式")


# 创建手动控制
manual_control_name = "手动场景名称"
create_manual_control()

device_name = "空调"
select_device(device_name)

# movement = {"电源":"onoff", "模式":{"睡眠风":-0.04}, "摇头":"onoff", "档位":{"3档":0.04}, "延时执行":{"延时1秒":-0.04}}
movement = {"电源":{"开/关":-0.04},"运行时长":{"0.5小时":-0.04}, "模式":{"制冷":0.12}, "温度":{"30°C":0.04}, "风速":{"中速风":0.08}, "风向":{"不摆风":0.04}, "延时执行":{"延时1秒":-0.04}}
# movement = {"打开一路开关":"select", "延时执行":{"延时1秒":-0.04}}
setup_device_movement(movement)

poco(type="android.view.View",name="创建").wait_for_appearance(5)
poco(type="android.view.View",name="创建").focus("center").click("center")
poco(type="android.view.View",name="请输入").wait_for_appearance(5)
poco(type="android.view.View",name="请输入").focus("center").click("center")
poco(name="android.widget.EditText",text="最多输入15个字").wait_for_appearance(5)
poco(name="android.widget.EditText",text="最多输入15个字").set_text(manual_control_name)
poco(name="完成",desc="完成").focus("center").click("center")

poco(name="保存",desc="保存").focus("center").click("center")

poco(name="添加该场景到手机桌面").wait_for_appearance(5)
poco(name="完成").focus("center").click("center")

# 验证新建手动场景
# poco(name="手动控制").wait_for_appearance(5)



# using("meiju_Teardown.air")
# from meiju_Teardown import meiju_Stop
# meiju_Stop()