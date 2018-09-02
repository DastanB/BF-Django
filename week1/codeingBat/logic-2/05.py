def round10(num):
    digit = num % 10
    if digit >= 5:
        return num + (10 - digit)
    return num - digit

def round_sum(a, b, c):
    return round10(a) + round10(b) + round10(c)