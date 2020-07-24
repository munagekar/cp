// https://leetcode.com/problems/integer-to-roman/
// It Would have been a better idea to use a dictionary based lookup instead of the long function
impl Solution {
    pub fn int_to_roman(mut num: i32) -> String {
        let mut a = String::new();
        let ms = num / 1000;
        num = num % 1000;
        let mut ds = num / 500;
        num = num % 500;
        let mut cs = num / 100;
        num = num % 100;
        let mut ls = num / 50;
        num = num % 50;
        let mut xs = num / 10;
        num = num % 10;
        let mut vs = num /5;
        num = num % 5;
        let mut is = num;
        
        for i in 0..ms{
            a.push('M');
        }
        
        if ds ==1 && cs==4{
            a.push_str("CM");
            ds -= 1;
            cs -=4;
        }
        
        for i in  0..ds{
            a.push('D');
        }
        
        if cs==4{
            a.push_str("CD");
            cs -=4;
        }
        
        for i in 0..cs{
            a.push('C');
        }
        
        if ls ==1 && xs==4{
            a.push_str("XC");
            ls -=1;
            xs -=4;
        }
        
        for i in 0..ls{
            a.push('L');
        }
        
        if xs==4{
            a.push_str("XL");
            xs -=4;
        }
        
        for i in 0..xs{
            a.push('X');
        }
        
        if vs==1 && is==4{
            a.push_str("IX");
            vs -=1;
            is -=4;
        }
        
        if vs==1{
            a.push_str("V");
        }
        
        if is==4{
            a.push_str("IV");
            is -=4;
        }
        
        for i in 0..is{
            a.push('I');
        }
        
        a
        
    }
}