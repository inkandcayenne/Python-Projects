# 1. Напишите программу, которая будет запрашивать на вход числа (через запятую на одной строке) и выводить наибольшее
# значение из списка.
numbers = list(input('введите значения').split(', '))
numbers_1 = list(map(int, numbers))

number = 0
number2 = 1

while number2 < len(numbers_1):
    if numbers_1[number] >= numbers_1[number2]:
        number_max = numbers_1[number]
    else:
        number_max = numbers_1[number2]
    number += 1
    number2 += 1
print(number_max)

# 2 Напишите программу, которая будет запрашивать на вход числа (каждое с новой строки) до тех пор, пока не будет
# введен ноль (0). На выход должно выводиться второе по величине значение.

my_list = []
element = 1

while element != 0:
    element = int(input('введите число'))
    my_list.append(element)

print(my_list)

largest, second_largest = my_list[0], my_list[0]
for number in my_list:
    if number > largest:
        second_largest = largest
        largest = number
    elif number > second_largest and number < largest:
        second_largest = number
print(second_largest)

# 3. Напишите программу, которая принимает на вход год, а на выход выдает количество дней в этом году.
year = int(input('введите год: '))
if year % 400 != 0 and year % 100 == 0:
    print(365)
elif year % 4 == 0:
    print(366)
else:
    print(365)

# 4 Напишите программу, которая на вход получает координаты двух клеток шахматной доски и выводит соощение о том,
# являются ли эти клетки одного цвета.

koord1 = list(input('введите координаты первой клетки через пробел ').split(' '))
koord2 = list(input('введите координаты второй клетки через пробел ').split(' '))
koord1_new = list(map(int, koord1))
koord2_new = list(map(int, koord2))

if (koord1_new[0] + koord1_new[1]) % 2 == (koord2_new[0] + koord2_new[1]) % 2:
    print('эти клетки одного цвета')
else:
    print('клетки разного цвета')

# 5 Напишите программу, которая на вход получает число, а на выходе сообщает, простое это число или составное.
number = int(input('введите число: '))

denominator = number - 1

while denominator > 1:
    if number % denominator == 0:
        print('составное')
        break
    denominator -= 1
else:
    print('простое')

# 6 Напишите программу, которая на вход получает целое число больше 2 и выводит по нему его наименьший натуральный
# делитель, отличный от 1.
whole_number = int(input('введите целое число: '))

denominator = 2

while whole_number % denominator != 0:
    denominator += 1
print(denominator)

# 7 Напишите программу, которая поможет составить план тренировок для подготовки к марафону. Она получает на вход
# число километров на планируемом марафоне, сколько пользователь планирует пробежать в первый день тренировок и на
# сколько процентов планирует увеличивать каждый день это расстояние. На выходе программа должна выдавать,
# сколько дней пользователю потребуется для того, чтобы подготовиться пробежать целевое количество километров.

km = int(input('количество километров в марафоне: '))
km_start = int(input('сколько километров вы планируете пробежать в первый день: '))
km_percent = int(input('на сколько процентов вы увеличите нагрузку каждый день: '))
km_new = km_start
days = 0
while km_new <= km:
    km_new = km_new + km_new * km_percent / 100
    days += 1
print(days)

# 8 Напишите программу, которая на вход получает число n и считает по нему сумму 1²+2²+3²+...+n².
number = int(input('введите число'))
i = 0
summa = 0
while i <= number:
    summa = summa + i ** 2
    i += 1
print(summa)

# 9 Напишите программу, которая на вход получает число n и считает по нему сумму сумму 1! + 2! + 3! + ... + n!
number = int(input('введите число'))
i = 1
summa = 0
factorial = 1
while i <= number:
    factorial = factorial * i
    summa = summa + factorial
    i += 1
print(summa)

# 10 Напишите программу, которая получает на вход последовательность чисел (каждое число с новой строки до того
# момента, пока пользователь не введет 0) и считает количество четных элементов в последовательности.
my_list = []
element = 1

while element != 0:
    element = int(input('введите число'))
    my_list.append(element)
print(my_list)

i = 0
for number in my_list:
    if number % 2 == 0 and number != 0:
        i += 1
print(i)

