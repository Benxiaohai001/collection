#include <stdio.h>
int add(int a, int b); // 函数的声明；告诉编译器，有该函数定义，在别处，别报错

/*
test1.c, test2.c 两个源文件，
.venv) ➜  01-hello git:(main) ✗ gcc ./test1.c ./test2.c -o test
(.venv) ➜  01-hello git:(main) ✗ ./test 
结果是：4 
编译器将两个组成一个可执行文件
*/

int main() {
    int res = add(1, 3);

    printf("结果是：%d \n", res); // %d 转义字符 占位符 表示整数
    return 0;
}