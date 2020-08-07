'''A 16x16 sudoku solution must satisfy all of the following rules:
1. Each of the digits 1-G must occur exactly once in each row.
2. Each of the digits 1-G must occur exactly once in each column.
3. Each of the digits 1-G must occur exactly once in each of the
16 4x4 sub-boxes of the grid.
'''

from math import sqrt


def is_valid(board, row, col, val): #  check valid
    for i in range(length):
        if board[row][i] == val:
            return False
    for i in range(length):
        if board[i][col] == val:
            return False
    x = row - row % sub_matrix_length
    y = col - col % sub_matrix_length
    for i in range(sub_matrix_length):
        for j in range(sub_matrix_length):
            if board[i+x][y+j] == val:
                return False
    return True


def solver(row, col):
    if row == length:
        return True
    elif col >= length:     # col == 16
        return solver(row + 1, 0)
    elif board[row][col] != '.':
        return solver(row, col + 1)
    else:
        for i in range(1, 17):
            if is_valid(board, row, col, str(i)):
                board[row][col] = str(i)
                if solver(row, col + 1):
                    return True
    board[row][col] = '.'
    return False


board1 = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]

board = [[".","9",".",".","2",".","3","8","A",".",".",".",".",".",".","."],
    [".","1",".","6",".",".","D",".",".",".","8",".","F",".","B","5"],
    [".",".",".","3",".","B",".",".",".","5",".",".","G",".",".","."],
    ["7",".",".","F",".",".",".","A",".",".","G","1",".","4",".","."],
    ["G",".",".",".",".",".",".","D",".","A","C","7",".",".",".","F"],
    [".",".",".",".","1","3",".","F",".","B",".","8",".",".",".","."],
    ["1","8",".","A",".",".",".","E",".",".",".",".","2",".",".","6"],
    ["5",".",".",".",".",".",".",".",".","D",".",".","E","G","4","1"],
    ["9",".",".",".","E",".",".",".","7","1",".",".",".","A",".","4"],
    [".",".",".",".",".",".","1",".",".","9",".","E","C",".","8","."],
    [".","2","C","D",".",".","7",".","4",".",".",".",".","E","5","."],
    [".","4",".",".",".",".",".",".",".",".","D","6",".",".",".","G"],
    [".",".",".",".","F","8","B","4",".",".",".","2","A",".",".","."],
    ["E","3",".",".","9","7",".",".","6",".",".",".",".",".",".","."],
    [".","F","8","4",".",".","A",".",".",".","5",".","6",".",".","9"],
    [".",".",".",".",".","2",".","1","8",".",".","B",".",".",".","D"]]

length = len(board)
sub_matrix_length = int(sqrt(length))

solver(0, 0)
for a in board:
    print(a)
