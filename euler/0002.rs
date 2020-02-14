use std::io::{self, BufRead};


fn cal(max:i128) -> i128 {
    let mut first: i128 = 1;
    let mut second: i128 = 2;
    let mut sum: i128 = 2;
    loop {
        first = first + second;

        // Breaking condition
        if first > max  {
            break;
        }

        // Regular Update
        if first % 2 == 0 {
            sum = sum + first;

        }

        // Swap
        std::mem::swap(&mut first, &mut second);
    }

    sum
}


fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let t: i64 = input.trim().parse().unwrap();


    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();

    for _ in 0..t {
        let line = iterator.next().unwrap().unwrap();
        let n: i128 = line.trim().parse().unwrap();
        println!("{}",cal(n));
    }
}