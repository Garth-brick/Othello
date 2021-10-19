# one player mode is still in the making
# this file contains the major chunk of the code

import os
from time import sleep
import sys
from itertools import cycle
from othello_board import flippy
from othello_possibilities import board_possi


def cleanup():
    os.system('cls')
    print("O T H E L L O\n\n")


def board_refresh():
    global board, symdict, numdict, letdict
    board = [[0 for i in range(8)] for i in range(8)]
    board[4][4], board[3][3] = 1, 1
    board[3][4], board[4][3] = 2, 2


def showboard():
    global board, symdict, letdict, numdict
    dashes = "\t" + "-"*49
    print("\t   ", end="")
    for i in range(8):
        print(numdict[i+1], end="     ")
    for i in range(8):
        print("\n"+dashes)
        print(" "*5+f"{i+1}  ", end="")
        for j in range(8):
            print(f"| {symdict[board[i][j]]} ", end="")
        print("|", end="")
    print("\n"+dashes)


def letsgo():
    global board, symdict, letdict, numdict
    board_refresh()
    exit = False
    final_exit = False
    turns = 0
    for i in cycle((1, 2)):  # keep scycling between player 1 and 2 till break statement is triggered when moves are over

        cleanup()
        print(
            f"Here's the board, type a letter followed by an integer to denote the position:\nType 'exit' at any point to leave mid-game.\n")
        board = board_possi(board, i)

        white_num = 0
        black_num = 0
        move_poss = False
        for j in board:  # count numbers for each type of piece
            for k in j:
                if k == 1:
                    white_num += 1
                if k == 2:
                    black_num += 1
                if k == 3:
                    move_poss = True  # check if any moves are left while iterating over the loop

        showboard()
        print(
            f"\n\t{symdict[1]} = {white_num}       {symdict[2]} = {black_num}\n")
        col_play = 0
        row_play = 0

        while move_poss:  # keep doing this until a valid input is given and moves are left
            print(f"{symdict[i]} - Now make your move, player-{i}:")
            play = str(input())
            if play == "exit":  # check if player wants to quit first, then see if their input is valid
                exit = True
                break
            try:
                if play[0].lower() in "abcdefgh":
                    col_play = letdict[play[0].upper()] - 1
                    if play[1] in "12345678":
                        row_play = int(play[1])-1
                        if board[row_play][col_play] == 3:
                            board[row_play][col_play] = i
                            board = flippy(board, row_play, col_play)
                            turns += 1
                            break
                        else:
                            print(
                                f"\nYou can only place a piece on the empty spaces that lead to flips. All such options are marked with '{symdict[3]}'")
                    else:
                        print(
                            "\nplease type a letter followed by an integer for a position on the board.")
                else:
                    print(
                        "\nPlease type a letter followed by an integer for a position on the board.")
            except IndexError:
                print("\nYou need to type both coordinates.")
        else:
            cleanup()
            exit = True
            print(f"Player-{i} has no valid moves left...")

        if exit or turns == 60:

            for i in range(8):  # makes sure no more possibility indicators on the board if quit
                for j in range(8):
                    if board[i][j] == 3:
                        board[i][j] = 0

            print("Here is the final board and score:\n")
            showboard()
            print(
                f"\n\t{symdict[1]} = {white_num}    {symdict[2]} = {black_num}\n")

            if white_num > black_num:  # print which player has more pieces
                print(f"\n{symdict[1]} player-1 WINS!\n")
            elif black_num > white_num:
                print(f"\n{symdict[2]} player-2 WINS!\n")
            else:
                print("\nIt's a perfect tie...? That's really rare!\n")

            while True:  # ask to play again
                print("\nWould you like to play again?\n(A) Yes    (B) No")
                try:
                    again = str(input())
                    again.lower()
                except:
                    print("Please give a valid input. There are only two options")
                    continue
                if again == "a" or again == "yes":
                    letsgo()
                    break
                elif again == "b" or again == "no":
                    final_exit = True
                    break
                else:
                    print("Please give a valid input. There are only two options")
                    continue

        if final_exit == True:
            print("\nIt was nice to have you! Byeee!\n")
            quit()


cleanup()

while True:
    print("How many players?\n(A) 1\t(B) 2\t(C) 3\n")
    players = input()
    if str(players) in "bB2":
        cleanup()
        print("Let's get started then!\nEach player just has to type the number corresponding to the position where they wish to make their mark.", end="")
        sys.stdout.flush()
        for i in range(4):
            print(".", end="")
            sleep(0.8)
            sys.stdout.flush()
        symdict = {0: "   ", 1: "[_]", 2: "###", 3: " ~ "}
        letdict = {"A": 1, "B": 2, "C": 3, "D": 4,
                   "E": 5, "F": 6, "G": 7, "H": 8}
        numdict = {v: k for k, v in letdict.items()}
        letsgo()
        break
    else:
        cleanup()
        print("We only have 2 a player game right now, sorry for the inconvenience.")
