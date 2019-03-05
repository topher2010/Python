

board = [' ']*10

def display_board(board):
    print(' ' + board[1] + ' ' + ' | ' + ' ' + board[2] + ' ' + ' | ' + ' ' + board[3] + ' ')
    print('---------------')
    print(' ' + board[4] + ' ' + ' | ' + ' ' + board[5] + ' ' + ' | ' + ' ' + board[6] + ' ')
    print('---------------')
    print(' ' + board[7] + ' ' + ' | ' + ' ' + board[8] + ' ' + ' | ' + ' ' + board[9] + ' ')

def player_input():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ')
    
    player1 = marker
    
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
        
    return (player1,player2)

def win_check(board, marker):
    
    return ((board[1] == marker and board[2] == marker and board[3] == marker) or #across the top
           (board[4] == marker and board[5] == marker and board[6] == marker) or #across middle
           (board[7] == marker and board[8] == marker and board[9] == marker) or #across bottom
           (board[1] == marker and board[4] == marker and board[7] == marker) or #down left
           (board[2] == marker and board[5] == marker and board[8] == marker) or #down center
           (board[3] == marker and board[6] == marker and board[9] == marker) or #down right
           (board[1] == marker and board[5] == marker and board[9] == marker) or #diagonal left to right
           (board[3] == marker and board[5] == marker and board[7] == marker)) #diagonal right to left
