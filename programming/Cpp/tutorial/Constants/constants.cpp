// # include <iostream>

// using namespace std;

// const double pi = 3.1415926;
// const char newline = '\n';

// int main() {
//     double r = 5.0;
//     double circle;

//     circle = 2 * pi * r;
//     cout << circle;
//     cout << newline;
// }


// 预处理定义
#include <iostream>
using namespace std;

#define PI 3.1415926
#define NEWLINE '\n'

int main() {
    double r = 5.0;
    double circle;

    circle = 2 * PI * r;
    cout << circle;
    cout << NEWLINE;
}