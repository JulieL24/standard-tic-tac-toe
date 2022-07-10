def print_board(entries):
    line = "+---+---+---+"
    output = line
    n = 0
    for entry in entries:
        if n % 3 == 0:
            output = output + "\n| "
        else:
            output = output + " | "
        output = output + str(entry)
        if n % 3 == 2:
            output = output + " |\n"
            output = output + line
        n = n + 1
    print(output)
    print()

def game_over(board, current_player):
    print_board(board)
    print("GAME OVER")
    print(current_player, "has won")
    exit()

def top_row_is_winner(board):
    return board[0] == board[1] and board[1] == board[2]

def middle_row_is_winner(board):
    return board[3] == board[4] and board[4] == board[5]

def bottom_row_is_winner(board):
    return board[6] == board[7] and board[7] == board[8]

def left_column_is_winner(board):
    return board[0] == board[3] and board[3] == board[6]

def middle_column_is_winner(board):
    return board[1] == board[4] and board[4] == board[7]

def right_column_is_winner(board):
    return board[2] == board[5] and board[5] == board[8]

def left_diagonal_is_winner(board):
    return board[0] == board[4] and board[4] == board[8]

def right_diagonal_is_winner(board):
    return board[2] == board[4] and board[4] == board[6]

def is_row_winner(board, row_number):
    if row_number == 1:
       return top_row_is_winner(board)
    elif row_number == 2:
        return middle_row_is_winner(board)
    elif row_number == 3:
        return bottom_row_is_winner(board)
 
def is_column_winner(board, column_num):
    if column_num == 1:
        return left_column_is_winner(board)
    elif column_num == 2:
        return middle_column_is_winner(board)
    elif column_num == 3:
        return right_column_is_winner(board)

def is_diagonal_winner(board, diagonal_num):
    if diagonal_num == 1:
        return left_diagonal_is_winner(board)
    if diagonal_num == 2:
        return right_diagonal_is_winner(board)

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
current_player = "X"

for move_number in range(1, 10):
    print_board(board)
    response = input("Where would " + current_player + " like to move? ")
    space_number = int(response) - 1
    board[space_number] = current_player

    if is_row_winner(board, 1):
        game_over(board,current_player)

    elif is_row_winner(board, 2):
        game_over(board,current_player)

    elif is_row_winner(board, 3):
        game_over(board,current_player)

    elif is_column_winner(board, 1):
        game_over(board,current_player)

    elif is_column_winner(board, 2):
        game_over(board,current_player)

    elif is_column_winner(board, 3):
        game_over(board,current_player)

    elif is_diagonal_winner(board, 1):
        game_over(board,current_player)

    elif is_diagonal_winner(board, 2):
        game_over(board,current_player)


    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("It's a tie!")


