import time
from random import randint

"""It's my first project, don't be too hard on me"""

START_HP: int = 10
MONEY: int = 0


class MainCharacter:
    
    def __init__(self, hp, money):
        self.hp = hp
        self.money = money
        
    def work(self):     
        money_earn = int(randint(1, 10))
        m_e = 0
        m_e_time = randint(5, 10)
        
        if money_earn == 1:
            money_earn_word = 'монете'            
        elif 2 <= money_earn <= 4:
            money_earn_word = 'монеты'            
        else:
            money_earn_word = 'монет' 
            print('Вам повезло с работой!')
        
        print(f'Вы будете работать: {m_e_time} секунд. Вы будете зарабатывать по {money_earn} {money_earn_word} в секунду')
        
        for _ in range(m_e_time):
            time.sleep(1)
            self.money += money_earn
            m_e += money_earn
        
        hp_dmg = randint(0, 8) 
        self.hp -= hp_dmg
        return print(f'Заработано: {m_e} / Потеряно здоровья: {hp_dmg} \nВсего монет: {self.money}')

mc = MainCharacter(hp=START_HP, money=MONEY)


class Potions:

    def __init__(self, duration: int,
                 time_use: int,
                 number_of_potion: int):
        self.duration = duration
        self.time_use = time_use
        self.number_of_potion = number_of_potion

    def drink(self):
        pass
    
    def potion_buy(self):
        money = mc.money
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
                    money -= 10
                    bougt_potion += 1
                    num_of_potion += 1
            
            mc.money = money
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
        
    
    def drink(self):
        health_points = mc.hp
        dur = self.duration
        
        self.number_of_potion -= 1
        print(str())
        print(f"Здоровье: {health_points}")
        
        for i in range(self.duration):
            time.sleep(.5)
            health_points += 1
            dur -= 1
            print(f"Здоровье: {health_points} / Действие зелья: {dur}")
        
        mc.hp = health_points
        

if __name__ == '__main__':
    small_hp_p = HealthPotion(duration=5, time_use=3, number_of_potion=4)

    print(f"Текущее кол-во зелий: {small_hp_p.number_of_potion}")
    
    while True:
        buy = False
        work = False

        if mc.money < 10:
            answer_1 = str(input('Хотите заработать денег? [ y / n ]: '))
            
            if answer_1 == 'y':
                mc.work()
                work = True
                
                if mc.hp < 1:
                    print(f"Вы погибли. Осталось монет: {mc.money}, зелий: {small_hp_p.number_of_potion}")
                    break
            else: time.sleep(1)
        
        if work == True or mc.money >= 10:
            answer_2 = str(input('Хотите купить немного зелий? [ y / n ]: '))
            
            if answer_2 == 'y':
                small_hp_p.potion_buy()
                buy = True
            else: time.sleep(1)
        
        if work == True and ((buy == True) 
                             or (small_hp_p.number_of_potion > 0)):
            print(f"Текущее кол-во зелий: {small_hp_p.number_of_potion}")
            small_hp_p.use()
