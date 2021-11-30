import random


def display_board(board):
    '''
    Board Layout
    '''
    print('  ' + board[1] + '|' + board[2] + '|' + board[3])
    print(' -------')
    print('  ' + board[4] + '|' + board[5] + '|' + board[6])
    print(' -------')
    print('  ' + board[7] + '|' + board[8] + '|' + board[9])


def player_input_marker():

    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Choose X or O: ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    '''
    Player's marker place holder
    '''
    board[position] = marker


def win_check(board, mark):

    return ((board[1] == mark and board[2] == mark and board[3] == mark)
            or (board[4] == mark and board[5] == mark and board[6] == mark)
            or (board[7] == mark and board[8] == mark and board[9] == mark)
            or (board[1] == mark and board[4] == mark and board[7] == mark)
            or (board[2] == mark and board[5] == mark and board[8] == mark)
            or (board[3] == mark and board[6] == mark and board[9] == mark)
            or (board[1] == mark and board[5] == mark and board[9] == mark)
            or (board[3] == mark and board[5] == mark and board[7] == mark))


def choose_player():
    '''
    Randomly choose which player goes first
    '''
    choice = random.randint(0, 1)
    if choice == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    '''
    return True is a particular position on the board is empty
    '''

    return board[position] == ' '


def full_board_check(board):

    for i in range(1, 10):
        if space_check(board, i):
            return False

    return True


def player_choice(board, player_turn):
    '''
    player chooses a position
    '''
    position = 0

    while position not in range(1, 10) or not space_check(board, position):
        position = int(input(f'{turn} choose a position (1-9): '))

    return position


def play_again():
    choice = input('Enter y to play again, n to quit: ').lower()
    while not choice in ['y', 'n']:
        choice = input('Enter y to play again, n to quit: ').lower()
    if choice == 'y':
        return 'y'
    else:
        return 'n'


###### Main Game Code ##########

while True:
    #Setting up the game
    the_board = [' '] * 10

    player1_marker, player2_marker = player_input_marker()
    print(f'Player 1: {player1_marker}')
    print(f'Player 2: {player2_marker}')

    turn = choose_player()
    # turn = 'Player 1'
    print(f'{turn} goes first')

    game_on = True
    while game_on:

        if turn == 'Player 1':
            #display board
            display_board(the_board)

            #choose a position
            position = player_choice(the_board, turn)

            #place marker on the position selected by player 1
            place_marker(the_board, player1_marker, position)

            #check if player 1 has won the game
            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Player 1 has won the game!')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie")
                    game_on = False
                else:
                    turn = 'Player 2'

        else:
            #display board
            display_board(the_board)

            #choose a position
            position = player_choice(the_board, turn)

            #place marker on the selected position by player 2
            place_marker(the_board, player2_marker, position)

            #check if player 2 wins the game
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Player 2 has won the game')
                game_on = False

            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print("It's a tie")
                    game_on = False
                else:
                    turn = 'Player 1'

    if play_again() == 'y':
        pass
    else:
        break
