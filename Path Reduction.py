# Задача: Дан список направлений, которых объекту нужно придеживаться в пути.
# Возможные напрвления -  NORTH, SOUTH, WEST, EAST
# Идти сразу на юг после того, как объект пошел на север бессмысленно, так же как и идти на запад после сразу после
# того, как объект пошел на восток.
# Напишите функцию, которая принимает на вход направления пути в виде списка, а возвращает сокращенный список
# направлений, который убирает ненужные перемещения (на юг после севера или на восток после запада и наоборот)


def directions_reduction(arr):
    opposite_directions = {'NORTH': 'SOUTH', 'EAST': 'WEST', 'SOUTH': 'NORTH', 'WEST': 'EAST'}
    result_directions = []
    for direction in arr:
        if bool(result_directions) == True and result_directions[-1] == opposite_directions[direction]:
            result_directions.pop()
        else:
            result_directions.append(direction)
    return result_directions

# Examples
list_directions1 = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
print(directions_reduction(list_directions1))
list_directions2 = ["NORTH",  "EAST", "SOUTH", "WEST"]
print(directions_reduction(list_directions2))


#Решение с учетом того, что мы не хотим оказаться в одной и той же точке в течение пути.
# Для решения принимаем, что каждое направление двигает нас на 1 в соответствующую сторону

def directions_reduction2(arr):
    directions = {'NORTH': {'y': 1, 'x': 0}, 'SOUTH': {'y': -1, 'x': 0}, 'EAST': {'x': 1, 'y': 0}, 'WEST': {'x': -1, 'y': 0}}
    x = 0
    y = 0
    coordinates_collection = [[0, 0]]
    result_directions = []
    for direction in arr:
        x += directions[direction]['x']
        y += directions[direction]['y']
        if [x, y] in coordinates_collection:
            cut = coordinates_collection.index([x, y])
            coordinates_collection = coordinates_collection[:cut+1]
            result_directions = result_directions[:cut]
        else:
            coordinates_collection.append([x, y])
            result_directions.append(direction)
    return result_directions

# Examples
print(directions_reduction2(list_directions1))
print(directions_reduction2(list_directions2))







