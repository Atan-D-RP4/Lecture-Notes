impl Solution {
    #[inline]
    pub fn max_sub_array(nums: Vec<i32>) -> i32 {
        let mut mc = nums[0];
        let mut mt = nums[0];
        for i in nums.iter().skip(1) {
            mc = if mc < 0 { *i } else { *i + mc };
            mt = mc.max(mt);
        }
        mt
    }
}