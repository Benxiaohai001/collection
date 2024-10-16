// assignment operator
#include <iostream>
using namespace std;

int main()
{
    // int a, b;
    // a = 10;
    // b = 4;
    // a= b;
    // b = 7;

    // cout << "a:" << a << endl;
    // cout << "b:" << b << endl;
    // compound assignment operator
    // int a, b = 10;
    // a = b;
    // a += 2;
    // cout << "a:" << a << endl;
    // 自增/自减运算符
    int a, b = 10;
    a = b++;
    cout << "a:" << a << endl;
    cout << "b:" << b << endl;
    int c, d = 10;
    c = ++d;
    cout << "c:" << c << endl;
    cout << "d:" << d << endl;
}