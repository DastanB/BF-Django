def swap_case(s):
    string = ""
    for x in s:
        if x.isupper(): string = string + x.lower()
        else: string = string + x.upper()
    return string