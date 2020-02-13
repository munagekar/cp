// https://www.hackerearth.com/problem/algorithm/large-average-51cfb031/
use std::io::{self, BufRead};

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let n: i32 = input.trim().parse().unwrap();
    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();
    for _x in 0..n {
        let line = iterator.next().unwrap().unwrap();
        let v: Vec<i64>=line.split(" ").map(|x| x.trim().parse().unwrap()).collect();
        let (x,y) = (v[0],v[1]);
        println!("{}",(x + y)/2);
    }
}
