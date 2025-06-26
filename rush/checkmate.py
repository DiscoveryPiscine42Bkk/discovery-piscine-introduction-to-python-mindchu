#!/usr/bin/env python3

def checkmate(board):
    board_location = coordinated_position(board) #create location of chess using list.
    board_row = len(board_location)
    board_column = check_format(board_row, board_location) #check the square format
    king_pos = find_king(board_column, board_row, board_location) #check king position
    count_king(board_column, board_row, board_location) #check how many king
    king = is_king_check(board, king_pos, board_column, board_row, board_location)
    if king == True:
        return print("Success")
    else:
        return print("Fail")

def coordinated_position(board):
    board_location = [] #big list
    chess_location = [] #small list
    for location in board:
        if location == "\n":
            board_location.append(chess_location)
            chess_location = []
        else:
            chess_location.append(location)
    board_location.append(chess_location)
    #print(f"This board format is {board_location}")
    return board_location

def check_format(board_row, board_location):
    count_king_column = []
    for i in range(board_row):
        count_king_column.append(len(board_location[i]))

    for j in range(len(count_king_column)):
        if count_king_column[j] != len(board_location[0]):
            print("Error")
            quit()
    board_column = len(board_location[0])
    #print(f"This board has {board_row} row.")
    #print(f"This board has {board_column} column.")
    if board_column != board_row:
        print("Error")
        quit()
    return board_column

def find_king(board_column, board_row, board_location):
    for i in range(board_row):
        for j in range(board_column):
            if board_location[i][j] == 'K':
                return (i,j)

def count_king(board_column, board_row, board_location):
    count = 0
    for i in range(board_row):
        for j in range(board_column):
            if board_location[i][j] == 'K':
                count += 1
    if count > 1:
        print("Error: Too many king.")
        quit()
    elif count == 0:
        print("Error: No king on the board.")
        quit()
    else:
        return

def is_king_check(board, king_pos, board_column, board_row, board_location):
    pawn = is_pawn_check(board, king_pos, board_column, board_row, board_location)
    rook = is_rook_check(board, king_pos, board_column, board_row, board_location)
    bishop = is_bishop_check(board, king_pos, board_column, board_row, board_location)
    if pawn == True or rook == True or bishop == True:
        return True
    else:
        return False

def is_pawn_check(board, king_pos, board_column, board_row, board_location):
    king_row, king_column = king_pos
    possible_positions = [(king_row + 1, king_column - 1), (king_row + 1, king_column + 1)]
    for x, y in possible_positions:
        if 0 <= x < board_row and 0 <= y < board_column and board_location[x][y] == 'P':
            return True
    return False

def is_rook_check(board, king_pos, board_column, board_row, board_location):
    king_row, king_column = king_pos
    # Check horizontally to the left
    for i in range(king_column - 1, -1, -1):
        if board_location[king_row][i] == 'R' or board_location[king_row][i] == 'Q':
            return True
        if board_location[king_row][i] != '.':
            break

    # Check horizontally to the right
    for i in range(king_column + 1, board_column):
        if board_location[king_row][i] == 'R' or board_location[king_row][i] == 'Q':
            return True
        if board_location[king_row][i] != '.':
            break

    # Check vertically upwards
    for i in range(king_row - 1, -1, -1):
        if board_location[i][king_column] == 'R' or board_location[i][king_column] == 'Q':
            return True
        if board_location[i][king_column] != '.':
            break

    # Check vertically downwards
    for i in range(king_row + 1, board_row):
        if board_location[i][king_column] == 'R' or board_location[i][king_column] == 'Q':
            return True
        if board_location[i][king_column] != '.':
            break
    return False

def is_bishop_check(board, king_pos, board_column, board_row, board_location):
    king_row, king_column = king_pos
    for i in range(1,board_row):
        # Check main diagonal (bottom-right)
        if 0 <= king_row + i <board_row and 0 <= king_column + i < board_column:
            if board_location [king_row + i][king_column + i] == 'B' or board_location [king_row + i][king_column + i] == 'Q':
                return True
            if board_location [king_row + i][king_column + i] != '.':
                break

        # Check main diagonal (top-left)
        if 0 <= king_row - i <board_row and 0 <= king_column - i < board_column:
            if board_location [king_row - i][king_column - i] == 'B' or board_location [king_row - i][king_column - i] == 'Q':
                return True
            if board_location [king_row - i][king_column - i] != '.':
                break

        # Check anti-diagonal (bottom-left)
        if 0 <= king_row + i <board_row and 0 <= king_column - i < board_column:
            if board_location [king_row + i][king_column - i] == 'B' or board_location [king_row + i][king_column - i] == 'Q':
                return True
            if board_location [king_row + i][king_column - i] != '.':
                break

        # Check anti-diagonal (top-right)
        if 0 <= king_row - i <board_row and 0 <= king_column + i < board_column:
            if board_location [king_row - i][king_column + i] == 'B' or board_location [king_row - i][king_column + i] == 'Q':
                return True
            if board_location [king_row - i][king_column + i] != '.':
                break
    return False
