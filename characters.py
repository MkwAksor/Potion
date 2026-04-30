import time
from random import randint


class Character:
    
    def __init__(self, hp, money):
        self.hp = hp
        self.money = money
        
    def getHp(self):
        return self.hp
    
    def getMoney(self):
        return self.money
    
    def changeHp(self, points):
        self.hp += points


class MainCharacter(Character):
    
    def __init__(self, hp, money):
        super().__init__(hp, money)
        
    def pay(self, amount):
        self.money -= amount
        
    def income(self, amount):
        self.money += amount
        
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
            self.income(money_earn)
            m_e += money_earn
        
        hp_dmg = randint(1, 8)
        self.changeHp(-(hp_dmg))
        return print(f'Заработано: {m_e} / Потеряно здоровья: {hp_dmg} \nВсего монет: {self.getMoney()}')