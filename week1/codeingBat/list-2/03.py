def centered_average(nums):
    sum = 0
    total = len(nums)-2
    largest = nums.index(max(nums))     
    smallest = nums.index(min(nums))    
    if largest == smallest:             
        for i in range(len(nums)):      
            if nums[i] == nums[smallest]:
                largest = i             
    for i in range(len(nums)):
        if i != largest and i != smallest:      
            sum = sum + nums[i] 
    if total > 0:
        return sum / total         
    else:
        return sum 