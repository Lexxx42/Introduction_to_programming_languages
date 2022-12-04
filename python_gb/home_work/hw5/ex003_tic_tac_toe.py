# * 3. Создайте программу для игры в "Крестики-нолики". Поле 3x3. Игрок - игрок, без бота.
# Эмодзи


def current_board(board: list) -> None:
    print('-' * 34)
    for i in range(3):
        print('|', ' ', board[0 + i * 3], '\t', '|', ' ', board[1 + i * 3], '\t', '|', ' ', board[2 + i * 3], '\t', '|')
        print('-' * 34)


def take_input(sign: str, board: list) -> None:
    valid = False
    while not valid:
        select_cell = input('Where to place' + sign + '? ')
        try:
            select_cell = int(select_cell)
        except:
            print('Incorrect input! Input must be a number')
            continue
        if 1 <= select_cell <= 9:
            if str(board[select_cell - 1]) not in ['\U0000274C', '\U00002B55']:
                board[select_cell - 1] = sign
                valid = True
            else:
                print('Choose another cell')
        else:
            print('Incorrect input! Input must be [1, 9]')


def check_win(board: list) -> bool:
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def form_board(board: list) -> None:
    steps = 0
    win = False
    while not win:
        current_board(board)
        if steps % 2 == 0:
            take_input('\U0000274C', board)
        else:
            take_input('\U00002B55', board)
        steps += 1
        if steps > 4:
            tmp = check_win(board)
            if tmp:
                print(tmp, 'Wins! \U0001F9BE')
                win = True
                break
        if steps == 9:
            print('Draw \U0001F610')
            break
    current_board(board)


def main() -> None:
    print("Oh, god! It's a tic-tac-toe game \U0001F525")
    board = list(range(1, 10))
    form_board(board)


if __name__ == '__main__':
    main()
