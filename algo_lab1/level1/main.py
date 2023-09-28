def func(input_array: list):
    squared_numbers = [number ** 2 for number in input_array]
    for i in range(len(squared_numbers)):
        minimum = i
        for j in range(i + 1, len(squared_numbers)):
            if squared_numbers[j] < squared_numbers[minimum]:
                minimum = j
        squared_numbers[minimum], squared_numbers[i] = squared_numbers[i], squared_numbers[minimum]
    return squared_numbers
input_array = [1, 7, 4, 10, 9, -2]
result = func(input_array)
print(result)







