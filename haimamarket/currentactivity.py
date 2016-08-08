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

softbutton = wbdriver.find_element_by_id('nb_ranking')
softbutton.click()
downbutton = wbdriver.find_element_by_id('downPointsText')
downbutton.click()
downnum = wbdriver.find_element_by_id('down_num')
downnum.click()
loading_text = wbdriver.find_element_by_id('loading_text')
downnumbutton = wbdriver.find_element_by_id('downPointsText')
while wbdriver.current_activity == ('.mdcontent.usermanager.down.UserDownActivity'):
    print('下载进度：',loading_text.text,end='\r')
    time.sleep(5)



wbdriver.quit()