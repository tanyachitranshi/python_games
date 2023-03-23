def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("-" * 9)
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("-" * 9)
    print(f"{board[6]} | {board[7]} | {board[8]}")

def get_player_names():
    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    return player1, player2

def get_move(player):
    move = input(f"{player}, enter a cell number (1-9): ")
    while not move.isdigit() or int(move) < 1 or int(move) > 9:
        move = input(f"{player}, please enter a valid cell number (1-9): ")
    return int(move) - 1

def check_win(board):
    win_positions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] != ' ':
            return True
    return False

def check_tie(board):
    return ' ' not in board

def play_game():
    board = [' '] * 9
    player1, player2 = get_player_names()
    current_player, other_player = player1, player2
    while True:
        print_board(board)
        move = get_move(current_player)
        if board[move] != ' ':
            print("That cell is already occupied. Please choose another cell.")
            continue
        board[move] = 'X' if current_player == player1 else 'O'
        if check_win(board):
            print_board(board)
            print(f"Congratulations, {current_player} wins!")
            break
        if check_tie(board):
            print_board(board)
            print("The game is a tie!")
            break
        current_player, other_player = other_player, current_player

play_game()
