#!/usr/bin/env python3

def checkmate(board):
    board_location = coordinated_position(board) #create location of chess using list.
    row_num = len(board_location)
    column_num = len(board_location[0])
    if check_format(row_num, board_location):
        return print("Error: Invalid board input")
    king_pos = find_king(column_num, row_num, board_location) #check king position
    count = count_king(column_num, row_num, board_location) #check how many king
    if count > 1:
        return print("Error: Too many king")
    elif count == 0:
        return print("Error: No king on the board")
    put_board(board_location)
    king = is_king_check(king_pos, column_num, row_num, board_location)
    if king == True:
        return print("Success")
    else:
        return print("Fail")

def put_board(board_location):
    print("Chessboard:")
    for row in board_location:
        first_col = 0
        for col in row:
            if first_col == 0:
                first_col = 1
                print(col, end="")
            else:
                print(" " + col, end="")
        print()

def coordinated_position(board):
    board_location = [] #big list
    chess_location = [] #small list

    for location in board:
        if location == "\n":
            board_location.append(chess_location)
            chess_location = []
        else:
            chess_location.append(location)
    # do not need this line as the board in file have \n as the last line
    # board_location.append(chess_location)
    return board_location

def check_format(row_num, board_location):
    column_num = len(board_location[0])
    count_column = []

    for i in range(row_num):
        count_column.append(len(board_location[i]))
    #check every column is equal
    for j in range(len(count_column)):
        if count_column[j] != column_num:
            return True
    #check column is equal to row
    if column_num != row_num:
        return True
    return False

def find_king(column_num, row_num, board_location):
    for i in range(row_num):
        for j in range(column_num):
            if board_location[i][j] == 'K':
                return (i,j)

def count_king(column_num, row_num, board_location):
    count = 0
    for i in range(row_num):
        for j in range(column_num):
            if board_location[i][j] == 'K':
                count += 1
    return count

def is_king_check(king_pos, column_num, row_num, board_location):
    pawn = is_pawn_check(king_pos, column_num, row_num, board_location)
    if pawn == True:
        print("King is in check by Pawn")
        return True
    rook = is_rook_check(king_pos, column_num, row_num, board_location)
    if rook == True:
        print("King is in check by Rook or Queen")
        return True
    bishop = is_bishop_check(king_pos, column_num, row_num, board_location)
    if bishop == True:
        print("King is in check by Bishop or Queen")
        return True
    return False

def is_pawn_check(king_pos, column_num, row_num, board_location):
    king_row, king_column = king_pos
    possible_positions = [(king_row + 1, king_column - 1), (king_row + 1, king_column + 1)]
    for x, y in possible_positions:
        if 0 <= x < row_num and 0 <= y < column_num and board_location[x][y] == 'P':
            return True
    return False

def is_rook_check(king_pos, column_num, row_num, board_location):
    king_row, king_column = king_pos
    # Check horizontally to the left
    for i in range(king_column - 1, -1, -1):
        if board_location[king_row][i] == 'R' or board_location[king_row][i] == 'Q':
            return True
        if board_location[king_row][i] in ['P','B']:
            break

    # Check horizontally to the right
    for i in range(king_column + 1, column_num):
        if board_location[king_row][i] == 'R' or board_location[king_row][i] == 'Q':
            return True
        if board_location[king_row][i] in ['P','B']:
            break

    # Check vertically upwards
    for i in range(king_row - 1, -1, -1):
        if board_location[i][king_column] == 'R' or board_location[i][king_column] == 'Q':
            return True
        if board_location[i][king_column] in ['P','B']:
            break

    # Check vertically downwards
    for i in range(king_row + 1, row_num):
        if board_location[i][king_column] == 'R' or board_location[i][king_column] == 'Q':
            return True
        if board_location[i][king_column] in ['P','B']:
            break
    return False

def is_bishop_check(king_pos, column_num, row_num, board_location):
    king_row, king_column = king_pos
    for i in range(1, row_num):
        # Check main diagonal (bottom-right)
        if 0 <= king_row + i < row_num and 0 <= king_column + i < column_num:
            if board_location [king_row + i][king_column + i] == 'B' or board_location [king_row + i][king_column + i] == 'Q':
                return True
            if board_location [king_row + i][king_column + i] in ['P','R']:
                break

        # Check main diagonal (top-left)
        if 0 <= king_row - i < row_num and 0 <= king_column - i < column_num:
            if board_location [king_row - i][king_column - i] == 'B' or board_location [king_row - i][king_column - i] == 'Q':
                return True
            if board_location [king_row - i][king_column - i] in ['P','R']:
                break

        # Check anti-diagonal (bottom-left)
        if 0 <= king_row + i < row_num and 0 <= king_column - i < column_num:
            if board_location [king_row + i][king_column - i] == 'B' or board_location [king_row + i][king_column - i] == 'Q':
                return True
            if board_location [king_row + i][king_column - i] in ['P','R']:
                break

        # Check anti-diagonal (top-right)
        if 0 <= king_row - i < row_num and 0 <= king_column + i < column_num:
            if board_location [king_row - i][king_column + i] == 'B' or board_location [king_row - i][king_column + i] == 'Q':
                return True
            if board_location [king_row - i][king_column + i] in ['P','R']:
                break
    return False
