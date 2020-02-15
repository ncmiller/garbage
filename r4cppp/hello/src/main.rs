fn foo(_x: &'static str) -> &'static str {
    "world"
}

fn main() {
    println!("Hello, {}!", foo("bar"));
}
