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
    // int a, b = 10;
    // a = b++;
    // cout << "a:" << a << endl;
    // cout << "b:" << b << endl;
    // int c, d = 10;
    // c = ++d;
    // cout << "c:" << c << endl;
    // cout << "d:" << d << endl;

    // 关系元素安抚和比较运算符
    cout << (5 > 3) << endl;
    cout << (5 < 3) << endl;
    cout << (5 >= 3) << endl;
    cout << (5 <= 3) << endl;
    cout << (5 == 3) << endl;
    cout << (5 != 3) << endl;

    int a = 5;
    int b = 3;
    int c = 7;
    cout << (a > b) << endl;
    cout << (a < b) << endl;
    cout << (a >= b) << endl;
    cout << (a <= b) << endl;
    cout << (a == b) << endl;
    cout << (a != b) << endl;
    cout << (a > b && a < c) << endl;
    cout << (a == 5) << endl;
    cout << (a == 3) << endl;
    cout << (a*b > c)  << endl;
    cout << (a*b < c)  << endl;
    cout << ((b = 2) < 10) << endl;
    return 0;
}