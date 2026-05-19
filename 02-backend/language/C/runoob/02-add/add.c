#include <stdio.h>
/*
系统头文件使用<>,自定义头文件使用""
例如：#include <stdio.h> #include "myhaeder.h"
*/

#define PI 3.14159 // 宏定义
/*
1. 符号常量或代码片段，预处理阶段进行文本替换，不占用运行时内存
2. 没有类型检查
3. 示例：#define PI 3.14159、#define MAX(a, b) ((a) > (b) ? (a) : (b))
*/
int add(int a, int b);
/*
函数声明
1. 必须在调用或者定义之前。包括函数名，返回类型，参数列表；
2. 声明可以放在头文件，供多个源文件共享。
*/

int main() {
    /*
    主函数
    1. 返回值通常0表示成功，非零表示失败；
    2. main函数可以接受命令行参数
    */
    int num1, num2, sum;
    /*
    变量
    1. 必须使用前声明；局部&全局
    2. 声明的同时可以进行初始化。不初始化可能会包含垃圾值。全局和静态变量会自动初始化为0.
    */
    // printf("%d %d %d", num1, num2, sum);
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);

    sum = add(num1, num2);
    printf("Sum: %d\n", sum);

    return 0;
}

int add(int a, int b) {
    return a + b;
}