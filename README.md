# 从0开始-Appium自动化

##### 在Windows上进行Android自动化

[Appium](https://github.com/appium/appium)
支持对IOS和Android进行自动化测试，而且可以部署在Windows(仅支持Android)和Mac OS X机器上。他使用Server-Client架构，能够支持Python Java ruby等多种语言来编写自动化脚本。本文详细记录配置Appium环境的方法。

## 在Windows上安装部署

##### 1. 安装[node.js](https://nodejs.org/en/download/)
下载安装后，打开`cmd`，输入`node -v`和`npm -v`验证安装正确。
##### 2. 安装appium-doctor
在打开的`cmd`中输入`npm install -g appium-doctor`，安装appium-doctor，它可以在稍后用来验证Appium的依赖是否配置正确。
##### 3. 安装[JDK](http://www.oracle.com/technetwork/java/javase/downloads/index.html)
下载安装后，在系统环境变量中新建`JAVA_HOME`变量，地址指向JDK的`bin`目录。
##### 4. 安装[Apache Ant](http://ant.apache.org/bindownload.cgi)
下载解压到固定目录下，在系统环境变量中新建`ANT_HOME`变量，地址指向刚才解压的目录，在`PATH`变量下，添加`%ANT_HOME%\bin`，启动`cmd`输入`ant`，提示
```
Buildfile: build.xml does not exist!
Build failed
```
则表示Ant配置正确
##### 5. 安装[Apache Maven](http://maven.apache.org/download.cgi)
下载解压到固定目录下，在系统环境变量中新建`M2HOME`变量，地址指向刚才解压的目录，新建`M2`变量，地址为`%M2HOME%\bin`，在`PATH`变量下，添加`%M2%`，启动`cmd`输入`mvn -v`，会显示Maven的版本，则表示Maven配置正确
##### 6. 安装[Android Studio](https://developer.android.com/studio/index.html)
安装后运行一次，会自动下载更新相应的Android SDK，等待更新完成后，在系统环境变量中新建`ANDROID_HOME`变量，地址指向SDK的目录，添加`tools`和`platform-tools`两个目录到`PATH`变量下。
##### 7. 检测Appium依赖
打开`cmd`，输入`appium-doctor`，会自动检测以上的配置，如果没有异常，则当前已经配置Appium依赖完成。
##### 8. 安装Appium
下载安装即可。
##### 9. 安装[Python3](https://www.python.org/downloads/windows/)
根据操作系统选择32或64位安装包，安装完成后，打开`cmd`，输入`pip install Appium-Python-Client`，安装Appium的Python客户端
##### 10. 备注&疑难问题
目前在Windows平台上，最新的安装包版本是1.4.16，这个版本是15年编译的，而Appium在不停的修复bug，因此使用安装包安装的Appium不包含最新的修复bug。所以推荐使用`npm install -g appium`来安装最新的命令行版本的Appium，并且当版本更新时，可以随之升级，比较方便。
但是使用npm安装需要翻墙，因为在npm下载完成后，安装过程中，还是会从github上下载一些文件，比如appium-selendroid-driver会在安装中下载selendroid-server.jar，如果不翻墙则会下载失败导致不能正确安装
