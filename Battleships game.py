import random

horizontal = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ж': 6, 'З': 7,'И': 8, 'К': 9}
vertical = {'1': 0, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7,'9': 8, '10': 9}
ships_allowed = {4: 1, 3:2, 2:3, 1:4}

class Board:
    def __init__(self, auto = 'n'):
        self.auto = auto
        #при инициализации класса формируем пустую доску
        self.board = []
        columns = list(horizontal.keys())
        columns.insert(0, ' ')
        rows = list(vertical.keys())
        self.board.append(columns)
        for i in rows:
            row = [i]
            row.extend(list([' ']*10))
            self.board.append(row)

        self.ships_on_board = {4:0, 3:0, 2:0, 1:0}
        self.ships_orig_collection = []
        self.ships_cur_collection = []

    def print_board(self):
        #чтобы вывести на печать
        if self.auto == 'n':
            line = ''
            for i in self.board:
                for j in i:
                    line += '  |  ' + j
                line += '  |  \n -------------------------------------------------------------------- \n'
            print(line)
        else:
            auto_board = self.board.copy()
            i = 0
            while i < len(auto_board):
                j = 0
                while j < len(auto_board[i]):
                    auto_board[i][j] = auto_board[i][j].replace('О', ' ')
                    auto_board[i][j] = auto_board[i][j].replace('-', ' ')
                    j+=1
                i+=1
            line = ''
            for i in self.board:
                for j in i:
                    line += '  |  ' + j
                line += '  |  \n -------------------------------------------------------------------- \n'
            print(line)

    def draw_ship(self, list_coord):
        self.list_coord = list_coord
        for i in list_coord:
            self.board[i[0]][i[1]] = 'О'

    def draw_around(self, list_coord, symbol):
        self.list_coord = list_coord
        self.symbol = symbol
        minx = list_coord[0][0]-1
        miny = list_coord[0][1]-1
        maxx = list_coord[-1][0]+1
        maxy = list_coord[-1][1]+1
        for i in range(max(minx, 1), min(10, maxx)+1):
            for j in range(max(miny, 1), min(10, maxy)+1):
                if self.board[i][j] != 'О' and self.board[i][j] != 'X':
                    self.board[i][j] = self.symbol


    def place_ship(self):

        #запрашиваем координаты корабля, пока они не будут существующими, по одной
        input_check = False
        while input_check == False:
            coord_1 = input('Куда поставить корабль? Введите координату начала корабля (Формат: К3) ')
            if coord_1[0] in horizontal.keys():
                if coord_1[1:] in vertical.keys():
                    input_check = True
                    coord_1x = horizontal[coord_1[0]]+1
                    coord_1y = vertical[coord_1[1:]]+1
                else: print('координаты не существует, введите еще раз')
            else: print('координаты не существует, введите еще раз')

        input_check = False
        while input_check == False:
            coord_2 = input('Введите координату конца корабля (Формат: К5) ')
            if coord_2[0] in horizontal.keys():
                if coord_2[1:] in vertical.keys():
                    input_check = True
                    coord_2x = horizontal[coord_2[0]]+1
                    coord_2y = vertical[coord_2[1:]]+1
                else: print('координаты не существует, введите еще раз')
            else: print('координаты не существует, введите еще раз')

            #получили корректные координаты, проверяем может ли получиться такой корабль
        if coord_1x == coord_2x:
            ship_len = abs(coord_2y - coord_1y)+1
        elif coord_1y == coord_2y:
            ship_len = abs(coord_2x - coord_1x) + 1
        else:
            print('положение корабля неправильное')
            return self.place_ship()

        #проверяем длину корабля и количество кораблей такой длины на доске, заполненность поля
        if ship_len <=4 and self.ships_on_board[ship_len] < ships_allowed[ship_len]:
            #проверяем что все координаты пустые до изменения поля
            for i in range(min(coord_1y, coord_2y), max(coord_1y, coord_2y)+1):
                for j in range(min(coord_1x, coord_2x), max(coord_1x, coord_2x)+1):
                    if self.board[i][j] == ' ':
                        pass
                    else:
                        print('здесь уже стоит корабль')
                        return self.place_ship()
        else:
            print(f'корабль длины {ship_len} нельзя использовать')
            return self.place_ship()

        ship = []
        for i in range(min(coord_1y, coord_2y), max(coord_1y, coord_2y) + 1):
            for j in range(min(coord_1x, coord_2x), max(coord_1x, coord_2x) + 1):
                ship.append([i, j])
        self.ships_on_board.update({ship_len: self.ships_on_board[ship_len] + 1})
        self.ships_orig_collection.append(ship)
        self.ships_cur_collection.append(ship.copy())
        self.draw_ship(ship)
        self.draw_around(ship, '-')


    def place_ship_auto(self):
        empty_slots = []
        i = 0
        while i < len(self.board):
            j = 0
            while j < len(self.board[i]):
                if self.board[i][j] == ' ' and [i,j] != [0, 0]:
                    empty_slots.append([i, j])
                j+=1
            i+=1

        length = 4
        while length > 0:
            if ships_allowed[length] > self.ships_on_board[length]:
                length = length
                break
            else:
                length -=1

        check = False
        while check == False:
            coord_1 = random.choice(empty_slots)
            coord_1y = coord_1[0]
            coord_1x = coord_1[1]
            for i in range(coord_1x, coord_1x+length):
                if [coord_1y, i] in empty_slots:
                    continue
                else:
                    for j in range(coord_1y, coord_1y + length):
                        if [j, coord_1x] in empty_slots:
                            continue
                        else:
                            break
                    else:
                        coord_2x = coord_1x
                        coord_2y = j
                        check = True
                    break
            else:
                coord_2x = i
                coord_2y = coord_1y
                check = True

        ship = []
        for i in range(min(coord_1y, coord_2y), max(coord_1y, coord_2y) + 1):
            for j in range(min(coord_1x, coord_2x), max(coord_1x, coord_2x) + 1):
                ship.append([i, j])
        self.ships_on_board.update({length: self.ships_on_board[length] + 1})
        self.ships_orig_collection.append(ship)
        self.ships_cur_collection.append(ship.copy())
        self.draw_ship(ship)
        self.draw_around(ship, '-')



    def hit(self, around = None):
        if self.auto == 'y':

            input_check = False
            while input_check == False:
                coord_hit = input('Введите координаты для удара (Формат: А3) ')
                if coord_hit[0] in horizontal.keys():
                    if coord_hit[1:] in vertical.keys():
                        input_check = True
                        coord_hitx = horizontal[coord_hit[0]] + 1
                        coord_hity = vertical[coord_hit[1:]] + 1
                    else:
                        print('координаты не существует, введите еще раз')
                        return self.hit()
                else:
                    print('координаты не существует, введите еще раз')
                    return self.hit()

            coord_hit = [coord_hity, coord_hitx]

        else:
            empty_slots = []
            i = 0
            while i < len(self.board):
                j = 0
                while j < len(self.board[i]):
                    if self.board[i][j] == ' ' or self.board[i][j] == 'О' or self.board[i][j] == '-' and [i, j] != [0, 0]:
                        empty_slots.append([i, j])
                    j += 1
                i += 1

            coord_hit = random.choice(empty_slots)
            coord_hity = coord_hit[0]
            coord_hitx = coord_hit[1]



        i = 0
        while i < len(self.ships_cur_collection):
            j = 0
            while j < len(self.ships_cur_collection[i]):
                if self.ships_cur_collection[i][j] == coord_hit:
                    self.board[coord_hity][coord_hitx] = 'X'
                    self.ships_cur_collection[i].pop(j)
                    if self.ships_cur_collection[i] == []:
                        self.draw_around(self.ships_orig_collection[i], 'x')
                        return coord_hit, 'убит'
                    else:
                        return coord_hit, 'ранен'
                else:
                    j += 1
            else:
                i += 1
        else:
            self.board[coord_hity][coord_hitx] = 'х'
            return coord_hit, 'мимо'



    def check_board(self):
        for i in self.ships_cur_collection:
            if i == []:
                continue
            else:
                return 'on'
                break
        else: return 'off'


