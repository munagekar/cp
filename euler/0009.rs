use std::io::{self,BufRead};

fn main(){
    let mut t = String::new();
    io::stdin().read_line(& mut t).unwrap();
    let t:u32 = t.trim().parse().unwrap();

    let stdin = io::stdin();
    let mut iterator = stdin.lock().lines();

    for _ in 0..t{
        let n:u32 = iterator.next().unwrap().unwrap().trim().parse().unwrap();
        if n %2 == 1{
            println!("{}",-1 );
            continue;
        }

        let mut ans:u128 = 0;
        for a in 0..n/3{
            let num = n * n - 2 * a * n;
            let deno = 2 * (n-a);
            let b = num as f64 / deno as f64;
            if b.fract() != 0.0{
                continue;
            }
            let c = (b).hypot(a as f64);
            if c.fract() != 0.0{
                continue;
            }
            let prod = (a as f64) * b * c;
            ans = std::cmp::max(prod as u128, ans);
        }

        if ans <= 0{
            println!("{}",-1);
            continue;
        }
        println!("{}",ans);

    }
}