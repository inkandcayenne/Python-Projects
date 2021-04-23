# bubbles sort

def bubble_sort(list_for_sort):
    swaps_num = None
    #выполняем пока количество перестановок не станет 0

    while swaps_num != 0:
        swaps_num = 0
        count = 0

        #сравниваем соседей пока не кончится список
        for i in list_for_sort:
            if count < len(list_for_sort) - 1:
                a = list_for_sort[count]
                b = list_for_sort[count + 1]

                #проверяем и переставляем соседей
                if a > b:
                    list_for_sort[count] = b
                    list_for_sort[count + 1] = a
                    swaps_num += 1
            count += 1
    return list_for_sort


# Examples
sort_list = [1000, 1, 2, 4, 88]
print(bubble_sort(sort_list))
sort_list1 = [1011, 1011, 3, 4, 88, 88]
print(bubble_sort(sort_list1))


# Merge sort

def mergesort(array):
    if len(array) > 1:
        mid = len(array) // 2
        #делим на левую и правую часть при каждом вызове функции
        left = array[:mid]
        right = array[mid:]
        #вызываем рекурсию до базового случая - когда остался 1 элемент
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0
        #получаем отсортированные массивы и добавляем хвосты, если они не равной длины
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            array[k] = left[i]
            k += 1
            i += 1
        while j < len(right):
            array[k] = right[j]
            k += 1
            j += 1
        return array


# Examples:
print(mergesort([1, 4, 2, 100, 3, 6]))
