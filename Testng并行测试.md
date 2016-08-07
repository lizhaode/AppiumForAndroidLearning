#使用TestNG进行多手机并行测试
经过测试，成功在一台电脑上同时进行两个手机进行并行测试，相关问题记录下来
##前提条件
java的TestNG单元框架支持通过配置文件进行脚本并行运行，此次在Windows系统上，安装GUI的Appium进行并行的实验
##配置步骤
####1. 脚本准备
* 使用IDEA新建工程，选择maven下的maven-archetype-quickstart模版创建一个工程
* 等待相关组件下载添加完毕后，打开pom.xml文件，在dependencies标签中添加
```xml
<dependency>
     <groupId>io.appium</groupId>
     <artifactId>java-client</artifactId>
     <version>4.1.0</version>
   </dependency>
```
来添加Appium的java client及其所需依赖
* 等待完成后，打开src --> main --> java -->groupId名 下边的.java文件
* 光标定位到主类上，敲击Alt + Enter 选择creat test
* 在弹出的窗口中，Testing library下选择TestNG，然后会提示`TestNG library not found in the module`，点击fix即可自动添加TestNG依赖到pom.xml中
* 其他的选项根据实际情况配置即可，重复以上步骤可以添加多个测试脚本
####2. 并行测试配置
* 脚本准备完成后，在项目中新建testng.xml文件
