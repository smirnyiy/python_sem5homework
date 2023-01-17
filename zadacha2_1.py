# игра против бота

from random import randint, randrange

total_sweets = int(input('Введите колличество конфет на столе: '))
print('Начало игры')
print(f'На столе лежит {total_sweets} конфет(а)')

def whos_first ():
    a = randint(0,2)
    if a == 0:
        return False
    else:
        return True


int_bot = 0
player_turn = whos_first()

while total_sweets != 0:
    if total_sweets >= 28:
        if player_turn == True:
            print('Сколько конфет возьмет первый игрок (от 1 до 28)')
            player = int(input())
            while player < 1 or player > 28:
                print ('Неверно введено количество конфет')
                player = int(input())
            total_sweets -= player
            print(f'Игрок взял {player} конфет, осталось {total_sweets} конфет')
            player_turn = False
            
        else:   
            int_bot = randrange(1, 29)
            total_sweets-=int_bot
            print(f'Компьютер взял {int_bot} конфет, осталось {total_sweets} конфет')
            player_turn = True
    else:
        if player_turn == True:
            print(f'Сколько конфет возьмет первый игрок (от 1 до {total_sweets})')
            player = int(input())
            while player < 1 or player > total_sweets:
                print ('Неверно введено количество конфет')
                player = int(input())
            total_sweets -= player
            player_turn = False
            print(f'Игрок взял {player} конфет, осталось {total_sweets} конфет')
        else:   
            int_bot = randrange(1, total_sweets+1)
            total_sweets-=int_bot
            player_turn = True
            print(f'Компьютер взял {int_bot} конфет, осталось {total_sweets} конфет')
           

if player_turn == True:
    print(f'Победил компьютер!')
    print(f'Осталось {total_sweets} конфет')
else:
    print(f'Победил первый игрок!')
    print(f'Осталось {total_sweets} конфет')
