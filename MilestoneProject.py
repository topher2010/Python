import random

def display_board(board):
    print(' ' + board[1] + ' ' + ' | ' + ' ' + board[2] + ' ' + ' | ' + ' ' + board[3] + ' ')
    print(' ' + board[4] + ' ' + ' | ' + ' ' + board[5] + ' ' + ' | ' + ' ' + board[6] + ' ')
    print(' ' + board[7] + ' ' + ' | ' + ' ' + board[8] + ' ' + ' | ' + ' ' + board[9] + ' ')

def player_input():
    marker = ' '

    while not (marker == 'X' or marker == 'O'):
        marker == input("Player 1: Choose X or O ").upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('0', 'X')

def place_marker(board, marker, position):
    board[position] = marker
    
def win_check(board, marker):
    
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or #across the top
           (board[4] == marker and board[5] == marker and board[6] == marker) or #across middle
           (board[7] == marker and board[8] == marker and board[9] == marker) or #across bottom
           (board[1] == marker and board[4] == marker and board[7] == marker) or #down left
           (board[2] == marker and board[5] == marker and board[8] == marker) or #down center
           (board[3] == marker and board[6] == marker and board[9] == marker) or #down right
           (board[1] == marker and board[5] == marker and board[9] == marker) or #diagonal left to right
           (board[3] == marker and board[5] == marker and board[7] == marker)) #diagonal right to left

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space-check(board, i):
            return False
        return True
    
def player_choice(board):
    
