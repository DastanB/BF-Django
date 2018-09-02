def count_substring(string, sub_string):
    count = 0
    index = 0
    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            r = i+len(sub_string)
            if string[i:r] == sub_string:
                count += 1

    return count