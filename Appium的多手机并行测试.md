# 使用TestNG进行多手机并行测试

启动多个Appium Server，可以连接多台手机，这样就可以进行多用例并行测试

## 前提条件

经过查询，Java的junit框架对并行测试支持不好，而java的TestNG单元框架多并行测试支持较好，并且可以通过配置文件进行各种细粒度的并行。

此次试验，环境搭建在Windows系统上，安装GUI的Appium

## 配置步骤

#### 脚本准备

* 使用IDEA新建工程，选择maven下的maven-archetype-quickstart模版创建一个工程

* 等待相关组件下载添加完毕后，打开pom.xml文件，在dependencies标签中添加以下内容：

```xml
<dependency>
     <groupId>io.appium</groupId>
     <artifactId>java-client</artifactId>
     <version>4.1.0</version>
   </dependency>
```

他可以自动下载、添加Appium的java client及其所需依赖

* 等待完成后，打开src --> main --> java -->groupId名 下边的.java文件

* 光标定位到主类上，敲击Alt + Enter 选择creat test

* 在弹出的窗口中，Testing library下选择TestNG，然后会提示***TestNG library not found in the module***，点击fix即可自动添加TestNG依赖到pom.xml中

* 其他的选项根据实际情况配置即可，重复以上步骤再次添加一个测试脚本

* 编辑这两个测试脚本，让其能正常运行

#### testng配置
* 脚本准备完成后，在项目中新建testng.xml文件（与pom.xml文件同级目录），输入内容如下：

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE suite SYSTEM "http://testng.org/testng-1.0.dtd">
<suite name="Default Suite" parallel="classes" thread-count="2">
    <test name="testapp">
        <classes>
            <class name="com.lizhao.appiumtest"/>
            <class name="com.lizhao.appiumtest1"/>
        </classes>
    </test> 
</suite> 
```

* 对上述xml文件的解释如下：
  * `name` 标签随便填写，不会影响实际运行
  * `parallel` 标签代表了并行的细粒度，可以填写***methods***,***tests***,***classes***,***instaances***,具体解释见链接 [parallel](http://testng.org/doc/documentation-main.html#parallel-running)
  * `thread-count` 标签代表了线程数量

#### Appium Server设置

* 经过测试，启动两个GUI Appium Server，会发生错误，原因是GUI的Appium只能设置DeviceName，不能设置UDID，而在Appium Server接收到连接请求时，都会执行`adb devices`命令，检测到设备存在后，去连接命令返回的第一个设备，只有启动Appium Server时，指定UDID，才会根据UDID去连接设备

* 因此，首先启动一个GUI Appium ，在Android Settings中，设置Bootstrap Port，要保证设置的端口没有被占用，如果不手动设置Bootstrap Port，两个Appium Server在创建连接时，都会去连接相同的Bootstrap Port

* 然后使用命令行启动Appium Server。在Appium安装目录下的 **node_modules\\.bin**目录下，存在编译好的命令行启动程序，使用cmd打开，并注意仿照GUI Appium的log中给的参数，进行设置。`port`参数不要与GUI的重复，`Bootstrap-Port`参数同样不要重复，最后加上`-U`参数，参数值给`adb devices`命令返回的列表中第二个值

* 两个Appium Server启动成功后，就可以在IDEA中，右击testng.xml文件，选择run即可并发执行两个用例脚本