import random

def choose_first():
    return random.randint(0,2)

def display_board(board):
    print(board[0][0], board[0][1], board[0][2])
    print(board[1][0], board[1][1], board[1][2])
    print(board[2][0], board[2][1], board[2][2])


def player_input(player, board):
    valid_input = False
    row = None
    column = None
    while not valid_input:
        row = int(input('Please enter a valid row number from 1 - 3: '))
        column = int(input('Please enter a valid column number from 1 - 3: '))
        if row < 1 or row > 3 or column < 1 or column > 3:
            print('Row and column outside range, please pick again')
        elif board[row - 1][column - 1] != ' ':
            print('Square is already taken. Pick again')
        else:
            valid_input = True
    return row, column


def player_symbol(player):
    if player % 2 == 1:
        return 'X'
    else:
        return 'O'


def game_over(board, row, column, symbol):
    for position in range(0, 3):
        if board[position][column] != symbol:
            break
        elif position == 2:
            print("Victory for ", symbol)
            return True

    for position in range(0, 3):
        if board[row][position] != symbol:
            break
        elif position == 2:
            print("Victory for ", symbol)
            return True

    if row == column:
        for position in range(0, 3):
            if board[position][position] != symbol:
                break
            elif position == 2:
                print("Victory for ", symbol)
                return True

    if (row + column) == 2:
        for position in range(0, 3):
            if board[position][2 - position] != symbol:
                break
            elif position == 2:
                print("Victory for ", symbol)
                return True
    return False


def move(player, board, row, column, symbol):
    board[row][column] = symbol

def tic_tac_toe():
    print('Welcome to Tic Tac Toe')
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    player = choose_first()
    game_is_over = False
    while not game_is_over and player < 9:
        symbol = player_symbol(player)
        row, column = player_input(player, board)
        move(player, board, row - 1, column - 1, symbol)
        game_is_over = game_over(board, row - 1, column - 1, symbol)
        display_board(board)
        player += 1

def check_replay():
    valid_input = False
    replay = None
    while not valid_input:
        replay = input("Do you want to play again? Y/N: ")
        print(replay)
        if (replay is not "Y") and (replay is not "N"):
            print("Invalid response. Please enter Y or N.")
        else:
            valid_input = True
    if replay is "Y":
        return True
    else:
        return False

def game():
    replay = True
    while replay:
        tic_tac_toe()
        replay = check_replay()

game()
