use std::cmp;
impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut left:usize = 0;
        let mut right = height.len() - 1;
        
        let mut area = 0;
        while left <right{
            let cur_area = cmp::min(height[left],height[right]) * (right -left) as i32;
            area = cmp::max(area,cur_area);
            
            if height[left]< height[right]{
                left +=1;
            }
            else{
                right -=1;
            }
        }
        area
    }
}