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
// use std::fmt::Display;
// // where 子句，声明函数需要实现后续的trait
// // From(U) trait，用于将U类型转换为T类型
// fn create_and_print<T>() where T: From<i32> + Display {
//     // into()是into trait的一个方法，用于将i32转换为T类型
//     // 如果类型T实现了From(U) trait，那么U类型自动实现INTO(T) trait
//     let a: T = 100.into();
//     println!("a is {}", a);
// }
// fn main() {
//     // create_and_print::<i32>();
//     // 调用的实收可以显示的指定参数类型
//     create_and_print::<i64>();
// }




// 结构体中使用泛型
// 提前声明
// #[warn(dead_code)]
// struct Point<T> {
//     // x和y都是泛型类型T，两种类型必须相同
//     #[warn(dead_code)]
//     x: T,
//     #[warn(dead_code)]
//     y: T,
// }

// fn main() {
//     let _integer = Point { x: 5, y: 10 };
//     let _float = Point { x: 1.0, y: 4.0 };
//     // let _diff = Point { x: 1, y: 4.0 };
// }
// 两个值不同
// struct Point<T, U> {
//     x: T,
//     y: U,
// }
// fn main() {
//     let _both_integer = Point { x: 5, y: 10 };
//     let _both_float = Point { x: 1.0, y: 4.0 };
//     let _integer_and_float = Point { x: 5, y: 4.0 };
// }







// 枚举中实现泛型
// enum Option<T> {
//     Some(T),
//     None,
// }
// enum Result<T, E> {
//     Ok(T),
//     Err(E),
// }




// 方法中使用泛型
// struct Point<T> {
//     x: T,
//     y: T,
// }
// impl<T> Point<T> {
//     fn x(&self) -> &T {
//         &self.x
//     }
// }
// fn main() {
//     let p = Point {x: 5, y: 10};
//     println!("p.x = {}", p.x());
// }
// 结构体泛型
// struct Point<T, U> {
//     x: T,
//     y: U,
// }
// impl<T, U> Point<T, U> {
//     // 函数泛型
//     fn mixup<V, W>(self, other: Point<V, W>) -> Point<T, W> {
//         Point {
//             x: self.x,
//             y: other.y,
//         }
//     }
// }
// fn main() {
//     let p1 = Point {x: 5, y: 20.4};
//     let p2 = Point {x: "Hello", y: 'c'};
//     let p3 = p1.mixup(p2);
//     println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
// }






// 为具体的泛型实现方法
// struct Point<T> {
//     x: T,
//     y: T,
// }
// impl Point<f32> {
//     fn distance_from_origin(&self) -> f32 {
//         (self.x.powi(2) + self.y.powi(2)).sqrt()
//     }
// }



// const 泛型（rust 1,51）
fn display_array(arr: &[i32; 3]) {
    println!("{:?}", arr);
}
fn main() {
    let arr: [i32; 3] = [1, 2, 3]
}