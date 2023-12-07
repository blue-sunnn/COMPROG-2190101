# HW1 TIC-TAC-TOE (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main()

def show_board(board):
    # show current board state on screen
    # enter your code here
    for i in range(1, (len(board) + 1)) :
        print(' ', end = '')
        if board[i - 1] == '-' :
            if i % 3 == 0 : print(str(i))
            else : print(str(i) + ' |', end = '')
        else :
            if i % 3 == 0 : print(board[i - 1])
            else : print(board[i - 1] + ' |', end = '')
        if i % 3 == 0 and i != 9 : print('---+---+---')

def available(board):
    # return a list of integer numbers indicate the available positions in current board status
    x = []
    # enter your code here
    for j in range(len(board)) :
        if board[j] == '-' : x += [j + 1]
    return x

def generate_unique_random_sequence(n, seed_value=None):
    # return a list of unique random sequence from 0 to n-1
    import random
    random.seed(seed_value)
    sequence = []
    # enter you code here
    while len(sequence) != n :
        k = random.randint(0, n - 1)
        if k not in sequence : sequence += [k]
    return sequence

def get_new_board_state(board, position, player_turn):
    # return new board state after player/computer's turn
    # enter your code here, and remove the line with 'pass'
    pos = position - 1
    if player_turn :
        board = board[:pos] + 'X' + board[pos + 1:]
    else :
        board = board[:pos] + 'O' + board[pos + 1:]
    return board

def check_win(b):
    # check whether the board status is in winning conditions
    # return 'True' if someone win, and 'False' otherwise.
    # enter your code here
    Xs, Os = 'XXX', 'OOO'
    rows = (b[:3] == Xs or b[:3] == Os)     or (b[3:6] == Xs or b[3:6] == Os)   or (b[6:] == Xs or b[6:] == Os)
    cols = (b[::3] == Xs or b[::3] == Os)   or (b[1::3] == Xs or b[1::3] == Os) or (b[2::3] == Xs or b[2::3] == Os)
    dias = (b[0::4] == Xs or b[0::4] == Os) or (b[2:8:2] == Xs or b[2:8:2] == Os)
    if (rows or cols or dias) :
        cw = True
    else :
        cw = False
    return cw

#
# DO NOT modify the code after this line
#
def get_computer_turn(board):
    b = available(board) # need to implement
    # [1, ..., 9] without positions played
    k = generate_unique_random_sequence(len(b)) # need to implement
    # select the first position k
    return b[k[0]]

def get_player_turn(board):
    b = available(board) # need to implement
    print("Player's turn")
    print('Enter: ' + str(b))
    x = int(input())
    while x not in b:
        print('Wrong input please enter: ' + str(b))
        x = int(input())
    return x

def main():
    # 1 - start with empty board
    board = '---------'
    show_board(board)  # need to implement

    # 2 - player play first
    player_turn = True
    turn = 1

    # 3 - while game is not finished
    while (turn <= 9):
        if player_turn:
            k = get_player_turn(board)
            board = get_new_board_state(board, k, True)
            show_board(board)
            if check_win(board):
                print('Player win')
                break
        else:
            k = get_computer_turn(board)
            # format color using ANSI escape sequence
            yellow_bg = '\033[30;43m'
            bold_blue = '\033[1;34m'
            bold_red = '\033[1;91m'
            normal_black = '\033[21;30m'
            normal = '\033[0m'
            print(f"{yellow_bg}Computer put {bold_blue}'O'{normal_black} at {bold_red}{k}{normal}")
            board = get_new_board_state(board, k, False)
            show_board(board)
            if check_win(board):
                print('Computer win')
                break

        # switch turn
        player_turn = not player_turn
        turn += 1

    if turn > 9:
        print('DRAW!!!')

main()