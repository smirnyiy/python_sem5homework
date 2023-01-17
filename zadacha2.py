# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?

from random import randint as r


def correct_value(value, player):
    result = input(f'\n{player}, твоя очередь брать конфеты: ')
    while not result.isdigit() or not (29 > int(result) > 0) or int(result) > value:
        if value >= 28:
            result = input(f'{player}, можно вводить значения только от 1 до 28: ')
        else:
            result = input(f'{player}, можно вводить значения только от 1 до {value}: ')
    return int(result)


def player_init():
    player = input('\nВведите ваше имя: ')
    return player


def players_draw(player):
    draw = r(1, 2)
    if draw == 1:
        print(f'\nТебе повезло, {player}. По результатам жеребьевки ты ходишь первым!')
        return 1
    else:
        print(f'\nПо результатам жеребьевки первым ходит "Bot". Сдавайся!')
        return 2


def game_candies(value, player, turn):
    save_value = value
    one_time_print = 0
    while value > 0:
        if turn == 1:
            move = correct_value(value, player)
            value -= move
            if value == 0:
                print(f'\n{player} ПОБЕДИЛ!!!')
                break
            print(f'\nОсталось конфет: {value}\n')
            turn = 2
        if turn == 2:
            if save_value == value:
                move = value % 29
                one_time_print += 1
            elif value == value - value % 29:
                if save_value == value + save_value % 29:
                    print('Bot: Хороший ход!')
                if value == 29:
                    print('Bot: Так не честно!!!')
                move = r(1, 28)
            elif value % 29 != 0:
                if one_time_print == 0:
                    print('Bot: Ты упустил свой шанс! Сдавайся!')
                move = value % 29
                one_time_print += 1             
            print(f'Bot взял конфеты в колличестве: {move}')
            value -= move                                   
            if value == 0:
                print(f'ПОБЕДИТЕЛЬ Bot !!!')
                break
            print(f'\nОсталось конфет: {value}')
            turn = 1


# count_candies = input('Введите колличество конфет на столе: ')
print('!!!ИГРА В КОНФЕТЫ!!!')
print('Брать со стола можно от 1 до 28 конфет за раз')
print('Кто последний делает ход - тот победил!')

count_candies = int(input('Введите колличество конфет на столе: '))

player = player_init()
turn = players_draw(player)
print(f'\nКолличество конфет на столе: {count_candies}')
game_candies(count_candies, player, turn)