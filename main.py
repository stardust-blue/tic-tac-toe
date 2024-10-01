import sys


def create_board():
    return [[None, None, None], [None, None, None], [None, None, None]]


def render(board: list[list[None]]):
    print("  0 1 2")
    for row in range(3):
        print(
            str(row)
            + " "
            + " ".join([cell if cell is not None else "." for cell in board[row]]),
        )


def get_move():
    try:
        x = int(input("Your move (x): "))
        y = int(input("Your move (y): "))
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    coords = (x, y)
    return coords


def is_valid_move(board: list[list[any]], coords: tuple[int, int]):
    if board[coords[1]][coords[0]] is not None:
        return False
    else:
        return True


def make_move(old_board: list[list[any]], coords: tuple[int, int], player):
    new_board = old_board
    new_board[coords[1]][coords[0]] = player
    return new_board


def get_winner(board: list[list[any]]):
    lines = set()

    for row in range(3):
        lines.add(frozenset(board[row]))
    for col in range(3):
        lines.add(frozenset(board[rows][col] for rows in range(3)))

    lines.add(frozenset(board[index][index] for index in range(3)))
    lines.add(frozenset(board[index][2 - index] for index in range(3)))

    for line in lines:
        if len(line) == 1:
            return next(iter(line))
    return None


def check_draw(board: list[list[any]]):
    flag = True

    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                flag = False
                break

    return flag


def main():
    board = create_board()

    player = {1: "X", -1: "O"}
    move_coords = None
    turn = 1
    while True:
        move_coords = get_move()
        if is_valid_move(board, move_coords):
            board = make_move(board, move_coords, player[turn])
            render(board)
            turn *= -1
            winner = get_winner(board)
            if winner is not None:
                print(winner + " wins!")
                break
            elif check_draw(board):
                print("Draw!")
                break
        else:
            print("Illegal move")


if __name__ == "__main__":
    main()
