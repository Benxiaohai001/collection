// 函数指针
// 一种类型而不是特征
// fn add_one(x: i32) -> i32 {
//     x + 1
// }
// fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
//     f(arg) + f(arg)
// }
// fn main() {
//     let answer = do_twice(add_one, 5);
//     println!("The answer is: {}", answer);
//     println!("Hello, world!");
// }
// 将数字向量转变成字符串向量
// fn main() {
//     let list_of_numbers = vec![1, 2, 3];
//     // let list_of_strings: Vec<String> = list_of_numbers.iter().map(|i| i.to_string()).collect();
//     // 完全限定语法
//     // let list_of_strings: Vec<String> = list_of_numbers.iter().map(ToString::to_string).collect();
//     // println!("{:?}", list_of_strings);
//     // 每一个枚举变量的名称也称为一个初始化函数
//     #[derive(Debug)]
//     enum Status {
//         Value(u32),
//         Stop,
//     }
//     let list_of_statuses: Vec<Status> = (0u32..20).map(Status::Value).collect();
//     println!("{:?}", list_of_statuses);
// }


// 返回闭包
// 动态分发的特征对象 dyn
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    // 智能指针
    Box::new(|x| x + 1)
}