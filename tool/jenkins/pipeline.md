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