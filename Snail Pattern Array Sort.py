
# Дан массив рахмера n x n. Напишите функцию, возвращающую элементы массива по спирали,
# начиная с внешних элементов, двигаясь по часовой стрелке внутрь
# Пример, на вход дан массив:
# [[1,2,3,4],
#  [4,5,6,8],
#  [7,8,9,0],
#  [7,8,9,0]]
# Результат работы функции: [1, 2, 3, 4, 8, 0, 0, 9, 8, 7, 7, 4, 5, 6, 9, 8]

def snail(arr):
    result_arr = []

    while len(arr) != 0:
        y = 0
        while len(arr[y]) > 0:
            result_arr.append(arr[0].pop(0))
        arr.pop(0)
        if len(arr) == 0:
            break
        while y < len(arr):
            result_arr.append(arr[y].pop())
            y += 1
        y -= 1
        while len(arr[y]) > 0:
            result_arr.append(arr[y].pop())
        arr.pop(y)
        y -= 1
        while y >= 0 and y < len(arr):
            result_arr.append(arr[y].pop(0))
            y -= 1
    return result_arr


# Examples:
array = [[1,2,3,4],
 [4,5,6,8],
 [7,8,9,0],
 [7,8,9,0]]

print(snail(array))

array = [[1,2,3,4,5],
 [16,17,18,19,6],
 [15,24,25,20,7],
 [14,23,22,21,8],
 [13,12,11,10,9]]

print(snail(array))