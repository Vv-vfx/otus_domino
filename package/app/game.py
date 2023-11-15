import sys

from service.gamer import Gamer
from service.bag import Bag

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



            








    