import random
# множество с вариантами победы
list_for_win = ({1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7})
# множества с ходами игроков и компьютера
player1_moves = set()
player2_moves = set()
pc_moves = set()
# множество для уже занятых клеток
close_list = set()
# список для проверки нажата ли цифра пользователем во время выбора
allow_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# игровая доска
game_place = ''' ___ ___ ___
 |1| |2| |3|
 --- --- ---
 |4| |5| |6|
 --- --- ---
 |7| |8| |9|
 --- --- ---'''
# Начало игры
game_select = int(input('''Добро пожаловать в игру Крестики - Нолики!
Выберите, пожалуйста, режим игры: 
Одиночный режим, нажмите 1.
Два игрока, нажмите 2.
: '''))


# Функция для удержания окна в py installer после окончания игры
def end_game():
    end = input('Игра окончена! ')
    if end:
        return


# Начало игры за двоих
if game_select == 2:
    player1 = input('Первый игрок, введите, пожалуйста, ваше имя: ')
    player2 = input('''Спасибо! Второй игрок, введите, пожалуйста, ваше имя: ''')

# Алгоритм обрабтки ходов первого игрока
    def player1_game():
        global game_place
        player1_step = input(f'''{player1}, выберите номер клетки, где хотите поставить крестик!
{game_place}
:''')
        # Если не нажата цифра, то начинаем заново
        if player1_step not in allow_list:
            print('Вы нажали неверный символ, попробуйте еще раз')
            return player1_game()
        # Делаем проверку, есть ли выбор игроку в уже выбранных ходах, если нет, то добавляем в этот список
        if player1_step not in close_list:
            close_list.add(player1_step)
            # Меняем соответствующюю клетку на X
            game_place = game_place.replace(player1_step, 'X')
            # Добавляем выбор игрока в список его ходов
            player1_moves.add(int(player1_step))
            # Если в списке ходов есть совпадение с выигрышной комбинацией, то объявляем победителя
            if any(list(map(lambda i: player1_moves.issuperset(i), list_for_win))):
                print(f'''{player1}, поздравляем, вы одержали победу!
{game_place}''')
                return end_game()
            # Если количество ходов закончилось, то объявляем ничью
            if len(close_list) == 8:
                print('Ничья!')
                return end_game()
        #  Если выбор игроку в уже выбранных ходах, то рекурсивно заново запускаем функцию
        else:
            print('Вы не можете выбрать занятый квадрат! Выберите другой, пожалуйста.')
            player1_game()
        # Если нет победы либо ничьи, то передаем ход другому
        return player2_game()

    # Алгоритм обрабтки ходов второго игрока
    def player2_game():
        global game_place
        player2_step = input(f'''{player2}, выберите номер клетки, где хотите поставить нолик!
{game_place}
:''')
        # Если не нажата цифра, то начинаем заново
        if player2_step not in allow_list:
            print('Вы нажали неверный символ, попробуйте еще раз')
            return player1_game()
        # Делаем проверку, есть ли выбор игроку в уже выбранных ходах, если нет, то добавляем в этот список
        if player2_step not in close_list:
            close_list.add(player2_step)
            # Меняем соответствующюю клетку на X
            game_place = game_place.replace(player2_step, 'O')
            # Добавляем выбор игрока в список его ходов
            player2_moves.add(int(player2_step))
            # Если в списке ходов есть совпадение с выигрышной комбинацией, то объявляем победителя
            if any(list(map(lambda i: player2_moves.issuperset(i), list_for_win))):
                print(f'''{player2}, поздравляем, вы одержали победу!
{game_place}''')
                return end_game()
            # Если количество ходов закончилось, то объявляем ничью
            if len(close_list) == 8:
                print('Ничья!')
                return end_game()
        #  Если выбор игроку в уже выбранных ходах, то рекурсивно заново запускаем функцию
        else:
            print('Вы не можете выбрать занятый квадрат! Выберите другой, пожалуйста.')
            player2_game()
        # Если нет победы либо ничьи, то передаем ход другому
        return player1_game()

# Триггер для запуска игры за двоих
    player1_game()
# _____________________________________________________________________________________________________________________________________________________________
# Начало игры против компьютера
else:
    player1 = input('Введите, пожалуйста, ваше имя: ')

