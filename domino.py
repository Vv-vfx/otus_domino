import random, sys

class Card:

    def __init__(self):
        self._rows_count = 3
        self._columns_count = 9
        self._numbers_count = (1, 91)
        self._numbers_in_line_count = 5
        self._all_numbers = set()
        self._card_numbers = []

        self._create_card()

    def _create_card(self):
        
        # список всех возможных чисел
        all_numbers = list(range(*self._numbers_count))

        # идем по количеству строк
        for _ in range(self._rows_count):
            
            # выбираем 5 случайных
            selected_numbers = sorted(random.sample(all_numbers, k=self._numbers_in_line_count), reverse=True)
            # добавляем в множество всех чисел на карточке
            self._all_numbers.update(selected_numbers)

            # удаляем пять случайных из общего списка чисел
            for number in selected_numbers:
                all_numbers.remove(number)
            
            # готовим линию для заполнения с 1 и 0
            line = [1] * self._numbers_in_line_count + ([0] * (self._columns_count - self._numbers_in_line_count))
            random.shuffle(line)

            # заполняем линию выбранными числами
            for index, value in enumerate(line[:]):
                if value:
                    line[index] = selected_numbers.pop()


            # добавляем линию в карточку
            self._card_numbers.append(line)
            
    def cross_out_number(self, number):
        """Проверяем есть ли число в карточке"""

        # проверяем на наличие числа в карточке
        if number not in self._all_numbers:
            return 'not number in card'
        
        # удаляем число из общего списка
        self._all_numbers.remove(number)
        
        # зачеркиваем число в карточке
        self._fill_number_dash(number)

        # проверяем, не зачеркнуты ли все числа в карточке
        if len(self._all_numbers) == 0:
            return 'victory'
        
        return 'continue play' 

    def _fill_number_dash(self, number):
        ''' Зачеркиваем число в карточке - меняем на "--" '''
        
        # идем по линиям карточки
        for line_index, line in enumerate(self._card_numbers):
            # идем по цифрам
            for number_index, value in enumerate(line[:]):
                    if value == number:
                        # зачеркиваем число в карточке
                        self._card_numbers[line_index][number_index] = '--'
                        


    def __str__(self):
        
        temp = []

        for row in self._card_numbers:
            
            for number in row:
                if number == 0:
                    temp.append('  '.rjust(3))
                else:
                    temp.append(str(number).rjust(3))
            else:
                temp.append('\n' )

        temp.pop()

        str_card = ''.join(temp)

        return str_card
    

class Bag:

    def __init__(self):
        self._barrels_count = 90
        self._barrels = None
        
        self._fill_bag()
    
    def _fill_bag(self):

        self._barrels = [i for i in range(1,91)]

    def get_barrel(self):

        barrel = random.choice(self._barrels)
        self._barrels.remove(barrel)
        self._barrels_count -= 1
        print(f'Новый бочонок: {barrel}. Осталось {self._barrels_count}')

        return barrel


