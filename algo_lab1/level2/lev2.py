def func(k, mas: list):
    if k > len(mas):
        print("такого елемемнта не існує")
    else:
        while (k != 1):
            counter = 0
            for element in mas:
                if element == max(mas):
                    mas[counter] = 0
                    break
                counter += 1
            k -= 1

        max_value = max(mas)
        counter = 0
        for elem in mas:
            if elem == max_value:
                return counter
            counter += 1


k = 1
mas = [0, 15, 7, 22, 9, 36, 2, 42, 18, 88]
result = func(k, mas)
if result is not None:
    print("Знайдений",k,"-й найбільший елемент:",mas[result],".Позиція",k,"-го найбільшого елемента в масиві:",result)


# [5,6,3,2,8] 2