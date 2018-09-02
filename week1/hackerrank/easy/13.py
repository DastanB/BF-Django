def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

print(mutate_string('aaa', 1, 'b'))