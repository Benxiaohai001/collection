# 将maven源改为国内阿里云镜像
修改～/.ssh/settings.xml(没有这个文件可以手动创建) \
```
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
                      http://maven.apache.org/xsd/settings-1.0.0.xsd">
  <localRepository/>
  <interactiveMode/>
  <usePluginRegistry/>
  <offline/>
  <pluginGroups/>
  <servers/>
  <mirrors>
    <mirror>
     <id>aliyunmaven</id>
     <mirrorOf>central</mirrorOf>
     <name>阿里云公共仓库</name>
     <url>https://maven.aliyun.com/repository/central</url>
    </mirror>
    <mirror>
      <id>repo1</id>
      <mirrorOf>central</mirrorOf>
      <name>central repo</name>
      <url>http://repo1.maven.org/maven2/</url>
    </mirror>
    <mirror>
     <id>aliyunmaven</id>
     <mirrorOf>apache snapshots</mirrorOf>
     <name>阿里云阿帕奇仓库</name>
     <url>https://maven.aliyun.com/repository/apache-snapshots</url>
    </mirror>
  </mirrors>
  <proxies/>
  <activeProfiles/>
  <profiles>
    <profile>  
        <repositories>
           <repository>
                <id>aliyunmaven</id>
                <name>aliyunmaven</name>
                <url>https://maven.aliyun.com/repository/public</url>
                <layout>default</layout>
                <releases>
                        <enabled>true</enabled>
                </releases>
                <snapshots>
                        <enabled>true</enabled>
                </snapshots>
            </repository>
            <repository>
                <id>MavenCentral</id>
                <url>http://repo1.maven.org/maven2/</url>
            </repository>
            <repository>
                <id>aliyunmavenApache</id>
                <url>https://maven.aliyun.com/repository/apache-snapshots</url>
            </repository>
        </repositories>             
     </profile>
  </profiles>
</settings>
```

# 主要的目录结构
 ```java
 my-project/
|-- pom.xml  # 配置文件
`-- src
    |-- main  # 项目主要代码和资源文件
    |   |-- java # java源代码
    |   |   `-- com 
    |   |       `-- example
    |   |           `-- myproject
    |   |               `-- MyApp.java
    |   |-- resources # 项目的资源文件
    |   |   `-- myconfig.xml
    |   `-- webapp # web应用程序的静态文件
    |       |-- WEB-INF
    |       |   `-- web.xml
    |       `-- index.jsp
    `-- test # 测试代码和资源文件
        |-- java
        |   `-- com
        |       `-- example
        |           `-- myproject
        |               `-- MyAppTest.java
        `-- resources
            `-- testconfig.xml
 ```
 # 子命令
mvn package # 编译当前项目 \
mvn clean \
compile # 编译成class 文件
# 插件 plugin
## exec maven plugin
exec:exec # 单独程序中执行程序和java程序 \
exec:java # 在同一个虚拟机中执行java程序

# vscode 配置
```json
{
    "java.configuration.updateBuildConfiguration": "interactive",
    "java.classPath": ["target/classes", "target/test-classes", "/Users/bichaoxue/Library/Java/Extensions", "/Library/Java/Extensions", "/Network/Library/Java/Extensions", "/System/Library/Java/Extensions", "/usr/lib/java", "."],
    "java.Testclass": ["target/classes", "target/test-classes", "/Users/bichaoxue/Library/Java/Extensions", "/Library/Java/Extensions", "/Network/Library/Java/Extensions", "/System/Library/Java/Extensions", "/usr/lib/java", "."],
    // "java.testMethod": ["test/java/com/mycompany/app/AppTest.java"],
    "java.testMethod": ["mvn", "test", "-Dtest=${class}#${method}"]
}
```