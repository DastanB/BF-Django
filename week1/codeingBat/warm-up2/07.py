def array_front9(nums):
    
    lens = len(nums)
    if lens > 4:
        lens = 4
    
    for i in range(lens):  
        if nums[i] == 9:
            return True
    return False