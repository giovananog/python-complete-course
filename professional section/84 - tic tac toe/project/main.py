import os

options = {
    1: 'o',
    2: 'x'
}

board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}

def draw_board(board):
    row1 = f" {board[1]} | {board[2]} | {board[3]} "
    row2 = "-----------"
    row3 = f" {board[4]} | {board[5]} | {board[6]} "
    row4 = "-----------"
    row5 = f" {board[7]} | {board[8]} | {board[9]} "

    drawn_board = f"\n\t\t\t\t{row1}\n\t\t\t\t{row2}\n\t\t\t\t{row3}\n\t\t\t\t{row4}\n\t\t\t\t{row5}\n\n"
    print(drawn_board)

def update_screen(board):
    os.system('cls')

    print("\t------------------------tic tac toe-------------------------\n\n")
    draw_board(board)

def check_if_equals(num1, num2, num3):
    return (board[num1] == board[num2]) and (board[num2] == board[num3]) and (board[num1] != " ")

def check_win():
    return (check_if_equals(1,2,3) or check_if_equals(4,5,6) or check_if_equals(7,8,9) or check_if_equals(1,4,7) or check_if_equals(2,5,8) or check_if_equals(3,6,9) or check_if_equals(1,5,9) or check_if_equals(3,5,7))

update_screen(board)

player_num = 1
game_on = True

while game_on:
    print(f"Player {player_num}'s turn")

    pos = int(input("\t\tChoose a field: "))

    if ' ' not in board.values():
        print("It's a tie!")
        game_on = False

    if board[pos] == " ":
        board[pos] = options[player_num]
        update_screen(board)

        game_on = not check_win()

        if not game_on:
            print(f"Player {player_num} won!")

        player_num = 2 if player_num == 1 else 1
