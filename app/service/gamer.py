from service.card import Card


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