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


def testcase_Setup():
#     clear_app(meiju_App)
    start_app(meiju_App)
    poco(name=tv_home).wait_for_appearance(5)
    if poco(name=tv_home).get_text() == '未登录':
        poco(name=tv_home).click('center')
        if poco(name=btn_login).get_text() == '本机号码一键登录':
            poco(name=id_cb).click('center')
            poco(name=btn_login).click('center')
        else:
            poco(name=pwd_login).wait_for_appearance(5)
            poco(name=pwd_login).click('center')
            poco(name=et_input).wait_for_appearance(5)
            poco(name=et_input,text='请输入手机号码').set_text(phone_num)
            poco(name=et_input,text='请输入密码').set_text(pass_word)
            poco(name=id_cb).click('center')
            poco(name=btn_login).click('center')
    else:
        pass



