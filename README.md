# project_algo
# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"
## Виконав: Джуфер Олег Віталійович (Група ІР-24)
### Лабораторна робота №1 (Варіант 3 Рівень 2)

'''Напишіть функцію для пошуку k-того найбільшого елемента в заданому масиві цілих чисел. Параметр k задається на вхід функції і визначає порядковий номер найбільшого елемента, який потрібно знайти. Наприклад, якщо k = 1, програма повинна знайти найбільший елемент в масиві. Якщо k = 2, програма повинна знайти другий за величиною елемент, і так далі.
​
Умови задачі:
​
- Масив цілих чисел передається у вашу функцію.
- Розмір масиву повинен бути не менше k.
- Програма повинна вивести k-тий найбільший елемент і його позицію (індекс) в масиві.
​
Приклад введення та виведення результату:
​
Вхідний масив: [15, 7, 22, 9, 36, 2, 42, 18] Задане k: 3 Знайдений 3-й найбільший елемент: 22 Позиція 3-го найбільшого елемента в масиві: 2
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` .'''

# project_algo
# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"
## Виконав: Джуфер Олег Віталійович (Група ІР-24)
### Лабораторна робота №2 (Варіант 3 Рівень 2)

Горила Джекі  із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами, у і-тому кошику є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід зоопарку на Н годин, протягом якого Джекі може поласувати своєю улюбленою стравою.
​
Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти. Якщо кошик має менше, ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години.
​
Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться.
​
Напишвть функцію, яка повертає мінімальне ціле число К, яке дозволить Джекі з'їсти всі банани на складі протягом Н годин, поки повернеться охорона.
​
Приклад 1:
piles = `[3,6,7,11]`, 
H = 8  
Результат: 
4  
​
Приклад 2:
piles = `[30,11,23,4,20]`,
H = 5  
Результат: 
30  
  
Приклад 3:
piles = `[30,11,23,4,20]`,
H = 6  
Результат: 
23
​
Важливо:
1 <= piles.length <= 10^4
piles.length <= H <= 10^9
1 <= `piles[i]` <= 10^9
​
Для перевірки виконання роботи реалізованого алгоритму слід використати бібліотеку `unittest` та перевірити роботу вашої функції на прикладах, наведених вище

# project_algo
# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"
## Виконав: Джуфер Олег Віталійович (Група ІР-24)
### Лабораторна робота №3 (Варіант 3 Рівень 2)

Напишіть функцію, яка виконає операцію інвертування (перевернення) бінарного дерева таким чином, щоб лівий дочірній вузол став правим, а правий дочірній вузол став лівим.

Нехай у вас задане бінарне дерево такого вигляду:
    1
   / \
  2   3
 / \ / \
4  5 6  7

Ваша функція має повернути дерево, яке виглядатиме наступним чином:
    1
   / \
  3   2
 / \ / \
7  6 5  4

Клас, який описує бінарне дерево (та будь який вузол дерева) має вигляд:

This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None
Ваша функція має мати такий вигляд:

def invert_binary_tree(tree) -> BinaryTree:
Реалізація даної задачі не вимагає написання коду вставки чи виділення елементів з бінарного дерева. У тесті ви можете створити достатню кількість елементів класу BinaryTree наступним чином:

root = BinaryTree(3)
root.left = BinaryTree(9)
root.right = BinaryTree(20)
Ваша функція має повернути об'єкт класу  BinaryTree. Для спрощення тестування даної функції достатньо реалізувати порівняння значень вузлів дерева

# project_algo
# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"
## Виконав: Джуфер Олег Віталійович (Група ІР-24)
### Лабораторна робота №4 (Варіант 2 Рівень 2)

Коренева вершина орієнтованого графа — це вершина u з орієнтованим шляхом від u до v для кожної пари вершин (u, v) у графі. Іншими словами, всі інші вершини в графі можна досягнути з кореневої вершини (Рис. 2)

Граф може мати кілька кореневих вершин. Наприклад, кожна вершина графу може бути мати зв’язки з іншими (Рис.1). У таких випадках ваш код має повернути будь-яку із них. Якщо граф не має кореневих вершин, код має повернути -1.


Рис.1 Граф який містить компоненту сильної звязаності

Коренева вершина дорівнює 4, оскільки вона має шлях до кожної іншої вершини в наступному графі:

Для представлення графу слід використати список суміжності, який зчитується з файлу input.txt
Результат слід вивести у файл output.txt

# project_algo
# Лабораторні роботи з дисципліни "Алгоритмів і структур даних"
## Виконав: Джуфер Олег Віталійович (Група ІР-24)
### Лабораторна робота №5 (Варіант 3 Рівень 2)

Весілля та племена

Вождь Ваі-Ву з острова Пасхи вирішив поміняти традиції одруження на острові.

Раніше усі одружувались всередині свого племені.  Але після курсу біології на Coursera 
Ваі-Ву дізнався, що змішування генів - це корисна штука.  Тому він попросив усіх голів племен підготувати списки молодих хлопців/дівчат, і спробує організувати шлюби між племенами.

Вашим завдання буде проаналізувати списки, та сказати Ваі-Ву скільки можливих пар з різних племен він може скласти.

Формат списків племен:
Кожен юнак/дівчина - це ціле число
Юнаки - непарні числа, дівчата - парні
У кожному рядку - два числа, які означають що юнак чи дівчина належать до одного племені.  Наприклад:
	
		1 2
		2 4
		3 5

	Описує два племені - в одному є хлопець 1 та двоє дівчат 2 та 4, а в іншому племені - двоє хлопців 3 та 5.

Вхідні дані:
	Перший рядок містить кількість пар N
	Наступні N рядків містять пари людей з різних племен

Вихідні дані:
	Кількість можливих комбінацій пар таких, що хлопець і дівчина походять з різних племен.

Обмеження:
	0 < N < 10000
Приклади:
In:
3
1 2
	2 4
	3 5
Out:
	4 (Можливі пари - 2/3, 2/5, 4/3, 4/5)

In:
5
1 2
	2 4
	1 3
	3 5
	8 10
Out:
	6 (Можливі пари - 1/8, 1/10,  3/8, 3/10,  5/8, 5/10)
