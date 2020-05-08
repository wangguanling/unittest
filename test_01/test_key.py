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



class Test_Key(unittest.TestCase):
    def setUp(self):
        self.dev = connect_device("Windows:///")
        self.app = Application(backend="win32").start(r"C:\BurningRock\ctGMAS\ctGMAS-client.exe")
        self.dlg_spec = pywinauto.Application(backend="win32").connect(path=r"C:\BurningRock\ctGMAS\ctGMAS-client.exe")

    #配置问题
    def test_config(self):
        time.sleep(1)
        self.dlg_spec["SWT_Window0"].配置.click()
        self.dlg_spec["配置"]["Edit"].SetEditText("http://172.16.110.170:8081/")

        try:
            #判断能否正常的静茹配置文件中
            if assert_exists(Template("../img/基础配置.jpg")):

                time.sleep(1)
                self.dlg_spec["配置"]["Edit2"].SetEditText("172.16.110.170")
                self.dlg_spec["配置"]["Edit3"].SetEditText("914a24b6-aeb6-1036-8698-ed2d19f585b8")
                self.dlg_spec["基础配置"].保存.click()
                self.dlg_spec['SWT_Window0'].Edit.SetEditText('tmadmin')
                self.dlg_spec['SWT_Window0'].Edit2.type_keys("12345678")
                self.dlg_spec["SWT_Window0"].登录.click()
                touch(Template("../img/close.png"))
                time.sleep(1)
                self.dlg_spec["提示"].确定.click()
        except AssertionError as e:
            print(e)
            time.sleep(2)
            raise



    def tearDown(self) -> None:
        pass

