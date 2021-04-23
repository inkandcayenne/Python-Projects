# Tic Tack Toe
from IPython.display import clear_output

row1 = [' ', ' ', ' ']
row2 = [' ', ' ', ' ']
row3 = [' ', ' ', ' ']
cur_board = [row1, row2, row3]
cur_symbols = ["X", "O"]
cur_symbol_queue = 0


def clear_board(board):
    for i in range(0, 3):
        for j in range(0, 3):
            board[i][j] = ' '


# печать доски
def print_board(board):
    print(" | ".join(board[0]), " | ".join(board[1]), " | ".join(board[2]), sep='\n -------- \n')


# проверяем выигрыш каждого символа
def game_results(board, symbols):
    game_result = 'not finished'

    for symbol in symbols:
        # проверяем по строкам

        for row in board:
            if row.count(symbol) == 3:
                print(symbol, "выиграл")
                game_result = 'win'
                break

        # проверяем по столбцам
        for i in range(0, 3):
            columns_sum = 0
            for row in board:
                columns_sum = columns_sum + row[i].count(symbol)
            if columns_sum == 3:
                print(symbol, "выиграл")
                game_result = 'win'
                break

        # проверяем по диагоналям

        if board[0][0].count(symbol) + board[1][1].count(symbol) + board[2][2].count(symbol) == 3:
            print(symbol, "wins")
            game_result = 'win'
            break
        elif board[2][0].count(symbol) + board[1][1].count(symbol) + board[0][2].count(symbol) == 3:
            print(symbol, "wins")
            game_result = 'win'
            break

    # проверяем есть ли незаполненые поля, если никто не выиграл
    if game_result != 'win' and board[0].count(' ') + board[1].count(' ') + board[2].count(' ') > 0:
        game_result = 'not finished'
        print('делайте ход')

    # если все заполнено и никто не выиграл - это ничья
    elif game_result != 'win' and board[0].count(' ') + board[1].count(' ') + board[2].count(' ') == 0:
        game_result = 'even'
        print('ничья')
    return game_result


# user input
def enter_value(board):
    input_correct = False
    while input_correct == False:
        row_input = input('Введите номер строки от 0 до 2: ')
        if row_input in ['0', '1', '2']:
            column_input = input('Введите номер столбца от 0 до 2: ')
            if column_input in ['0', '1', '2']:
                row_input = int(row_input)
                column_input = int(column_input)
                if board[row_input][column_input] == ' ':
                    input_correct = True
                else:
                    clear_output()
                    print('Место занято')
            else:
                clear_output()
                print('введите столбец в соответствии с требованиями')
        else:
            clear_output()
            print('введите строку в соответствии с требованиями')
    return row_input, column_input


# изменения в списке
def change_value(board, row_input_fin, column_input_fin):
    if symbol_queue % 2 == 0:
        board[row_input_fin][column_input_fin] = 'O'
    else:
        board[row_input_fin][column_input_fin] = 'X'
    return board


symbol_queue = 0
clear_board(cur_board)
print('начннем играть')

while game_results(cur_board, cur_symbols) == 'not finished':
    symbol_queue += 1
    row_column = enter_value(cur_board)
    cur_board = change_value(cur_board, row_column[0], row_column[1])
    print_board(cur_board)
