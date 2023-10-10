def func(piles: list, h: int) -> int:
    left = 0
    right = max(piles)

    while left <= right:
        k = (left + right) // 2
        total = sum_operation(k,piles)

        if total <= h:
            right = k - 1

        else:
            left = k + 1

    return  left

def sum_operation(k,piles):
    result = 0
    for e in piles:
        result += (k+e-1)//k
    return result

result = ((func([3,6,7,11], 4)))
print("Результат:")
print(result)





