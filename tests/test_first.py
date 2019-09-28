import os
import base64
from time import sleep
import sys

import unittest
import HtmlTestRunner

from appium import webdriver

# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

class SimpleAndroidTests(unittest.TestCase):
    def setUp(self):
        print(f"Test device : {sys.argv[1]}")
        desired_caps = {
            'automationName': 'UiAutomator2',
            'platformName': 'Android',
            'deviceName': 'dummy',
            'udid': sys.argv[2],
            'autoGrantPermissions': True,
            'app': 'https://17438-30791823-gh.circle-artifacts.com/0/apk/debug/android-debug.apk',
        }
        self.driver = webdriver.Remote('http://192.168.1.207:4723/wd/hub', desired_caps)
        self.driver.save_screenshot(f"results/{sys.argv[1]}-startup.png")

        # with open("../colorado.bin", "rb") as f:
        #     data = base64.b64encode(f.read()).decode('UTF-8')
        #     self.driver.push_file('/sdcard/navit/colorado.bin', data)

        # data = open("colorado.xml", "rb").read()
        # self.driver.push_file('/sdcard/navit/colorado.xml', base64.b64encode(data))
        # data = open("../colorado.bin", "rb").read()
        # self.driver.push_file('/sdcard/navit/colorado.bin', base64.b64encode(data))

    def tearDown(self):
        # end the session
        self.driver.quit()

    def test_find_elements(self):
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Google")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Always")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("OK")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Yes")')
            el.click()
        except Exception as e:
            pass

        self.driver.save_screenshot(f"results/{sys.argv[1]}-home.png")
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("OK")')
            el.click()
        except Exception as e:
            pass
        self.driver.press_keycode(82)
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Download")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Maps containing")')
            el.click()
        except Exception as e:
            pass
        try:
            el = self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("Colorado")')
            el.click()
        except Exception as e:
            pass
        self.driver.save_screenshot(f"results/{sys.argv[1]}-download.png")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleAndroidTests)
    testRunner = HtmlTestRunner.HTMLTestRunner(combine_reports=True, report_name=sys.argv[1], output="results")
    unittest.main(testRunner=testRunner, argv=sys.argv[2:])
