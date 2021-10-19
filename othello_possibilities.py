from othello_board import flippy


def board_possi(b, play):
    for i in range(8):
        for j in range(8):
            if b[i][j] == 0 or b[i][j] == 3:
                b[i][j] = play
                check_move = flippy(b, i, j, True)
                if check_move:
                    b[i][j] = 3
                else:
                    b[i][j] = 0
    return b


# board = [[0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 3, 1, 2, 0, 0, 0],
#          [0, 0, 1, 2, 1, 0, 0, 0],
#          [0, 0, 2, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0],
#          [0, 0, 0, 0, 0, 0, 0, 0]]
# player = 1

# board = board_possi(board, player)
# for i in board:
#     print(i)
