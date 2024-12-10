// 如果没有泛型
// fn add_i8(a: i8, b: i8) -> i8 {
//     a + b
// }
// fn add_i32(a: i32, b: i32) -> i32 {
//     a + b
// }
// fn add_f64(a: f64, b: f64) -> f64 {
//     a + b
// }
// fn main() {
//     println!("add i8: {}", add_i8(1i8, 2i8));
//     println!("add i32: {}", add_i32(1, 2));
//     println!("add f64: {}", add_f64(1.0, 2.0));
//     println!("Hello, world!");
// }
// 多态
// fn add<T: std::ops::Add<Output = T>>(a: T, b: T) -> T {
//     a + b
// }
// fn main() {
//     println!("add i8: {}", add(1i8, 2i8));
//     println!("add i32: {}", add(1, 2));
//     println!("add f64: {}", add(1.0, 2.0));
//     println!("Hello, world!");
// }



// 泛型参数
// std::cmp::PartialOrd // 用于比较的特性
// &[T] 数组切片引用
// fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T{
//     let mut largest = &list[0];
//     for item in list.iter() {
//         if item > largest {
//             largest = item;
//         }
//     }
//     largest
// }
// fn main() {
//     let number = vec![34, 50, 25, 100, 65];
//     let result = largest(&number);
//     println!("The largest number is {}", result);
//     let char_list = vec!['y', 'm', 'a', 'q'];
//     let result = largest(&char_list);
//     println!("The largest char is {}", result);
// }
// fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> T {
//     let mut largest = list[0];

//     for &item in list.iter() {
//         if item > largest {
//             largest = item;
//         }
//     }

//     largest
// }

// fn main() {
//     let number_list = vec![34, 50, 25, 100, 65];

//     let result = largest(&number_list);
//     println!("The largest number is {}", result);

//     let char_list = vec!['y', 'm', 'a', 'q'];

//     let result = largest(&char_list);
//     println!("The largest char is {}", result);
// }


// 显式的指定泛型类型参数
use std::fmt::Display;
// where 子句，声明函数需要实现后续的trait
// From(U) trait，用于将U类型转换为T类型
fn create_and_print<T>() where T: From<i32> + Display {
    // into()是into trait的一个方法，用于将i32转换为T类型
    // 如果类型T实现了From(U) trait，那么U类型自动实现INTO(T) trait
    let a: T = 100.into();
    println!("a is {}", a);
}
fn main() {
    // create_and_print::<i32>();
    // 调用的实收可以显示的指定参数类型
    create_and_print::<i64>();
}