use std::io::{self,BufRead};

fn main(){
    let mut t = String::new();
    io::stdin().read_line(& mut t).unwrap();
    let t:i32 = t.trim().parse().unwrap();

    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    for _ in 0..t{
        let v:Vec<i32> = lines.next().unwrap().unwrap().split(' ').map(|x| x.trim().parse().unwrap()).collect();
        let n = v[0];
        let k = v[1];

        let c:Vec<char> = lines.next().unwrap().unwrap().to_string().chars().collect();

        let mut iterator = c.iter().map(|x| x.to_digit(10).unwrap());
        let mut v  = vec![];
        let mut ans:i32 = 0;
        for _ in 0..k{
            let x = iterator.clone();
            v.push(x);
            iterator.next().unwrap();
        }


        for _ in 0..n-k+1{
            let  p = v.iter_mut().fold(1, |acc, x| acc * x.next().unwrap());
            ans = std::cmp::max(ans,p as i32);
        }
        println!("{}",ans )


    }
}