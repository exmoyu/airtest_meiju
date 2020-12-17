# -*- encoding=utf8 -*-
__author__ = "ex_moyu"

from airtest.core.api import *
auto_setup(__file__)

meiju_App = 'com.midea.ai.appliances'#应用名称
phone_num = '13450159108'#测试账号
pass_word = 'a123456'#密码
# home_name = '场景实验室'

tv_home = "com.midea.ai.appliances:id/tv_home"#主页家庭名称
tab_smartCenter = "com.midea.ai.appliances:id/tab_smartCenter"#场景主页tab
pwd_login = "com.midea.ai.appliances:id/pwd_login"#密码登录按钮
et_input = "com.midea.ai.appliances:id/et_input"#手机密码输入框
id_cb = "com.midea.ai.appliances:id/cb"#我已阅读并同意
btn_login = "com.midea.ai.appliances:id/btn_login"#登录按钮


from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True,screenshot_each_action=False)


# 切换家庭
def switch_home(home_name):
    # print(poco(name=tv_home).get_text())
    # 判断主页当前家庭是否目标家庭
    if poco(name=tv_home).get_text() != home_name:
        poco(name=tv_home).click('center')
        poco(type="androidx.recyclerview.widget.RecyclerView",name="com.midea.ai.appliances:id/rv").wait_for_appearance(5)
        # 如果家庭列表有目标家庭则直接点击
        if poco(text=home_name).exists():
            poco(text=home_name).click('center')
        # 否则循环查找家庭列表
        else:
            # 获取家庭列表坐标
            x,y = poco(type="androidx.recyclerview.widget.RecyclerView",name="com.midea.ai.appliances:id/rv").get_position()
            home_exists = False
            # 循环翻页
            while home_exists is False:
                items = poco(type="androidx.recyclerview.widget.RecyclerView",name="com.midea.ai.appliances:id/rv").child("android.view.ViewGroup")
                # 循环查找家庭列表名称
                for item in items:
                    # print(item.child("com.midea.ai.appliances:id/tv_name").get_text())
                    # 匹配家庭名称则点击并结束循环
                    if item.child("com.midea.ai.appliances:id/tv_name").get_text() == home_name:
                        poco(text=home_name).click('center')
                        home_exists = True
                        break
                    else:
                        pass
                # 当前页没有匹配则翻页
                if home_exists is False:
                    end = [x, y - 0.4]
                    poco.swipe([x, y], end)
    else:
        pass
    # print(poco(name=tv_home).get_text())


# 选择主页业务模块
def select_bussi_mould(name_attr):
    poco(name=name_attr).wait_for_appearance(5)
    poco(name=name_attr).click('center')


# 选择场景新玩法
def select_scence_mould(scence_mould_name):
    poco(name="推荐",desc="推荐").wait_for_appearance(5)
    poco(name="推荐",desc="推荐").click()
    # 场景新玩法列表元素定位
    x,y = poco(name="androidx.recyclerview.widget.RecyclerView").get_position()
    scence_mould = False
    # 循环翻页
    while scence_mould is False:
        # 新玩法列表名称元素定位
        items = poco(name="androidx.recyclerview.widget.RecyclerView").child("android.widget.FrameLayout").offspring(type="android.view.View")
        # 循环查找场景列表名称
        for item in items:
            # 匹配场景名称则点击并结束循环
            if item.attr("name") == scence_mould_name:
                item.click('center')
                scence_mould = True
                break
            elif item.attr("name") == "上拉加载":
                item.wait_for_disappearance()
                sleep(5)
            # 找不到场景则触发异常
            elif item.attr("name") == "没有更多了哦":
                raise Exception("没这个场景呀!", scence_mould_name)
            else:
                sleep(5)
        # 当前页没有匹配则翻页
        if scence_mould is False:
            end = [x, y - 0.6]
            poco.swipe([x, y], end)

# 创建手动控制
def create_manual_control():
    poco("android.widget.LinearLayout").offspring("com.midea.ai.appliances:id/container").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout").child("android.widget.FrameLayout")[0].child("android.widget.FrameLayout")[1].child("android.widget.FrameLayout")[1].child("android.widget.FrameLayout")[1].child("android.widget.ImageView").click('center')
    poco(type="android.view.View",name="手动控制").wait_for_appearance(5)
    poco(type="android.view.View",name="手动控制").click('center')
    poco(type="android.view.View",name="添加更多控制").wait_for_appearance(5)
    poco(type="android.view.View",name="添加更多控制").click('center')

# 选择设备
def select_device(device_name):
    poco(type="android.view.View",name="选择设备").wait_for_appearance(5)
    poco(type="android.view.View",name="全部").wait_for_appearance(5)
    poco(name="androidx.recyclerview.widget.RecyclerView").wait_for_appearance(5)
    # 选择设备列表元素定位
    x,y = poco(name="androidx.recyclerview.widget.RecyclerView").get_position()
    swipe_times = 0
    device_found = False
    # 循环翻页
    while swipe_times < 10 and device_found == False:
            # 设备列表名称元素定位
            items = poco(name="androidx.recyclerview.widget.RecyclerView").offspring(type="android.view.View")
            # 循环查找设备列表名称
            for item in items:
                # print(item.attr("name"))
                # 匹配设备名称则点击并结束循环
                if item.attr("name") == device_name:
                    item.click('center')
                    device_found = True
                    break
                else:
                    pass
            # 当前页没有匹配则翻页
            if device_found is False:
                end = [x, y - 0.6]
                poco.swipe([x, y], end)
                swipe_times = swipe_times+1
    if device_found == False:
        raise Exception("没这个设备呀!", device_found)


# 设置设备动作
def setup_device_movement(movement):
    for k1,v1 in movement.items():
        poco(name=k1).wait_for_appearance(5)
        # 如果是一个开关则直接点击该项的开关定位
        if v1 == "onoff":
            poco(name=k1).parent().parent().parent().parent().child()[1].click("center")
        # 如果是勾选项，则点击该项
        elif v1 == "select":
            poco(name=k1).click("center")
        # picker控件则进行滚动操作
        else:
            poco(name=k1).click("center")
            for k2,v2 in v1.items():
                # 等待picker控件
                poco("com.midea.ai.appliances:id/optionspicker").wait_for_appearance(5)
                # 控件最后一列位置
                x,y = poco("com.midea.ai.appliances:id/optionspicker").child("android.view.View")[-1].get_position()
                # 按设定距离滑动
                end = [x, y + v2]
                poco.swipe([x, y], end)
                # 控件确定提交按钮
                poco(name="com.midea.ai.appliances:id/btnSubmit",text="确定").click("center")
    poco(type="android.view.View",name="确定").focus("center").click("center")




