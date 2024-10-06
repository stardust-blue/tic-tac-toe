import sys
import random


def get_mode() -> bool:
    try:
        mode = str(input("(M)anual or (A)utomatic?: ")).lower()
        while mode != "m" and mode != "a":
            print("That's not a valid mode!")
            mode = str(input("(M)anual or (A)utomatic?: ")).lower()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    return True if mode == "m" else False


def get_names() -> dict[int:str]:
    player_name = {}
    try:
        player_name[1] = input("Name of player (X): ").capitalize()
        player_name[-1] = input("Name of player (O): ").capitalize()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    return player_name


def create_board() -> list[list[any]]:
    return [[None, None, None], [None, None, None], [None, None, None]]


def render(board: list[list[any]]):
    print("  " + " ".join("012"))
    for row in range(3):
        print(
            str(row)
            + " "
            + " ".join([cell if cell is not None else "." for cell in board[row]]),
        )


def get_move(player_name) -> tuple[int, int]:
    try:
        x = int(
            input(
                "X coordinate for player {cur_player}: ".format(cur_player=player_name)
            )
        )
        y = int(
            input(
                "Y coordinate for player {cur_player}: ".format(cur_player=player_name)
            )
        )
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit()
    return (x, y)


def is_valid_move(board: list[list[any]], coords: tuple[int, int]) -> bool:
    if board[coords[0]][coords[1]] is not None:
        return False
    else:
        return True


def make_move(
    board: list[list[any]], coords: tuple[int, int], player
) -> list[list[any]]:
    board[coords[0]][coords[1]] = player
    return board


def get_winner(board: list[list[any]]) -> int:
    lines = set()

    for row in range(3):
        lines.add(frozenset(board[row]))
    for col in range(3):
        lines.add(frozenset(board[rows][col] for rows in range(3)))

    lines.add(frozenset(board[index][index] for index in range(3)))
    lines.add(frozenset(board[index][2 - index] for index in range(3)))

    for line in lines:
        if len(line) == 1:
            winner = next(iter(line))
            if winner == "X":
                return 1
            elif winner == "O":
                return -1
    return None


def check_draw(board: list[list[any]]) -> bool:
    flag = True

    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                flag = False
                break

    return flag


def random_move(board: list[list[any]]) -> tuple[int, int]:
    x, y = random.randint(0, 2), random.randint(0, 2)
    while board[x][y] is not None:
        x, y = random.randint(0, 2), random.randint(0, 2)
    return (x, y)


def manual_mode():
    board = create_board()
    player_symbol = {1: "X", -1: "O"}
    player_name = get_names()
    turn = 1

    while True:
        render(board)

        move_coords = get_move(player_name[turn])
        if is_valid_move(board, move_coords):
            board = make_move(board, move_coords, player_symbol[turn])
            render(board)
            turn *= -1

            winner = get_winner(board)
            if winner is not None:
                print("Congratulations! " + player_name[winner] + " wins!")
                break
            elif check_draw(board):
                print("Draw!")
                break
        else:
            print("Illegal move")


def automatic_mode():
    board = create_board()
    player_symbol = {1: "X", -1: "O"}
    player_name = str(input("Name of player: ")).capitalize()

    render(board)
    while True:
        move_coords = get_move(player_name)
        if is_valid_move(board, move_coords):
            board = make_move(board, move_coords, player_symbol[1])
            render(board)

            winner = get_winner(board)
            if winner == 1:
                print("Congratulations! " + player_name + " wins!")
                break
            elif winner == -1:
                print(
                    "{current_name} lost! How unfortunate!".format(
                        current_name=player_name
                    )
                )
                break
            elif check_draw(board):
                print("Draw!")
                break

        board = make_move(board, random_move(board), player_symbol[-1])
        print("AI has moved")

        render(board)
        winner = get_winner(board)
        if winner == 1:
            print("Congratulations! " + player_name + " wins!")
            break
        elif winner == -1:
            print(
                "{current_name} lost! How unfortunate!".format(current_name=player_name)
            )
            break
        elif check_draw(board):
            print("Draw!")
            break


def main():
    mode = get_mode()

    if mode:
        manual_mode()
    else:
        automatic_mode()


if __name__ == "__main__":
    main()
