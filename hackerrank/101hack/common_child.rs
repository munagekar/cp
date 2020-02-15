//https://www.hackerrank.com/contests/101hack/challenges/common-child/problem

use std::io;
use std::cmp;

fn main(){
	let mut first = String::new();
	io::stdin().read_line(&mut first).unwrap();
	let first:String = first.trim().to_string();
	
	let mut second = String::new();
	io::stdin().read_line(&mut second).unwrap();
	let second:String = second.trim().to_string();
	
	let mut dp = vec![vec![0; second.len()+1]; first.len()+1];
	
	let first:Vec<char> = first.chars().collect();
	let second:Vec<char> = second.chars().collect();
	
	for i in 1..first.len()+1{
		for j in 1..second.len()+1{
			let index_i = i - 1;
			let index_j = j - 1;
			
			let mut ans11= dp[i-1][j-1];
			
			if first[index_i] == second[index_j]{
				ans11 = ans11 + 1;
			}
			
			dp[i][j] = cmp::max(ans11, dp[i-1][j]);
			dp[i][j] = cmp::max(dp[i][j-1],dp[i][j]);
		}
	}
	
	println!("{}",dp[first.len()][second.len()]);
	
}