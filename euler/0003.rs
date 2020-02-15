use std::io::{self,BufRead};
use std::cmp;


fn largest_prime_factor(x:i128)-> i128{
	
	let mut y =x;
	let mut i:i128 = 2;
	let mut largest_prime = 2;
	
	while i <= (y as f64).sqrt() as i128 +1 {
		
		if y%i == 0{
			largest_prime = cmp::max(i,largest_prime);
			while y%i == 0{
				y/=i;
			}
		}
		i+=1;
	}
	
	cmp::max(y, largest_prime)

	}
	
fn main(){
	let mut test_cases = String::new();
	io::stdin().read_line(&mut test_cases).unwrap();
	let test_cases:i32 = test_cases.trim().parse().unwrap();
	
	let stdin = io::stdin();
	let mut iterator = stdin.lock().lines();
	
	for _i in 0..test_cases{
		let num:i128 = iterator.next().unwrap().unwrap().trim().parse().unwrap();
		println!("{}",largest_prime_factor(num));
	}
	    
	
}