# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока 
# делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего 
# конкурента?


# человек против человека


from random import randint

value = int(input('Введите колличество конфет на столе: '))
print('Начало игры')
print(f'На столе лежит {value} конфет(а)')

def input_dat(name):
    x = int(input(f"Сколько конфет возьмет игрок {name} (от 1 до 28): "))
    while x < 1 or x > 28:
        x = int(input(f"Неверно введено количество конфет "))
    return x

def p_print(name, k, counter, value):
    print(f"Игрок {name} взял {k}, теперь у него {counter}, на столе осталось {value} конфет.")

player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
#value = 201
flag = randint(0,2)
if flag:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

counter1 = 0 
counter2 = 0

while value != 0:
    if flag:
        k = input_dat(player1)
        counter1 += k
        value -= k
        flag = False
        p_print(player1, k, counter1, value)
    else:
        k = input_dat(player2)
        counter2 += k
        value -= k
        flag = True
        p_print(player2, k, counter2, value)

if flag:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")