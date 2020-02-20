use std::io::{self,BufRead};


fn precompute() -> Vec<i128>{
    let n = (15000 as f64) * (15000 as f64).ln();
    let n = n as usize;
    let mut v:Vec<i128> = vec![1;n];
    let mut primes: Vec<i128> = vec![0];    //Off by 1
    for i in 2..n{
        if v[i] == 0{
            continue;
        }
        primes.push(i as i128);
        let mut z = 2 * i;
        while z < n{
            v[z] = 0; 
            z += i;
        }
    }
    primes
}




fn main(){
    let mut t = String::new();
    io::stdin().read_line(& mut t).unwrap();
    let t:i32 = t.trim().parse().unwrap();

    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();


    let v:Vec<i128> = precompute();
    for _ in 0..t{
        let n:usize= iterator.next().unwrap().unwrap().trim().parse().unwrap();
        println!("{}",v[n])    
    
    }
    
    
    
}