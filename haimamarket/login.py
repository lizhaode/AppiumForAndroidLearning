from appium import webdriver as wd
import time

dc = {
    'platformName':'Android',
    'platformVersion':'5.1',
    'deviceName':'MESUIT i6P',
    'appPackage':'me.haima.androidassist',
    'appActivity':'.InitializeLoadActivity'
}

wbdriver = wd.Remote('http://127.0.0.1:4723/wd/hub',dc)
wbdriver.wait_activity('.MainActivity',100)

# managerbutton = wbdriver.find_element_by_id('nb_manager')
# managerbutton.click()
# loginbutton = wbdriver.find_element_by_id('login_btn')
# loginbutton.click()

# useridbutton = wbdriver.find_element_by_android_uiautomator('.className("android.widget.EditText").instance(0)')
# useridbutton.send_keys('lizhaotest')
# passwordbutton = wbdriver.find_element_by_android_uiautomator('.className("android.widget.EditText").instance(1)')
# passwordbutton.send_keys('123456')




wbdriver.quit()