# 11 Напишите программу, которая формирует список игроков женской команды по футболу.
# Программа должна записывать возраст и пол претендента. Возраст должен запрашиваться после пола и только
# в том случае, если пол претендента женский. Если пол претендента мужской, программа должна сообщать о том,
# что он не подходит. Возраст претенденток должен быть от 18 до 35 лет.
# Если кандидат удовлетворяет требованиям, должно появляться соответствующее сообщение.
pol = str(input('введите пол претендента, м/ж:'))
if pol == 'ж':
    vozrast = int(input('введите возраст претендентки:'))
    if 18 <= vozrast <= 35:
        print('претендент подходит')
    else:
        print('претендент не подходит по возрасту')
else:
    print('претендент не подходит, мужской пол')

# 12 Напишите программу, которая на вход получает максимальную ширину ромба и рисует его.
# Пример вывода для числа 5:
# ```
#   *
#  ***
# *****
#  ***
#   *```

width = int(input('максимальная ширина ромба:'))
if width % 2 == 0:
    i = 2
else:
    i = 1

while i <= width:
    print(' ' * ((width - i) // 2), '*' * i)
    i += 2

i = width - 2
while i > 0:
    print(' ' * ((width - i) // 2), '*' * i)
    i -= 2


# 13 Напишите программу, которая запрашивает у пользователя сторону квадрата и символ, а затем рисует этот символ
# по диагоналям квадрата.
# Пример вывода для числа 5:
# ```
#
# #   #
#  # #
#   #
#  # #
# #   #

height = int(input('сторона квадрата:'))
symbol = str(input('введите символ'))
i = 0
j = (height-2)
while 0 < j <= (height):
    print(' '*i, symbol, ' '*j, symbol, sep = "")
#     print(i, j)
    i += 1
    j -= 2

if height%2 ==0:
#     print(i, j)
    print(' '*i, symbol*2, sep = "")
else:
#     print(i,j)
    print(' '*i, symbol, sep = "")

if height%2 == 0:
    i = height//2-2
    j = 2
else:
    i = height//2-1
    j = 1
# print(i, j)
while j <= height-1:
    print(' '*i, symbol, ' '*j, symbol, sep = "")
    i -= 1
    j += 2

# 14 В корзине лежат шары. Если раскладывать их группами по 2, 3, 4, 5, 6, в корзине остается один шар.
# Если разложить по 7 шаров, то в корзине не останется ничего.
# Какое минимальное количество шаров находится в корзине?
denominator = 2
spheres_number = 1

while denominator < 7:
    if spheres_number%denominator == 1 and spheres_number//denominator >= 1 and spheres_number%7 == 0:
        denominator += 1
        spheres_number += 0
    else:
        spheres_number += 1
        denominator = 2
print(spheres_number)


# 15 Рабочие клеили обои на стены. Первую стену поклеили за M минут, а каждую следующую на 5 минут больше, чем предыдущую.
#  Напишите программу, которая запрашивает сколько стен было в квартире под поклейку, а также время работы с первой стеной.
#  Программа должна выводить, сколько часов рабочие потратили на поклейку обоев во всей квартире.

steny = int(input('количество стен под поклейку'))
M = int(input('время на первую стену, мин'))
M = M/60

i = steny
sum = 0
while 0 < i <= steny:
    sum = sum + M
    M = M*(1+5/60)
    i -= 1
print(sum)

# 16 Напишите программу, которая убирает из списка повторяющиеся элементы.
# Программа должна запрашивать на вход слова, каждое с новой строки, пока пользователь не введет пустую строку.
# Затем должна выводить список без повторяющихся элементов.

my_list = []
element = 1

while element != '':
    element = str(input('введите слово'))
    if element in my_list:
        pass
    else:
        my_list.append(element)
my_list.remove('')
print(my_list)

# 17 Напишите программу, которая выводит число пар одинаковых элементов в списке.
# Программа должна запрашивать на вход слова, каждое с новой строки, пока пользователь не введет пустую строку.
my_list = []
element = 1
i = 0
while element != '':
    element = str(input('введите слово'))
    if element in my_list:
        my_list.append(element)
        i += 1
    else:
        my_list.append(element)
print(i)

# 18 Будем считать, что кубик может иметь неограниченное количество граней (натуральное число).
# Напишите программу, которая запрашивает, сколько граней имеется у двух разных кубиков.
# Затем выводит все возможные комбинации результатов бросков двух таких кубиков.
gran = int(input('грань кубиков: '))
kub1 = list(range(1, gran+1))
kub2 = list(range(1, gran+1))
for i in kub1:
    for j in kub2:
        print(i, j)
    i += 1
    j += 1


