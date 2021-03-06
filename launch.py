import random

# множество с вариантами победы
list_for_win = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7})
# множества с ходами игроков и компьютера
player1_moves = set()
player2_moves = set()
pc_moves = set()
# множество для уже занятых клеток
close_list = set()
# список для проверки, нажата ли цифра пользователем во время выбора
allow_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
x = 'X'
o = 'O'
# игровая доска
game_place = ''' ___ ___ ___   
 |1| |2| |3|
 --- --- ---
 |4| |5| |6|
 --- --- ---
 |7| |8| |9|
 --- --- ---'''


def player_game(player, allow_list, close_list, player_moves, list_for_win, symbol):
    """Алгоритм игры игрока"""
    global game_place
    player_step = input(f'''{player}, выберите номер клетки, где хотите поставить крестик!
{game_place}
:''')
    # Если не нажата цифра, то начинаем заново
    if player_step not in allow_list:
        print('Вы нажали неверный символ, попробуйте еще раз')
        return player_game(player, allow_list, close_list, player_moves, list_for_win, symbol)
    # Делаем проверку, есть ли выбор игрока в уже выбранных ходах, если нет, то добавляем в этот список
    if player_step not in close_list:
        close_list.add(player_step)
        # Меняем соответствующую клетку на X
        game_place = game_place.replace(player_step, symbol)
        # Добавляем выбор игрока в список его ходов
        player_moves.add(int(player_step))
        # Если в списке ходов есть совпадение с выигрышной комбинацией, то объявляем победителя
        if any(list(map(lambda i: player_moves.issuperset(i), list_for_win))):
            print(f'''{player}, поздравляем, вы одержали победу!
{game_place}''')
            return end_game()
        # Если количество ходов закончилось, то объявляем ничью
        if len(close_list) == 9:
            print('Ничья!')
            return end_game()
    #  Если выбор игрока в уже выбранных ходах, то рекурсивно заново запускаем функцию
    else:
        print('Вы не можете выбрать занятый квадрат! Выберите другой, пожалуйста.')
        player_game(player, allow_list, close_list, player_moves, list_for_win, symbol)


def pc_game(list_for_win, player1_moves, close_list, pc_moves, player):
    """Локика игры компьютера"""
    global game_place
    all_step = []
    # Обходим главное множество для сужения вариантов добавляя варианты относительно игрока
    for i in list_for_win:
        if i.intersection(player1_moves):
            all_step.append(i)
    # Из сортированного множество отбираем множество, относительно уже нажатых цифр
    all_step = map(lambda y: y.difference(close_list), all_step)
    available_step = []
    # Обходим победный лист удаляя нажатые ходы
    for s in all_step:
        for i in player1_moves:
            s.discard(int(i))
            available_step.append(s)
    choice_list = []
    for i in available_step:
        # Если минимальная длина списка равно одному, то сторим список вариантов
        if min(list(map(len, available_step))) == 1:
            if len(i) == 1:
                choice_list.append(i)
        # Если минимальная длина списка равно двум, то сторим список вариантов
        elif min(list(map(len, available_step))) == 2:
            if len(i) == 2:
                choice_list.append(i)
    # Рандомно выбираем один из доступных вариантов
    pc_step = str(random.choice(random.choice(list(map(list, choice_list)))))
    # Делаем проверку, есть ли выбор компьютера в уже выбранных ходах, если нет, то добавляем в этот список
    if pc_step not in close_list:
        close_list.add(pc_step)
        # Меняем соответствующюю клетку на O
        game_place = game_place.replace(pc_step, 'O')
        print('Комьютер выбрал клетку №', pc_step)
        # Добавляем выбор компьютера в список его ходов
        pc_moves.add(pc_step)
        # Если в списке ходов есть совпадение с выигрышной комбинацией, то объявляем о том, что игрок проиграл
        if any(list(map(lambda y: pc_moves.issuperset(y), list_for_win))):
            print(f'''{player}, Вы проиграли!
{game_place}''')
            return end_game()
        if len(close_list) == 9:
            print(f'''Ничья!
{game_place}''')
            return end_game()
    else:
        #  Если выбор компьютера в уже выбранных ходах, то рекурсия
        pc_game(list_for_win, player1_moves, close_list, pc_moves, player)


def end_game():
    """Конец игры"""
    input('Игра окончена! Нажмите любую клавишу, чтобы начать заново...')
    global player1_moves
    global player2_moves
    global pc_moves
    global close_list
    global game_place
    player1_moves = set()
    player2_moves = set()
    pc_moves = set()
    close_list = set()
    game_place = '''___ ___ ___
|1| |2| |3|
--- --- ---
|4| |5| |6|
--- --- ---
|7| |8| |9|
--- --- ---'''
    return start()


def start():
    """Начало игры"""
    game_select = input('''
Выберите, пожалуйста, режим игры: 
Два игрока, нажмите 2.
Одиночный режим, нажмите любую клавишу.
: ''')
    # Начало игры за двоих
    if game_select == '2':
        player1 = input('Первый игрок, введите, пожалуйста, ваше имя: ')
        player2 = input('''Спасибо! Второй игрок, введите, пожалуйста, ваше имя: ''')
        while game_select == '2':
            player_game(player1, allow_list, close_list, player1_moves, list_for_win, x)
            player_game(player2, allow_list, close_list, player2_moves, list_for_win, o)

    # Начало игры против компьютера
    else:
        player = input('Введите, пожалуйста, ваше имя: ')
        while game_select != '2':
            player_game(player, allow_list, close_list, player1_moves, list_for_win, x)
            pc_game(list_for_win, player1_moves, close_list, pc_moves, player)


print('Добро пожаловать в игру Крестики - Нолики!')
start()
