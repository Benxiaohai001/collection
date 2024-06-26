fn main() {
    let input = "COUNT(UInt8(1))\n0\n";
    let zero_str = input.split('\n').nth(1).unwrap();
    println!("{}", zero_str); // 输出: 0
    println!("Hello, world!");
    panic!("This is a test panic!");
}
