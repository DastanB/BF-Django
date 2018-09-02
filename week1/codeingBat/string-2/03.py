def cat_dog(str):
    c = 0
    d = 0
    for i in range (len(str)-2):
        if str[i] == 'c':
            if str[i+1] == 'a' and str[i+2] == 't':
                c += 1
        elif str[i] == 'd':
            if str[i+1] == 'o' and str[i+2] == 'g':
                d += 1

    if c == d: return True  
    return False

