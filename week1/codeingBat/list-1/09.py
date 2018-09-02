def sum2(nums):
    if len(nums) < 3:
        s = 0
        for num in nums:
          s += num
        return s
    else:
        s = 0
        for i in range(2):
          s += nums[i]
        return s