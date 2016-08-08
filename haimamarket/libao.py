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

libaobutton = wbdriver.find_element_by_id('libao_img')
libaobutton.click()
qiangbutton = wbdriver.find_element_by_id('qiangBtn')
for i in range(10):
    qiangbutton.click()
    time.sleep(1)
    qiangbutton.click()
    okbutton = wbdriver.find_element_by_id('okBtn')
    okbutton.click()

time.sleep(1)
qiangbutton.click()
errtext = wbdriver.find_element_by_id('code_text')
if errtext.text == '抢包失败':
    print('防止抢礼包成功')
    qiangbutton.click()
else:
    print('防止抢礼包失败')

wbdriver.quit()