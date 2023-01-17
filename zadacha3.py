# Создайте программу для игры в ""Крестики-нолики"".

import random
import os

def print_array(field):   #игровое поле крестиков-ноликов
    os.system('cls')
    for i in range(1, 10):
        print(f"{field[i - 1]} ", end="")
        if not i%3: print()

def filling(array, array_ex, set): 
    x = int(input("Выберете клетку: "))
    if x in array_ex:
        for i in range(len(array)):
            if array[i] == x:
                if set: array[i] = "X"
                else: array[i] = "O"
        array_ex.remove(x)
    else:
        print("Поле занято, или вы вышли за границы игрового поля")
        filling(array, array_ex, set)
        

def win_set(array): 
    if (array[0] == array[1] == array[2] or
     array[3] == array[4] == array[5] or
     array[6] == array[7] == array[8] or
     array[0] == array[3] == array[6] or
     array[1] == array[4] == array[7] or
     array[2] == array[5] == array[8] or
     array[0] == array[4] == array[8] or
     array[2] == array[4] == array[6]) :
        return True
    else:
        return False
        

def play(array, array_ex, set):  
    print_array(array)
    if array_ex == []:
        print("Победила Дружба!")
        return
    
    if set:
        player = "1-й"
    else: 
        player = '2-й'
    print(f"Ходит {player} игрок")
    
    filling(array, array_ex, set)
    
    if win_set(array):
        print_array(array)
        print(f"Выиграл {player} игрок \n GAME OVER")
        return
    play(array, array_ex, not set)

field = [int(i) for i in range(1, 10)]      
field_ex = [int(i) for i in range(1, 10)] 

set = random.randint(0,1)
play(field, field_ex, set)

