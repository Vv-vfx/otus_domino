import random

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