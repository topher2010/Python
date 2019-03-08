def display_board(board):
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('---------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('---------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')

def player_input():
    marker = ' '

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player one please select X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, marker):

    return ((board[7] == marker and board[8] == marker and board[9] == marker) or
            (board[4] == marker and board[5] == marker and board[6] == marker) or
            (board[1] == marker and board[2] == marker and board[3] == marker) or
            (board[7] == marker and board[4] == marker and board[1] == marker) or
            (board[8] == marker and board[5] == marker and board[2] == marker) or
            (board[9] == marker and board[6] == marker and board[3] == marker) or
            (board[7] == marker and board[5] == marker and board[3] == marker) or
            (board[9] == marker and board[5] == marker and board[1] == marker))

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    
def player_choice(board):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Select a position to play (0-9): '))

        return position

def replay():
    return input('Do you want to play again?  y or n: ').startswith('y')

print('Welcome to Tic Tac Toe')

while True:

    board = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Are you ready to play?')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)

            if win_check(board,player1_marker):
                display_board(board)
                print('Congratulations Player 1 won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, player2_marker, position)

            if win_check(board,player2_marker):
                display_board(board)
                print('Congratulations Player 2 won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    game_on = False
                else:
                    turn = 'Player 1'

    if not replay():
        break