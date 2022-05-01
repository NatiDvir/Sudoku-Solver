bo = [
    [3, 0, 2, 0, 5, 0, 6, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0, 0],
    [1, 0, 0, 0, 0, 9, 5, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 9, 0],
    [0, 4, 3, 0, 0, 0, 7, 5, 0],
    [0, 9, 0, 0, 0, 4, 0, 0, 8],
    [4, 0, 9, 7, 0, 0, 0, 6, 0],
    [0, 0, 0, 2, 0, 0, 0, 0, 0],
    [0, 0, 7, 0, 4, 0, 2, 0, 3]
]


def printBoard(board):
    for i in range(len(board[0])):
        if i % 3 == 0 :
            print("- - - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0:
                print("| ", end="")
            if j == 8:
                print(str(board[i][j]) + " |")
            else:
                print(str(board[i][j]) + " ", end="")
    print("- - - - - - - - - - - - -")


def emptyPosition(board):
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def checkRow(board, num, position):
    for i in range(len(board[0])):
        if num == board[position[0]][i] and position[1] != i:
            return False
    return True


def checkCol(board, num, position):
    for i in range(len(board[0])):
        if num == board[i][position[1]] and position[0] != i:
            return False
    return True


def checkBox(board, num, position):
    boxX = position[0] // 3
    boxY = position[1] // 3
    for i in range(boxX*3,boxX*3 + 3):
        for j in range(boxY*3,boxY*3 + 3):
            if num == board[i][j] and position != (i, j):
                return False
    return True


def checkValid(board, num, position):
    if checkBox(board, num, position) and checkCol(board, num, position) and checkRow(board, num, position):
        return True
    else:
        return False


def solve(board):
    pos = emptyPosition(bo)
    if not pos:  # If no empty place - board is full
        return True
    else:
        for i in range(1, 10):  # Check for all numbers 1-9 to fit
            if checkValid(bo, i, (pos[0], pos[1])):  # Check if number 'i' is a valid number.
                bo[pos[0]][pos[1]] = i
                if solve(bo):  # Recursive call to backtrack
                    return True
                bo[pos[0]][pos[1]] = 0  # If solution is wrong - delete number from position and try the next number.
        return False



printBoard(bo)
print("Solution:")
solve(bo)
printBoard(bo)
