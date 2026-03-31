use hello::HelloMacro;
use hello_macro_derive::HelloMacro;

#[derive(HelloMacro)]
struct Sunfei;

#[derive(HelloMacro)]
struct Sunfei2;

fn main() {
    // println!("Hello, world!");
    // let v = vec![1, 2, 3];
    // println!("{:?}", v);
    Sunfei::hello_macro();
    Sunfei2::hello_macro();
}

// #[macro_export]
// macro_rules! vec {
//     ( $( $x:expr), *) => (
//         {
//             let mut temp_vec = Vec::new();
//             $(
//                 temp_vec.push($x);
//             )*
//             temp_vec
//         }
//     ) ;
// }
