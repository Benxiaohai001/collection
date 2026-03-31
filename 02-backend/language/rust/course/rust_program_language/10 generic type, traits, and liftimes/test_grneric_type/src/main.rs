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



// 参数不相同的声明
// struct Point<X1, Y1> {
//     x: X1,
//     y: Y1,
// }
// impl<X1, Y1> Point<X1, Y1> {
//     fn mixup<X2, Y2>(self, other: Point<X2, Y2>) -> Point<X1, Y2> {
//         Point {
//             x: self.x,
//             y: other.y,
//         }
//     }
// }
// fn main() {
//     let p1 = Point {x: 5, y: 10.4};
//     let p2 = Point {x: "Hellp", y: 'c'};
//     let p3 = p1.mixup(p2);
//     println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
// }


// 使用泛型的代码性能
// 单态化
// enum Option_i32 {
//     Some(i32),
//     None,
// }
// enum Option_f64 {
//     Some(f64),
//     None,
// }
enum Option<T> {
    Some(T),
    None,
}
fn main() {
    // let integer = Option_i32::Some(5);
    // let float = Option_f64::Some(5.0);
    let integer = Option::Some(5);
    let float = Option::Some(5.0);
}