# pipeline
## trigger
### 插件
#### Jenkins ​​Generic Webhook Trigger
GenericTrigger
genericVariables: 从http请求中获取配置项。
genericHeaderVariables：从http请求头获取参数的核心配置。
## agent
## stages
## options
0815cc32a7b81a9887a03ed1e636ceafde59a342

environment 中定义的变量具有全局优先；在后续的stage中重新赋值不会覆盖；
# 两个stage之间传递变量，怎么传递到shell中
```jenkins
pipeline {
    agent: any
    stages {
        stage {
            step {
                script {
                    env.para = 1
                    // 可以使用env. 修改为全局变量，可以跨stage传递
                }
            }
        }
        stage {
            step {
                script {
                    echo "env.para: {env.para}"
                    // 这里将会输出上一个stage的变量赋值
                    // script 中嵌入的sh脚本,前后两个是独立的
                    sh```#! /bin/bash
                    echo $para
                    // 这里可以正常输出我们在流水线中定义的变量
                    export VAR = 1
                    ```
                    sh```#! /bin/bash
                    echo $VAR
                    ```
                }
            }
        }
    }
}
```
# script 中嵌入的sh脚本,前后两个是独立的
```jenkins
pipeline {
    agent: any
    stages {
        stage {
            step {
                script {
                    // script 中嵌入的sh脚本,前后两个是独立的
                    sh```#! /bin/bash
                    export VAR = 1
                    ```
                    sh```#! /bin/bash
                    echo $VAR
                    // 这里无法输出上一个shell中定义的变量，因为两个shell之间彼此是完全独立的。
                    ```
                }
            }
        }
    }
}
```


# 类型
## 声明式
## 脚本式
## 区别
|特性纬度|声明式（Declarative Pipeline）|脚本式（Scripted Pipeline）|
|---|---|---|
|设计哲学|声明式：|命令式|
|语法结构|结构严谨|结构自由|
|学习难度|较低|较高|
|错误处理|内置更健壮的错误处理和恢复机制|错误处理依赖于groovy异常处理机制|
|灵活性|相对较低|极高|
|官方推荐|推荐|早期支持流水线方式，目前复杂场景依旧是首选|
