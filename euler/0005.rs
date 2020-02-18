use std::io;

fn gcd(x:i128,y:i128)-> i128{
    if x > y{
        return gcd(y,x)
    }

    if x == 0{
        return y
    }

    gcd(y%x,x)
}

fn lcm(x:i128, y:i128) -> i128{
    (x * y)/gcd(x,y)
}




fn solve(n:i32){
    if n == 1{
        println!("{}",1);
    }

    else if n == 2{
        println!("{}", 2);
    }

    else{
        let mut ans:i128 = 2;

        for i in 3..n+1{
            ans = lcm(ans,i as i128);
        }

        println!("{}",ans);
    }
}


fn main(){
    let mut input = String::new();
    io::stdin().read_line(& mut input).unwrap();
    let t:i32 = input.trim().parse().unwrap();

    for _ in 0..t{
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let n:i32 = input.trim().parse().unwrap();
        solve(n);
    }

}