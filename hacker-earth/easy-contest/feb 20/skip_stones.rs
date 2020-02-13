//https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/practice-problems/algorithm/jump-k-forward-250d464b/

use std::io;
use std::cmp::max;

fn main(){
    const MODULO:i64 = 10e9 as i64 +7;
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let vec:Vec<i64> = input.trim().split(' ').map(|x| x.parse().unwrap()).collect();
    let (n,k) = (vec[0],vec[1]);
    let mut dp:Vec<i128> = vec![0; 1e4 as usize + 17];
    dp[0] +=1;
    for i in 1..n{
        for j in max(0,i-k)..i{
            dp[i as usize] +=dp[j as usize];
            dp[i as usize] %= MODULO
        }
    }
    let n = n as usize;
    println!("{}",dp[n-1]);
}