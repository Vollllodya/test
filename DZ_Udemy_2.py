import random

print('Предлагаю древнюю китайскую игру. \n Играют два игрока. \n Есть 10 палочек. \n Игроки по очереди берут от одной до трёх палочек. \n Играют до тех пор пока не закончатся палочки. \n Тот кто взял последним - тот проиграл')
player1 = input('Введите имя первого игрока: ')
player2 = input('Введите имя второго игрока: ')
last_player = player2
x = int(input(f'{player1}, {player2}, сколько вы хотите палочек в игре?'))

Monetka = random.randint(1, 2)
if Monetka == 1:
    print(f'Первым ходит {player1}')
    last_player = player2
else:
    print(f'Первым ходит {player2}')
    last_player = player1

while x > 0:
    if last_player == player1:
        try:
            y = int(input(f'{player2}, у вас есть {x} палочек, сколько вы хотите вытащить?'))
        except ValueError:
            print('Вы не ввели количество палочек!')
            continue
        if 0 < y < 4 and y <= x:
            x = x - y
            last_player = player2
            continue
        elif 0 < y < 4 and y > x:
            print(f'У Вас осталось всего {x} палочки!' if 1 < x < 4 else f'У Вас осталось всего {x} палочка!')
            continue
        else:
            print('Вытаскивать можно от одной до трех палочек')
            continue
    else:
        try:
            z = int(input(f'{player1} ,у вас есть {x} палочек, сколько вы хотите вытащить?'))
        except ValueError:
            print('Вы не ввели количество палочек!')
            continue
        if 0 < z < 4 and z <= x:
            x = x - z
            last_player = player1
            continue
        elif 0 < z < 4 and z > x:
            print(f'У Вас осталось всего {x} палочки!' if 1 < x < 4 else f'У Вас осталось всего {x} палочка!')
            continue
        else:
            print('Вытаскивать можно от одной до трех палочек')
            continue

if last_player == player1:
    print(f'Поздравляю, {player2}, вы выйграли!')
else:
    print(f'Поздравляю, {player1}, вы выйграли!')