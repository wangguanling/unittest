from msilib.schema import ListBox

from pywinauto import Application
# auto_setup(__file__)
from airtest.core.api import *
import time
# from pywinauto import Application
import pywinauto
# 开启测试
from airtest.core.api import connect_device
from PIL import  ImageGrab
import unittest

class Test(unittest.TestCase):
    # 软件初始化
    def setUp(self):
        time.sleep(3)
        self.dev=connect_device("Windows:///")
        self.app = Application(backend="win32").start(r"C:\BurningRock\ctGMAS\ctGMAS-client.exe")
        self.dlg_spec = pywinauto.Application(backend="win32").connect(path=r"C:\BurningRock\ctGMAS\ctGMAS-client.exe")
    #登录软件
    # self.dlg_spec.wait(timeout ="2")
    def test_landing(self):
        time.sleep(1)
        self.dlg_spec["SWT_Window0"].配置.click()
        self.dlg_spec["配置"]["Edit"].SetEditText("http://172.16.110.170:8081/")
        time.sleep(1)
        self.dlg_spec["配置"]["Edit2"].SetEditText("172.16.110.170")
        self.dlg_spec["配置"]["Edit3"].SetEditText("914a24b6-aeb6-1036-8698-ed2d19f585b8")
        self.dlg_spec["基础配置"].保存.click()
        self.dlg_spec['SWT_Window0'].Edit.SetEditText('tmadmin')
        self.dlg_spec['SWT_Window0'].Edit2.type_keys("12345678")
        self.dlg_spec["SWT_Window0"].登录.click()

        try:
            if assert_exists(Template("../img/close.png","判断密码正确是否能够正常登录")):
                touch(Template("../img/close.png"))
                time.sleep(1)
                self.dlg_spec["提示"].确定.click()

        except AssertionError as e:
            time.sleep(2)
            self.dlg_spec["登录失败"].OK.click()
            self.dlg_spec["SWT_Window0"].退出.click()
            self.dlg_spec["提示"].确定.click()
            print(e)
            raise


        # else:
        #         #     print("登录失败")
        #         #     self.dlg_spec["登录失败"].OK.click()
        #         #     self.dlg_spec["SWT_Window0"].退出.click()
        #         #     self.dlg_spec["提示"].确定.click()
        #         #     print("登录失败")

    def tearDown(self) -> None:
        pass





