class Gamer:

    def __init__(self, name, role):
        self.gamer_name = name
        self.role = role
        self.card = Card()

    def pr_card(self):

        line = self.card._columns_count * 3
        text = f'Карточка: {self.gamer_name}'
        print(f"{text:{'-'}^{line}}")
        print(self.card)
        print('-'* line)

    def cross_out_number(self, number):

        if self.role == 'human':
            return self._cross_out_number_human(number)
        else:
            return self._cross_out_number_cpu(number)

            
    def _cross_out_number_human(self, number):

        self.pr_card()
        unswer = input(f"Зачеркнуть число {number}? (y/n) ")
        
        if unswer == 'y':
            card_back = self.card.cross_out_number(number)
            
            if card_back == 'victory':
                print(f'Игрок {self.gamer_name} зачеркивает число {number}!')
                print()
                return 'victory'
            elif card_back == 'not number in card':
                print(f'Игрок {self.gamer_name} хотел смухлевать но не вышло. Он проиграл.')
                print()
                return "lost"
            elif card_back == "continue play":
                print(f'Игрок {self.gamer_name} зачеркивает число {number}!')
                print()
                return "continue play"
       
        elif unswer == 'n':
            card_back = self.card.cross_out_number(number)
            if card_back == 'victory' or card_back == 'continue play':
                print(f'Ты хочешь поддаваться? Ты не зачеркнул {number}! Поэтому ты проиграл!')
                print()
                return 'lost'
            elif card_back == 'not number in card':
                print(f'Правильно, зачеркивать нечего, в карточке нет {number}')
                print()
                return "continue play"
            
    def _cross_out_number_cpu(self, number):
        
        print(f"Игроку {self.gamer_name} надо зачеркнуть число {number}:")
        self.pr_card()
        
        card_back = self.card.cross_out_number(number)
        
        if card_back == 'victory':
            print(f'Игрок {self.gamer_name} зачеркивает число {number}!')
            print()
            return 'victory'
        elif card_back == "continue play":
            print(f'Игрок {self.gamer_name} зачеркивает число {number}!')
            print()
            return "continue play"
        elif card_back == "not number in card":
            print(f'У игрока {self.gamer_name} нет в карточке числа {number}, поэтому ход следующего игрока!')
            print()
            return "continue play"
        
    
    def __str__(self):

        return self.gamer_name


class Game:

    def __init__(self):
        self.gamers_count = None
        self.gamers_list : list[Gamer,] = []
        self.bag = Bag()
        
        self._setup_gamers()

    def _setup_gamers(self):

        while True:
            gamers_count = input('Сколько будет игроков? (или exit): ')
            if gamers_count.lower() == 'exit':
                sys.exit()
            elif gamers_count.isdigit():
                gamers_count = int(gamers_count)
                if gamers_count >= 2:
                    break
                else:
                    print("Должно быть минимум 2 игрока")
            
            print('Некорректный ввод')


        for gamer_number in range(1, gamers_count + 1):
            role = input(f'Введите роль игрока номер {gamer_number} (1 - Человек, 2 - Компьютер) ')
            if role == '1':
                gamer_name = input(f'Введите имя игрока номер {gamer_number} ')
                gamer_role = "human"
            else:
                gamer_name = f"CPU_{gamer_number}"
                gamer_role = "cpu"
            
            self.gamers_list.append(Gamer(gamer_name, gamer_role))  
    
    def game_start(self):
        
        stop_game_codes = {
            1: "Есть победители, завершаем игру",
            2: "Остался один игрок, засчитываем автоматическую победу",
            3: "Все проиграли",
        }
        
        lost_gamers = []
        victory_gamers = []

        while True:
                        
            # достаем бочонок
            burrel = self.bag.get_barrel()

            # проходим по всем игрокам и зачеркиваем числа
            for index_gamer, gamer in enumerate(self.gamers_list[:]):
                if gamer != 'lost': 
                    cross_out_number_result = gamer.cross_out_number(burrel)
                
                    if cross_out_number_result == 'lost':
                        self.gamers_list.remove(gamer)
                        lost_gamers.append(gamer.gamer_name)

                    elif cross_out_number_result == 'victory':
                        victory_gamers.append(gamer.gamer_name)


            # проверяем результаты
            if victory_gamers:
                # stop_game_code = 1
                if len(victory_gamers) == 1:
                    print(f'Победитель: {victory_gamers[0]}')
                elif len(victory_gamers) > 1:
                    print(f'Победители: {",".join(victory_gamers)}')
                break

            elif len(self.gamers_list) == 1:
                # stop_game_code = 2
                print(f'Все игроки, кроме одного, проиграли!')
                print(f'Победитель: {self.gamers_list[0]}')
                break
            
            elif not self.gamers_list:
                # stop_game_code = 2
                print(f'Все проиграли!')
                break

if __name__ == "__main__":

    game = Game()
    game.game_start()



            








    