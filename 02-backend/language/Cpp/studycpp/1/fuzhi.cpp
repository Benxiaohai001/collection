#include <iostream>
int main() {
    int width;
    width = 5;
    std::cout << width << std::endl;
    width = 7;
    std::cout << width << std::endl;

    int a;          // 默认初始化
    int b = 5;      // 拷贝初始化
    int c(6);       // 直接初始化

    // 列表初始化
    int d {7};      // 直接列表初始化
    int e = {8};    // 拷贝列表初始化
    int f{};        // 值列表初始化
    // 零初始化
    // 实际使用初始化的值，则显示设置初始化值
    int x {0};  // 列表初始化为0
    std::cout << x;
    // 如果值在使用前被替换，使用值初始化
    int y {};
    std::cin >> y;
    std::cout << "x = " << x; 

    return 0;
}