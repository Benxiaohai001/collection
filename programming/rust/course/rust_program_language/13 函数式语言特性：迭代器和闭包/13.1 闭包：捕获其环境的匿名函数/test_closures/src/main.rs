// 匿名函数
// 使用闭包捕获环境
#derive(Debug, PartialEq, Copy, Clone)
enum ShirtColor {
    Red,
    Blue,
}
struct Inventory {
    shirts: Vec<ShirtColor>,
}
impl Inventory {
    fn giveaway(&self, user_perference: Option<ShirtColor>) -> ShirtColor {
        user_perference.unwrap_or_else(||self.most_stocked())
    }
    fn most_stocked(&self) -> {
        let mut num_red = 0;
        let mut num_blue = 0;
        for color in &self.shirts {
            match color {
                ShirtColor::Red => num_red += 1,
                ShirtColor::Blue => num_blue += 1,
            }
        }
        if num_red > num_blue {
            ShirtColor::Red
        } else {
            ShirtColor::Blue
        }
    }
}
fn main() {
    println!("Hello, world!");
}
