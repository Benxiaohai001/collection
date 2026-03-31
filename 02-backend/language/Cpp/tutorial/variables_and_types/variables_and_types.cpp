#include <iostream>
#include <string>

using namespace std;

int main() {
    // int a, b;
    // int result;
    
    // a = 5;
    // b = 2;
    // a = a + 1;
    // result = a - b;
    // cout << result;
    // initialization
    // int a = 5;
    // int b(3);
    // int c{2}; // c++11 及以上版本支持这种初始化方式；列表初始化
    // int result;
    // cout << "a:" << a << "b:" << b << /*"c:" << c << */ endl;
    // 自动初始化
    // int foo = 5;
    // auto bar = foo;
    // cout << "bar: " << bar << endl;
    // decltype
    // int foo = 5;
    // decltype(foo) bar;
    // cout << "bar: " << bar << endl; // 这里的输出为什么不是5呢？
    string mystring;
    mystring = "This is the initial string content";
    string mystring2("This is the initial string content");
    string mystring3{"This is the initial string content"};
    mystring = "This is a different string content";
    cout << "mystring:" << mystring << "\nmystring2" << mystring2 << "\nmystring3" << mystring3<< endl;
    return 0;
}