def print_board(board):
    for i in range(len(board)):
        print(" ".join([str(x) for x in board[i]]))

board = [[0 for _ in range(8)] for _ in range(8)]

for i in range(8):
    for j in range(8):
        if (i < 3 or i > 4) and (i + j) % 2 == 1:
            board[i][j] = 1

print_board(board)