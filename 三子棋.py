import os
from time import *

chess = "O"
play_time = 0


def show_board():
    for i in board:
        print("".join(i))


board = [["-" for _ in range(3)] for i in range(3)]
while True:

    def play(i1, i2, chess):
        if board[i1][i2] == "-":
            board[i1][i2] = chess
        else:
            w = "选择无效"
            print(w)


    show_board()
    print(chess + "下棋")
    row = input("你要下在第几行")
    row = int(row) - 1
    col = input("你要下在第几列")
    col = int(col) - 1
    play(row, col, chess)
    sleep(0.8)
    os.system("cls")
    if chess == "O":
        chess = "X"
    else:
        chess = "O"
    if (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (
            board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (
            board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O") or (
            board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (
            board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
        print("O获胜")
        show_board()
        break
    if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (
            board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (
            board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X") or (
            board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (
            board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
        print("X获胜")
        show_board()
        break
    play_time += 1
    if play_time == 9:
        print("平局")
        show_board()
        break
