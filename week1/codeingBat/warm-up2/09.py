def string_match(a, b):
    
    shortest = min(len(a), len(b))
    count = 0
    
    for i in range(shortest-1):
        a_sub = a[i:i+2]
        b_sub = b[i:i+2]
        if a_sub == b_sub:
            count = count + 1

    return count