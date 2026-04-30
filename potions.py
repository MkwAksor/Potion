import time
from random import randint


class Potions:

    def __init__(self, duration: int,
                 time_use: int,
                 number_of_potion: int):
        self.duration = duration
        self.time_use = time_use
        self.number_of_potion = number_of_potion

    def drink(self):
        pass
    
    def potion_buy(self, character):
        money = character.getMoney()
        bougt_potion = 0
        
        key_letter = int(input('Сколько зелий купить?: '))
        
        if key_letter > 0 and money >= 10:
            num_of_potion = self.number_of_potion
            
            if key_letter > 1 and money < (key_letter * 10):
                print(f'Недостаточно денег для покупки {key_letter} зелий.')
                print(f'Будет куплено максимально возможное кол-во: {(money // 10)}')
                
                while money >= 10:
                    money -= 10
                    bougt_potion += 1
                    num_of_potion += 1
                
            elif key_letter > 0 and money >= (key_letter * 10):
                for money in range(key_letter):
                    character.pay(10)
                    bougt_potion += 1
                    num_of_potion += 1
            
            self.number_of_potion = num_of_potion
            print(f'Куплено: {bougt_potion}. Всего: {self.number_of_potion}')
            
        else: print('Недостаточно монет >-<')
    
    def use(self):
        
        use_number = int(input(f"У вас {self.number_of_potion} зелий. Сколько использовать?: "))
        
        for i in range(use_number):
            if self.number_of_potion > 0:
                t_use = self.time_use
                
                print(">_< Используется: ", self.time_use, end=' ', flush=True)
                
                for j in range(self.time_use - 1):
                    time.sleep(.1)
                    t_use -= 1
                    print(t_use, end=' ', flush=True)
                    
                self.drink()
                
            else: print('Нет необходимых зелий O_O')


class HealthPotion(Potions):
    
    def __init__(self, duration, time_use, number_of_potion):
        super().__init__(duration, time_use, number_of_potion)
        
    
    def drink(self, character):
        dur = self.duration
        
        self.number_of_potion -= 1
        print(str())
        print(f"Здоровье: {character.getHp()}")
        
        for i in range(self.duration):
            time.sleep(.5)
            character.changeHp(1)
            dur -= 1
            print(f"Здоровье: {character.getHp()} / Действие зелья: {dur}")