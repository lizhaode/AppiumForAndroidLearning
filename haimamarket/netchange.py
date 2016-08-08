from appium import webdriver as wd
import subprocess
import time

dc = {
    'platformName':'Android',
    'platformVersion':'5.1',
    'deviceName':'MESUIT i6P',
    'appPackage':'com.android.contacts',
    'appActivity':'.activities.PeopleActivity'
}

wbdriver = wd.Remote('http://127.0.0.1:4723/wd/hub',dc)
# wbdriver.wait_activity('.MainActivity',100)

# if wbdriver.network_connection() != 6:
#     wbdriver.set_network_connection(6)
# time.sleep(2)
# downbutton = wbdriver.find_element_by_id('downPointsText')
# downbutton.click()

# wbdriver.set_network_connection(4)
# time.sleep(2)

wbdriver.find_element_by_id('com.android.contacts:id/floating_action_button').click()
subprocess.check_output('adb shell input keyevent 4',shell=True)
phone = wbdriver.find_elements_by_name('电话')
phone[1].click()
time.sleep(10)
wbdriver.quit()