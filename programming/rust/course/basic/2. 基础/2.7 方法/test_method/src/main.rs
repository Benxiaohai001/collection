// 定义方法

// struct Circle {
//     x: f64,
//     y: f64,
//     radius: f64,
// }
// impl Circle {
//     // new是Circle的关联函数，因为他第一个参数不是self，且new不是关键字
//     // 用于初始化结构体实例
//     // 关联函数：与类型相关联的函数，不需要通过实例来调用；构造
//     fn new(x: f64, y: f64, radius: f64) -> Circle {
//         Circle {
//             x: x,
//             y: y,
//             radius: radius,
//         }
//     }
//     fn area(&self) -> f64 {
//         std::f64::consts::PI * (self.radius * self.radius)
//     }
// }
// fn main() {
//     let c = Circle::new(0.0, 0.0, 2.0);
//     println!("area: {}", c.area());
//     println!("Hello, world!");
// }


// 另一个例子
// #[derive(Debug)]
// struct Rectangle {
//     width: u32,
//     height: u32,
// }
// impl Rectangle{
//     fn area(&self) -> u32 {
//         self.width * self.height
//     }
// }
// fn main() {
//     let r = Rectangle {
//         width: 30,
//         height: 50,
//     };
//     println!(
//         "The area of the rectangle is {} square pixels.",
//         r.area()
//     );
// }



// self、&self、&mut self
// &self 等价于 self: &Self
// Self 结构体的类型
// self 此类型的实例，所有权转移到该方法中
// &self 一个指向此类型实例的不可变引用
// &mut self 一个可变引用
// 方法代替函数的好处
    // 不用在函数签名中重复写self对应的类型
    // 代码的组织性和内聚性更强，便于维护和阅读
// 方法名和结构体字段名相同
// struct Rectangle {
//     width: u32,
//     height: u32,
// }
// impl Rectangle {
//     fn width(&self) -> bool {
//         self.width > 0
//     }
// }
// fn main() {
//     let r = Rectangle {
//         width: 30,
//         height: 50,
//     };
//     println!(
//         "The Rectangle has a nonzore width; it is {}",
//         r.width()
//     );
//     println!(
//         "The rectangle's width is {}",
//         // r.width,
//         r.width
//     );
// }


// getter访问器
// 模块化：模块外访问结构体，默认结构体内的字段是私有的
// mod my {
//     pub struct Rectangle {
//         width: u32,
//         pub height: u32,
//     }
//     impl Rectangle {
//         pub fn new(width:  u32, height: u32) -> Rectangle {
//             Rectangle {
//                 width,
//                 height,
//             }
//         }
//         pub fn width(&self) -> u32 {
//             self.width
//         }
//         pub fn height(&self) -> u32 {
//             return self.height;
//         }
//     }
// }
// fn main() {
//     let r = my::Rectangle::new(30, 50);
//     println!("{}", r.width());
//     println!("{}", r.height());
//     println!("{}", r.height);
//     // println!("{}", r.width);
// }
// 自动引用和解引用




// 带有多个参数的方法
// struct Rectangle {
//     width: u32,
//     height: u32,
// }
// impl Rectangle {
//     fn area(&self) -> u32 {
//         self.width * self.height
//     }
//     fn can_hold(&self, other: &Rectangle) -> bool {
//         self.width > other.width && self.height > other.height
//     }
// }
// fn main() {
//     let rec1 = Rectangle { width: 30, height: 50 };
//     let rec2 = Rectangle { width: 10, height: 40 };
//     let rec3 = Rectangle { width: 60, height: 45 };

//     println!("Cac rec1 hold rec2? {}", rec1.can_hold(&rec2));
//     println!("Cac rec1 hold rec3? {}", rec1.can_hold(&rec3));
// }


// 关联函数
// 参数不包含self
// 定义在ipml块中，且没有self参数的函数叫做关联函数
// struct Rectangle {
//     width: u32,
//     height: u32,
// }
// impl Rectangle {
//     fn new(width: u32, height:u32) -> Rectangle {
//         Rectangle {
//             width,
//             height,
//         }
//     }
// }
// 不能用.调用关联函数，只能用::调用关联函数




