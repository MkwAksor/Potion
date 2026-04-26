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
    
    def potion_buy(self):
        pass
    
    def use(self):
        global drink
        
        use_number = int(input(f"У вас {self.number_of_potion}. Сколько зелий использовать?: "))
        
        for _ in range(use_number):
            if self.number_of_potion > 0:
                t_use = self.time_use
                
                print(">_< Используется: ", self.time_use, end=' ', flush=True)
                
                for using in range(self.time_use):
                    time.sleep(.1)
                    t_use -= 1
                    print(t_use, end=' ', flush=True)
                    
                self.drink()
                
            else: print('Нет необходимых зелий O_O')
    
class HealthPotion(Potions):
    
    def __init__(self, duration, time_use, number_of_potion):
        super().__init__(duration, time_use, number_of_potion)
        
    
    def drink(self):
        global health_points
        hp_p_dur = self.duration
        
        self.number_of_potion -= 1
        print(str())
        print(f"Здоровье: {health_points}")
        
        for sec in range(self.duration):
            time.sleep(.5)
            health_points += 1
            hp_p_dur -= 1
            print(f"Здоровье: {health_points} / Действие зелья: {hp_p_dur}")
            
    def potion_buy(self):
        global money
        bougt_hp_potion = 0
        
        key_letter = int(input('Сколько зелий купить?: '))
        
        if key_letter > 0 and money >= 10:
            num_of_potion = self.number_of_potion
            
            if key_letter > 1 and money < (key_letter * 10):
                print(f'Недостаточно денег для покупки {key_letter} зелий.')
                print(f'Будет куплено максимально возможное кол-во: {(money // 10)}')
                
                while money >= 10:
                    money -= 10
                    bougt_hp_potion += 1
                    num_of_potion += 1
                
            elif key_letter > 0 and money >= (key_letter * 10):
                for money in range(key_letter):
                    money -= 10
                    bougt_hp_potion += 1
                    num_of_potion += 1
            
            self.number_of_potion = num_of_potion
            print(f'Куплено: {bougt_hp_potion}. Всего: {self.number_of_potion}')
            
        else: print('Недостаточно монет >-<')

def money_earning():
    global money
    
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
        money += money_earn
        m_e += money_earn
        
    return print(f'Заработано: {m_e} \nВсего: {money}')


if __name__ == '__main__':
    health_points = int(10)
    money = int(5)
    health_potion = HealthPotion(duration=20, time_use=15, number_of_potion=4)

    print(f"Текущее кол-во зелий: {health_potion.number_of_potion}")
    
    while True:
        buy = False
        work = False

        answer_1 = str(input('Хотите заработать денег? [ y / n ]: '))
            
        if answer_1 == 'y':
            money_earning()
            work = True
        
        if work == True:
            answer_2 = str(input('Хотите купить немного зелий? [ y / n ]: '))
            
            if answer_2 == 'y':
                health_potion.potion_buy()
                buy = True
        
        if work == True and buy == True:
            health_potion.use()
