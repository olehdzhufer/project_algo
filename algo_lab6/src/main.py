def search_string(haystack, needle):
    array = []
    counter1 = 0
    counter2 = 0
    for char in haystack:
        for symbol in needle:
            if char == symbol:
                counter2 += 1
                if counter2 == len(needle):
                    array.append(counter1)
                    counter2 = 0
            if char not in needle:
                counter2 = 0
        counter1 += 1
    if len(array) == 0:
        return -1
    if len(needle) == 0:
        return -1
    else:
        return array[-1]



haystack = 'abcabd'
needle = 'xyz'
result = search_string(haystack, needle)
print(result)
