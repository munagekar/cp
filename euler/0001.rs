use std::io::{self, BufRead};

fn sum_ap(ft: i128, lt: i128, nt: i128) -> i128 {
    (ft + lt) * nt / 2
}

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: i64 = input.trim().parse().unwrap();

    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();

    for _i in 0..n {
        let num: i128 = iterator.next().unwrap().unwrap().trim().parse().unwrap();
        let num = num - 1;
        let last_3 = num - num % 3;
        let last_5 = num - num % 5;
        let tot_3 = (last_3 - 3) / 3 + 1;
        let tot_5 = (last_5 - 5) / 5 + 1;
        let last_15 = num - num % 15;
        let tot_15 = (last_15 - 15) / 15 + 1;

        let a3 = sum_ap(3, last_3, tot_3);
        let a5 = sum_ap(5, last_5, tot_5);
        let a15 = sum_ap(15, last_15, tot_15);
        let ans = a3 + a5 - a15;

        println!("{}", ans);
    }
}
