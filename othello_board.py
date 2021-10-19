def flippy(board, row_change, col_change, check=False):
    from itertools import permutations
    flip_dic = {1: 2, 2: 1, 3: 3, 0: 0}
    flip_cords_final = []
    is_changed = False

    for r, c in list(permutations([0, 1, -1], 2)) + [(1, 1), (-1, -1)]:
        r_change = r
        c_change = c
        flip_cords = []
        while True:
            try:
                if (board[row_change+r][col_change+c] != 0) and (board[row_change+r][col_change+c] != board[row_change][col_change]) and (board[row_change+r][col_change+c] != 3):
                    flip_cords.append((row_change+r, col_change+c))
                    r = r + r_change
                    c = c + c_change
                elif (board[row_change+r][col_change+c] == 0) or (board[row_change+r][col_change+c] == 3):
                    flip_cords = []
                    break
                else:
                    break
            except IndexError:
                flip_cords = []
                break
            if row_change+r < 0 or col_change+c < 0:
                flip_cords = []
        flip_cords_final = flip_cords_final + flip_cords

    if not check:
        for i, j in flip_cords_final:
            board[i][j] = flip_dic[board[i][j]]
        return board
    else:
        if not flip_cords_final == []:
            is_changed = True
            return is_changed


# board = [[1, 0, 0, 2, 0, 1, 2, 1],
#          [0, 2, 0, 2, 0, 1, 0, 2],
#          [0, 0, 2, 2, 2, 0, 0, 1],
#          [0, 1, 2, 1, 2, 2, 1, 2],
#          [0, 0, 2, 2, 2, 0, 0, 2],
#          [0, 2, 0, 2, 0, 2, 0, 2],
#          [1, 0, 0, 2, 0, 0, 1, 2],
#          [2, 2, 2, 1, 2, 2, 2, 2]]
# col_change = 3
# row_change = 0

# board, bool = flippy(board, row_change, col_change)

# print("\nFlipped board: ")
# for i in board:
#     print(i)
# print(bool)
