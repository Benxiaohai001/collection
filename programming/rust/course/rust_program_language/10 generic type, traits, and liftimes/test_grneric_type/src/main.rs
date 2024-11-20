// 寻找一个列表中的最大值10.1
// fn main() {
//     let number_list = vec![34, 50, 25, 100, 65];
//     let mut largest = number_list[0];
//     for number in number_list {
//         if number > largest {
//             largest = number;
//         }
//     }
//     println!("The largest number is {}", largest);
//     println!("Hello, world!");
// }
// 两个列表，分别找出其中的最大值。
// 

// 使用函数的方式

// fn largest(list: &[i32]) -> &i32 {
//     let mut largest = &list[0];
//     for number in list {
//         if number > largest {
//             largest = number;
//         }
//     }
//     largest
// }
// fn main() {
//     let number_list = vec![34, 50, 25, 100, 65];
//     let result = largest(&number_list);
//     println!("The largest number is {}", result);
//     let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];
//     let result = largest(&number_list);
//     println!("The largest number is {}", result);
//     println!("Hello, world!");
// }

// 使用泛型的方式
// fn largest<T: std::cmp::PartialOrd>(list: &[T]) -> &T {
//     let mut largest = &list[0];

//     for number in list {
//         if number > largest {
//             largest = number;
//         }
//     }
//     largest
// }

// fn main() {
//     let number_list = vec![23, 45, 87,45, 100, 23];
//     let result = largest(&number_list);
//     println!("The largest number is {}", result);

//     let char_list = vec!['y', 'm', 'a', 'q'];
//     let result = largest(&char_list);
//     println!("The largest char is {}", result);
// }

// 结构体中定义
// struct Point<T> {
//     x: T,
//     y: T,
// }
// struct Point1<T, U> {
//     x: T,
//     y: U,
// }

// fn main() {
//     let integer = Point {x: 5, y: 10};
//     let float = Point {x: 1.0, y: 4.0};
//     println!("integer.x = {}", integer.x);
//     println!("float.x = {}", float.x);
//     println!("integer.y = {}", integer.y);
//     println!("float.y = {}", float.y);
//     // let p = Point {x: 4, y: 6.0};
//     let p1 = Point1 {x: 4, y: 6.0};
//     println!("p1.x = {}", p1.x);
//     println!("p1.y = {}", p1.y);

// }

// 枚举中定义
// enum Option<T> {
//     Some(T),
//     None,
// }
// enum Result<T, E> {
//     Ok(T),
//     Err(E),
// }

// 在方法定义中
// struct Point<T> {
//     x: T,
//     y: T,
// }
// impl<T> Point<T> {
//     fn x(&self) -> &T {
//         &self.x
//     }
// }
// // 在对泛型进行一定的约束，实现某些方法
// impl Point<f64> {
//     fn distance_from_origin(&self) -> f64 {
//         (self.x.powf(2.0) + self.y.powf(2.0)).sqrt()
//     }
// }
// fn main() {
//     let p = Point {x: 5, y: 10};
//     println!("p.x = {}", p.x());
// }

