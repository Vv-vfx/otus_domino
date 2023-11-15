import random


class Card:

    def __init__(self):
        self._rows_count = 3
        self._columns_count = 9
        self._numbers_count = (1, 91)
        self._numbers_in_line_count = 5
        self._all_numbers : set = None
        self._card_numbers: list = None

        self._create_card()

    def _create_card(self):
        
        self._card_numbers = list()
        self._all_numbers = set()


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