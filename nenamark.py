from appium import webdriver as wd
import time

dc = {
    'platformName':'Android',
    'platformVersion':'5.1',
    'deviceName':'i60a',
    'appPackage':'se.nena.nenamark2',
    'appActivity':'se.nena.nenamark2.NenaMark2'
}

wbdriver = wd.Remote('http://127.0.0.1:4723/wd/hub',dc)
time.sleep(2)
# action = TouchAction(wbdriver)
wbdriver.tap([(266,261)])
time.sleep(50)
result = wbdriver.find_element_by_id('finished_details')
try:
    f = open('score.txt',mode='a+')
    timetxt = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    writetxt = timetxt + '测试结果: ' + result.text + '\n'
    f.write(writetxt)
finally:
    f.close()
wbdriver.quit()