# Алгоритм обработки ходов игрока
    def player1_game():
        global game_place
        player1_step = input(f'''{player1}, выберите номер клетки, где хотите поставить крестик!
{game_place}
:''')
        # Если не нажата цифра, то начинаем заново
        if player1_step not in allow_list:
            print('Вы нажали неверный символ, попробуйте еще раз')
            return player1_game()
        # Делаем проверку, есть ли выбор игроку в уже выбранных ходах, если нет, то добавляем в этот список
        if int(player1_step) not in close_list:
            close_list.add(int(player1_step))
            # Меняем соответствующюю клетку на X
            game_place = game_place.replace(player1_step, 'X')
            # Добавляем выбор игрока в список его ходов
            player1_moves.add(int(player1_step))
            # Если в списке ходов есть совпадение с выигрышной комбинацией, то объявляем победителя
            if any(list(map(lambda i: player1_moves.issuperset(i), list_for_win))):
                print(f'''{player1}, поздравляем, вы одержали победу!
{game_place}''')
                return end_game()
            # Если количество ходов закончилось, то объявляем ничью
            if len(close_list) == 8:
                print('Ничья!')
                return end_game()
        #  Если выбор игроку в уже выбранных ходах, то рекурсивно заново запускаем функцию
        else:
            print('Вы не можете выбрать занятый квадрат! Выберите другой, пожалуйста.')
            player1_game()
        # Если нет победы либо ничьи, то передаем ход другому
        return pc_game()

    # Локика игры компьютера
    def pc_game():
        global game_place
        pc_step = []
        # Обходим главное множество для сужения вариантов добавляя варианты относительно игрока
        for i in list_for_win:
            if i.intersection(player1_moves):
                pc_step.append(i)
        # Из сортированного множество отбираем множество, относительно уже нажатых цифр
        pc_step = map(lambda y: y.difference(close_list), pc_step)
        # Все множества внутри списка меняем на списки для дальнейшей работы
        pc_step = list(map(list, pc_step))
        # Если минимальная длина множество равно двум, то
        if min(list(map(len, pc_step))) == 2:
            # Среди списков внутри списка рандомно выбираем одну цифру
            pc_step = random.choice(random.choice(list(map(list, pc_step))))
        else:
            # иначе создаем промежуточное множество из элементов pc_step
            temp_list = set()
            for m in pc_step:
                for n in m:
                    temp_list.add(n)
# Данная часть кода была самым тяжелым, поэтому названия переменных пришлось брать просто буквами для экономии времени
            # Объединяем множество ходов игрока и множество доступных ходов, это даст варинты для его победы
            b = player1_moves.union(temp_list)
            # Из всех вариантов победы, через цикл отбираем реальные варианты победы
            for s in list_for_win:
                if s.issubset(b) and bool(s.intersection(temp_list)):
                    t = s.intersection(temp_list)
                # Если выбранный вариант не в списке уже выбранных ходов и это одно цифра, то окончательон выбираем его
                    if t not in close_list and len(t) == 1:
                        t = list(map(int, t))
                        pc_step = t[0]
        # Если в цикле не удалось выбрать лучший вариант, то выбираем ход для компьютера рандомно из множество доступных
            if type(pc_step) is list:
                pc_step = random.choice(list(temp_list))
        # Делаем проверку, есть ли выбор компьютера в уже выбранных ходах, если нет, то добавляем в этот список
        if pc_step not in close_list:
            close_list.add(pc_step)
            # Меняем соответствующюю клетку на O
            game_place = game_place.replace(str(pc_step), 'O')
            print('Комьютер выбрал клетку №', pc_step)
            # Добавляем выбор компьютера в список его ходов
            pc_moves.add(pc_step)
            # Если в списке ходов есть совпадение с выигрышной комбинацией, то объявляем о том, что игрок проиграл
            if any(list(map(lambda y: pc_moves.issuperset(y), list_for_win))):
                print(f'''{player1}, Вы проиграли!
{game_place}''')
                return end_game()
            if len(close_list) == 8:
                print(f'''Ничья!
{game_place}''')
                return end_game()
        else:
            #  Если выбор компьютера в уже выбранных ходах, то рекурсивно заново запускаем функцию
            print('Вы не можете выбрать занятый квадрат! Выберите другой, пожалуйста.')
            pc_game()
        # Если нет победы либо ничьи, то передаем ход игроку
        return player1_game()

# триггер запуска одиночного режима
    player1_game()
