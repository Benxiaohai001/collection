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
mod my {
    pub struct Rectangle {
        width: u32,
        pub height: u32,
    }
    impl Rectangle {
        pub fn new(width:  u32, height: u32) -> Rectangle {
            Rectangle {
                width,
                height,
            }
        }
        pub fn width(&self) -> u32 {
            self.width
        }
        pub fn height(&self) -> u32 {
            return self.height;
        }
    }
}
fn main() {
    let r = my::Rectangle::new(30, 50);
    println!("{}", r.width());
    println!("{}", r.height());
    println!("{}", r.height);
    // println!("{}", r.width);
}
// 自动引用和解引用