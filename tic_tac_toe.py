# Global Variables
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
game_still_going = True
current_player = 'X'
winner = None

# making game board and displaying
def display_board():
    print(board[0]+' | '+board[1]+' | '+board[2])
    print('---------')
    print(board[3]+' | '+board[4]+' | '+board[5])
    print('---------')
    print(board[6]+' | '+board[7]+' | '+board[8])

# handling current players position      
def handle_positions(player):
    print('-----------')
    print("<---Now "+player+"'s turn!!--->")
    position = input('Please enter your position (1-9):')
    valid = False
    while not valid:
        while position not in ['1','2','3','4','5','6','7','8','9']:
            position = input('--->Invalid Positions. Try again from (1-9):')
        position = int(position)-1
        if board[position] == " ":  
            valid = True
    board[position] = player
    display_board()   

# function for running the game
def play_game():
    display_board()
    while game_still_going:
        handle_positions(current_player)
        check_if_game_over()
        flip_player()
    if winner == 'X' or winner == 'O':
        print('-----------')
        print(winner + ' won!!')
    elif winner == None:
        print('-----------')
        print('Tie!!')

# function for game over
def check_if_game_over():
    check_if_win()
    check_if_tie()

# function for winner in the game
def check_if_win():
    global winner
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

# checking rows if there is any winner
def check_rows():
    global game_still_going
    row_1 = board[0]==board[1]==board[2]!=" "
    row_2 = board[3]==board[4]==board[5]!=" "
    row_3 = board[6]==board[7]==board[8]!=" "

    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

# checking colums if there is any winner
def check_columns():
    global game_still_going
    column_1 = board[0]==board[3]==board[6]!=" "
    column_2 = board[1]==board[4]==board[7]!=" "
    column_3 = board[2]==board[5]==board[8]!=" "

    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

# checking diagonals if there is any winner
def check_diagonals():
    global game_still_going
    diagonal_1 = board[0]==board[4]==board[8]!=" "
    diagonal_2 = board[2]==board[4]==board[6]!=" "

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

# functions for tie game
def check_if_tie():
    global game_still_going
    if " " not in board:
        game_still_going = False
    return

# changing the turn of players
def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

# finally calling the function
play_game()