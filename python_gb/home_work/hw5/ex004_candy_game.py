# ** 4. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
#
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота "интеллектом"

from random import randint

print('Candy game!')


def game_info(mode: int) -> None:
    if mode not in [1, 0]:
        print('Input is incorrect! Must be in [0, 1]')
        start()
    elif mode == 0:
        player_1 = 'xxxNogibator2015xxx'
        player_2 = 'sunOfTheBeach'
        candies = 2021
        who_start = bool(randint(0, 1))
        quantity_candies_1 = 0
        quantity_candies_2 = 0
        if who_start:
            print(f'First move from {player_1}')
        else:
            print(f'First move from {player_2}')
        while candies > 28:
            if who_start:
                taken_candies = take_candies(player_1)
                quantity_candies_1 += taken_candies
                candies -= taken_candies
                who_start = False
                result(player_1, taken_candies, quantity_candies_1, candies)
            else:
                taken_candies = take_candies(player_2)
                quantity_candies_2 += taken_candies
                candies -= taken_candies
                who_start = True
                result(player_2, taken_candies, quantity_candies_2, candies)


def result(player_name: str, candies_taken: int, candies_of_player: int, candies_left: int):
    print(
        f'Player {player_name} took {candies_taken}, and now have '
        f'{candies_of_player} candies. Candies left: {candies_left}')


def take_candies(player_name: str) -> int:
    candy = int(input(f'How much candies {player_name}, do you want to take? [1, 28]: '))
    while 1 > candy or candy > 28:
        candy = int(input('Quantity must be in [1, 28]: '))
    return candy


def start() -> None:
    mode = int(input('Enter 0 to play with the person and 1 to play with bot: '))
    game_info(mode)


start()
