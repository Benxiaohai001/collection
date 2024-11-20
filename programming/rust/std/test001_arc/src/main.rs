use std::sync::Arc;
use std::thread;

fn main() {
    let value = Arc::new(42);
    let handles: Vec<_> = (0..10).map(|_| {
        let value = Arc::clone(&value);
        thread::spawn(move || {
            println!("{}", value);
        })
    }).collect();
    for handle in handles {
        handle.join().unwrap();
    }
    println!("Hello, world!");
}
