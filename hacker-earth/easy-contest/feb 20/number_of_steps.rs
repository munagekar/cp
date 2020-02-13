

    //https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/make-all-equal-90a21ab2/description/

    use std::io;

    fn main() {
        let mut input = String::new();
        io::stdin().read_line(&mut input).unwrap();
        let mut n: usize = input.trim().parse().unwrap();

        let mut line1 = String::new();
        io::stdin().read_line(&mut line1).unwrap();
        let a: Vec<i32> = line1.trim().split(' ').map(|x| x.parse().unwrap()).collect();

        let mut line2 = String::new();
        io::stdin().read_line(&mut line2).unwrap();
        let b: Vec<i32> = line2.trim().split(' ').map(|x| x.parse().unwrap()).collect();

        let smallest_a: i32 = *a.iter().min().unwrap();

        let mut flag: bool = true;
        for small in (0..smallest_a + 1).rev() {
            flag = true;
            let mut ans = 0;
            let mut i: usize = 0;

            while &mut i < &mut n {
                if a[i] == small {
                    i += 1;
                    continue;
                }

                if small % b[i] != a[i] % b[i] {
                    flag = false;
                    break;
                } else {
                    ans += (a[i] - small) / b[i]
                }
                i += 1;
            }

            if flag {
                println!("{}", ans);
                break;
            }
        }
        if !flag {
            println!("{}", -1);
        }
    }