// 多个impl定义
// struct Rectangle {
//     width: u32,
//     height: u32,
// }
// impl Rectangle {
//     fn area(&self) -> u32 {
//         self.width * self.height
//     }
// }
// impl Rectangle {
//     fn can_hold(&self, other: &Rectangle) -> bool {
//         self.width > other.width && self.height > other.height
//     }
// }



// 为枚举实现方法
// #![] 是一种属性，可以用于整个crete、模块、函数、或者其它代码，通常放在文件顶部用于整个文件
// #![allow(unused)]
// enum Message {
//     Quit,
//     Move {x: i32, y: i32},
//     Write(String),
//     ChangeColor(i32, i32, i32),
// }
// impl Message {
//     fn call(&self) {
//         // 方法体
//     }
// }
// fn main() {
//     let m = Message::Write(String::from("hello"));
//     m.call();
// }






// 练习
// 语法糖：一种语法；使代码更已读或者更简洁。但不增加语法功能
// 字段初始化简写
// struct Point {
//     x: i32,
//     y: i32,
// }
// fn main() {
//     let x = 5;
//     let y = 10;
//     let p = Point { x, y }; // 等同于 Point { x: x, y: y }
// }
// 模式匹配中的if let和while let
// let some_option = Some(5);
// // if let
// if let Some(x) = some_option {
//     println!("Matched: {}", x);
// }
// // while let
// let mut stack = vec![1, 2, 3];
// while let Some(top) = stack.pop() {
//     println!("{}", top);
// }
// // 如果不用语法糖，都需要用match进行匹配，上面的代码会变成这样：
// let some_option = Some(5);
// // 使用 match 代替 if let
// match some_option {
//     Some(x) => println!("Matched: {}", x),
//     None => {},
// }
// // 使用 match 代替 while let
// let mut stack = vec![1, 2, 3];
// loop {
//     match stack.pop() {
//         Some(top) => println!("{}", top),
//         None => break,
//     }
// }
// 方法调用的自动引用和解引用
// struct Circle {
//     radius: f64,
// }
// impl Circle {
//     fn area(&self) -> f64 {
//         std::f64::consts::PI * self.radius * self.radius
//     }
// }
// fn main() {
//     let circle = Circle { radius: 5.0 };
//     println!("Area: {}", circle.area()); // 自动引用
//     // println!("Area: {}", Circle::area(&circle)); // 显式传递引用
// }
// 闭包的简写
// let add = |a, b| a + b; // 等同于 |a: i32, b: i32| -> i32 { a + b }
// println!("Sum: {}", add(2, 3));
// 1.
// struct Rectangle {
//     width: u32,
//     height: u32,
// }
// impl Rectangle {
//     fn area(&self) -> u32 {
//         self.width * self.height
//     }
// }
// fn main() {
//     let rect1 = Rectangle { width: 30, height: 50 };
//     assert_eq!(rect1.area(), 1500);
// }

// 2. 
// #[derive(Debug)]
// struct TrafficLight {
//     color: String,
// }
// impl TrafficLight {
//     pub fn show_state(&self) {
//         println!("the current state is: {}", &self.color);
//     }
// }
// fn main() {
//     let light = TrafficLight {
//         color: "red".to_owned(),
//     };
//     light.show_state();
//     println!("{:?}", light);
// }

// 3.
// struct TrafficLight {
//     color: String,
// }
// impl TrafficLight {
//     pub fn show_state(&self) {
//         println!("the current state is: {}", self.color);
//     }
//     pub fn change_state(& mut self) {
//         self.color = "green".to_string();
//     }
// }
// fn main() {}

// 4.
// #![]和#[]区别
// #![]crate级别属性
// #[]项级别属性
// #[derive(Debug)]
// struct TrafficLight {
//     color: String,
// }
// impl TrafficLight {
//     pub fn new() -> TrafficLight {
//         TrafficLight {
//             color: "red".to_string(),
//         }
//     }
//     pub fn get_status(&self) -> &str {
//         &self.color
//     }
// }
// fn main() {
//     let light = TrafficLight::new();
//     assert_eq!(light.get_status(), "red");
// }

// 5.
struct Rectangle {
    width: u32,
    height: u32,
}
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}
impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}
fn main() {}