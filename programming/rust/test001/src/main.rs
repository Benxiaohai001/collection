fn main() {
    // let input = "COUNT(UInt8(1))\n0\n";
    // let zero_str = input.split('\n').nth(1).unwrap();
    // println!("{}", zero_str); // 输出: 0
    // println!("Hello, world!");
    // panic!("This is a test panic!");


    // unwrap() 方法
    // let un: Result<u32, String> = Ok(32);
    // assert_eq!(un.unwrap(), 32);
    let un2: Result<u32, String> = Err("error".to_string());
    assert_eq!(un2.unwrap(), 32);
    for i in 0..10 {
        do_something().unwrap();
        // println!("{}", i);
    }
}

fn do_something() {}
