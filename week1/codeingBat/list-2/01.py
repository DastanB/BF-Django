def count_evens(nums):
    counter = 0
    for i in range (len(nums)):
        if nums[i] % 2 == 0:
            counter += 1
    return counter