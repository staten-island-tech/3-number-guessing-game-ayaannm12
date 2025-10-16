def count(line, letter):
    ret = 0
    for char in line:
        if char == letter:
            ret += 1
    return ret


def language(line):
    t = count(line, 't') +  count(line, "T")
    s = count(line, 's') +  count(line, 'S')
    if t > s:
        return "English"
    elif s > t:
        return "french we we"
    elif s == t:
        return"Its a 50/50 chance"
print(language("tommytuffknuckles"))
    


   