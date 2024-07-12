from random import choice

game_board = {
    '0,0': '',
    '0,1': '',
    '0,2': '',
    '1,0': '',
    '1,1': '',
    '1,2': '',
    '2,0': '',
    '2,1': '',
    '2,2': ''
}


def print_board(board):
    print(board['0,0'] or ' ','|', board['0,1'] or ' ','|', board['0,2'])
    print('-- -- --')
    print(board['1,0'] or ' ','|', board['1,1'] or ' ','|', board['1,2'])
    print('-- -- --')
    print(board['2,0'] or ' ' ,'|', board['2,1'] or ' ','|', board['2,2'])

def print_board2(board):
     for i in range(11):
        if i==3 or i==7 :
            #7 * 3 = 24 + 2 empties = 26 spaces
            line = "-"* 7 + " "
            print(line * 3)
        elif i==1:
            #positions 0,0 0,1 0,2
            if board['0,0']=='':
                print("  0,0  |", end="")
            else:
                print("   "+board['0,0']+"   |",end="")
            if board['0,1']=='':
                print("  0,1  |", end="")
            else:
                print("   "+board['0,1']+"   |",end="")
            if board['0,2']=='':
                print("  0,2  ")
            else:
                print("   "+board['0,2']+"   ")
        elif i==5:
            #positions 1,0 1,1 1,2
            if board['1,0']=='':
                print("  1,0  |", end="")
            else:
                print("   "+board['1,0']+"   |",end="")
            if board['1,1']=='':
                print("  1,1  |", end="")
            else:
                print("   "+board['1,1']+"   |",end="")
            if board['1,2']=='':
                print("  1,2  ")
            else:
                print("   "+board['1,2']+"   ")
        elif i==9:
            #positions 2,0 2,1 2,2
            if board['2,0']=='':
                print("  2,0  |", end="")
            else:
                print("   "+board['2,0']+"   |",end="")
            if board['2,1']=='':
                print("  2,1  |", end="")
            else:
                print("   "+board['2,1']+"   |",end="")
            if board['2,2']=='':
                print("  2,2  ")
            else:
                print("   "+board['2,2']+"   ")
        else:
            line = (" "* 7)+"|"
            print(line * 2)


# print_board(game_board)

def play_game(game_board):
    is_game_over = False
    print_board2(game_board)
    while is_game_over == False:
        get_user_move(game_board)
        is_game_over = is_game_over_check(game_board)
        if(is_game_over!= False):
            print_board2(game_board)
            continue
        get_computer_move(game_board)
        is_game_over = is_game_over_check(game_board)
        print_board2(game_board)
    if is_game_over == 'tie':
        print("It's a tie!")
    else:
        print(f"The winner is {is_game_over}!")


def get_user_move(game_board):
    move = input("X, choose a spot in the format 'x,y': ")
    while not is_valid_move(game_board, move):
        move = input("That is not a valid move, choose another: ")

    game_board[move] = 'X'
    # print_board(game_board)


def is_valid_move(game_board, move):
    return is_game_over_check(game_board) == False and move in game_board and game_board[move] == ''


def get_computer_move(game_board):
    move = choice(list(game_board.keys()))
    while not is_valid_move(game_board, move):
        move = choice(list(game_board.keys()))
    game_board[move] = 'O'


def is_game_over_check(game_board):
    if game_board['0,0'] == game_board['0,1'] == game_board['0,2'] and game_board['0,0'] != '' or game_board['0,0'] == game_board['1,0'] == game_board['2,0'] and game_board['0,0'] != '' or game_board['0,0'] == game_board['1,1'] == game_board['2,2'] and game_board['0,0'] != '':
        return game_board['0,0']
    elif game_board['1,0'] == game_board['1,1'] == game_board['1,2'] and game_board['1,0'] != '' or game_board['0,1'] == game_board['1,1'] == game_board['2,1'] and game_board['0,1'] != '' or game_board['0,2'] == game_board['1,1'] == game_board['2,0'] and game_board['0,2'] != '':
        return game_board['1,1']
    elif game_board['2,0'] == game_board['2,1'] == game_board['2,2'] and game_board['2,0'] != '' or game_board['0,2'] == game_board['1,2'] == game_board['2,2'] and game_board['0,2'] != '':
        return game_board['2,2']
    else:
        if '' not in game_board.values():
            return 'tie'
        else:
            return False


play_game(game_board)
