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
if downnum.text == '1':
    downnum.click()
else:
    print('当前存在其他下载！')
    wbdriver.quit()
loading_text = wbdriver.find_element_by_id('loading_text')
downnumbutton = wbdriver.find_element_by_id('downPointsText')
if wbdriver.wait_activity('.PackageInstallerActivity',100):
    time.sleep(3)
    oriscrollbutton = wbdriver.find_element_by_android_uiautomator('.className("android.widget.TextView").text("添加或移除帐户")')
    desscrollbutton = wbdriver.find_element_by_android_uiautomator('.className("android.widget.TextView").text("读取手机状态和身份")')
    wbdriver.scroll(oriscrollbutton,desscrollbutton)
    installbutton = wbdriver.find_element_by_android_uiautomator('.className("android.widget.Button").resourceId("com.android.packageinstaller:id/ok_button")')
    installbutton.click()
if wbdriver.current_activity == '.mdcontent.usermanager.down.UserDownActivity' and downnumbutton.text == '暂停':
    print('正在下载，进度： ',loading_text.text)
    if wbdriver.wait_activity('.PackageInstallerActivity',100):
        installbutton = wbdriver.find_element_by_android_uiautomator('.className("android.widget.Button").resourceId("com.android.packageinstaller:id/ok_button")')
        installbutton.click()
    elif wbdriver.current_activity == '.mdcontent.usermanager.down.UserDownActivity' and downnumbutton.text == '暂停':
        print('下载速度过慢，或下载文件过大')
        wbdriver.quit()
        
if wbdriver.current_activity == '.mdcontent.usermanager.down.UserDownActivity' and (downnumbutton.text == '继续' or downnumbutton.text == '重试'):
    print('下载出错')
    wbdriver.quit()
# while wbdriver.current_activity == '.mdcontent.usermanager.down.UserDownActivity':
#     if downnumbutton.text == '暂停':
#         print('正在下载，进度： ',loading_text.text,'\r',end='')
#     else:
#         break
#     if downnumbutton.text == '继续' or downnumbutton.text == '重试':
#         print('下载出错')
#         wbdriver.quit()
if wbdriver.wait_activity('.InstallAppProgress',100):
    time.sleep(20)
    finishbuttom = wbdriver.find_element_by_android_uiautomator('.className("android.widget.Button").resourceId("com.android.packageinstaller:id/done_button")')
    finishbuttom.click()
else:
    print('安装时间过长或安装失败')
if wbdriver.wait_activity('.mdcontent.usermanager.down.UserDownActivity',100):
    openbutton = wbdriver.find_element_by_id('tv_item_app_list_download')
    if openbutton.text != '打开':
        print('安装失败')
    else:
        print('安装成功')
else:
    print('安装时间过长或安装失败')
wbdriver.quit()