player1 = Board(auto='y')
player2 = Board()
while player1.ships_on_board != ships_allowed:
    player1.place_ship_auto()

while player2.ships_on_board != ships_allowed:
    print('Ваше поле:')
    player2.print_board()
    player2.place_ship()


print('Поле противника:')
player1.print_board()

turn = 0
while player1.check_board() == 'on' and player2.check_board() == 'on':
    if turn == 0:
        print('Ваша очередь стрелять')
        result = player1.hit()
        print(result[1])
        if result[1] == 'убит' or result[1] == 'ранен':
            print('Доска противника:')
            player1.print_board()
            turn = 0
        else:
            print('Доска противника:')
            player1.print_board()
            turn = 1

        if player1.check_board() == 'off':
            print('Вы выиграли')
            break

    if turn == 1:
        print('Очередь противника')
        result1 = player2.hit()
        for_user = list(horizontal.keys())[list(horizontal.values()).index(result1[0][1]-1)]
        for_user += list(vertical.keys())[list(vertical.values()).index(result1[0][0]-1)]
        print('Удар противника: ', for_user)
        print(result1[1])
        if result1[1] == 'убит' or result1[1] == 'ранен':
            print('Ваша доска:')
            player2.print_board()
            turn = 1
        else:
            print('Ваша доска:')
            player2.print_board()
            turn = 0

        if player2.check_board() == 'off':
            print('Вы проиграли:')
            break

