use std::io::{self,BufRead};


fn is_palindrome(x:u64)->bool{
	let s:String =  x.to_string();
	let reverse_s:String = s.chars().rev().collect();
	
	s==reverse_s
}

fn precompute()-> Vec<u64>{
	let mut v:Vec<u64> = Vec::new();
	
	for i in 100..1000{
		for j in i..1000{
			let num = i * j;
			match is_palindrome(num){
				true => v.push(num),
				false => continue,
			}
			
		}
	}
	
	v.sort();
	v.dedup();
	v
}



fn main(){
	let mut input = String::new();
	io::stdin().read_line(& mut input).unwrap();
	let t:i32 = input.trim().parse().unwrap();
	
	let v = precompute();
	
	let stdin = io::stdin();
	let mut iterator = stdin.lock().lines();
	
	for _i in 0..t{
		let n:u64 = iterator.next().unwrap().unwrap().trim().parse().unwrap();
		match v.binary_search(&n){
			Ok(idx) => println!("{}",v[idx-1]),
			Err(idx) => println!("{}",v[idx-1]),
		}
	}
}