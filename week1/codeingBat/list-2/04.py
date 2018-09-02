def sum13(nums):    
    sum = 0
    for i in range (len(nums)):
        if nums[i] != 13:
            sum += nums[i]
        elif nums[i] == 13 and i < len(nums)-1:
            nums[i]=0;
            nums[i+1] =0
            
    return sum 