def max_sub_array(nums):
    mc = nums[0]
    mt = nums[0]
    for i in nums[1:]:
        mc = i if mc < 0 else i + mc
        mt = max(mc, mt)
    return mt