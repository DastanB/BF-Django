def count_hi(str):
    s = 0
    for i in range (len(str)-1):
        if str[i] == 'h' and str[i+1] == 'i':
            s += 1
    return s
