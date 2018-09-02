def near_ten(num):
    mod = num % 10
    if mod >= 8 or mod <= 2:
        return True
    return False
