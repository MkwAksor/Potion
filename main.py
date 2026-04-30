import time
from random import randint

from characters import MainCharacter
from potions import HealthPotion


START_HP: int = 10
MONEY: int = 0

mc = MainCharacter(hp=START_HP, money=MONEY)
small_hp_p = HealthPotion(duration=5, time_use=3, number_of_potion=4)


def main():
    print(f"Текущее кол-во зелий: {small_hp_p.number_of_potion}")
    
    while True:
        buy = False
        work = False

        if mc.getMoney() < 10:
            answer_1 = str(input('Хотите заработать денег? [ y / n ]: '))
            
            if answer_1 == 'y':
                mc.work()
                work = True
                
                if mc.getHp() < 1:
                    print(f"Вы погибли. Осталось монет: {mc.getMoney()}, зелий: {small_hp_p.number_of_potion}")
                    break
            else: time.sleep(1)
        
        if work == True or mc.getMoney() >= 10:
            answer_2 = str(input('Хотите купить немного зелий? [ y / n ]: '))
            
            if answer_2 == 'y':
                small_hp_p.potion_buy()
                buy = True
            else: time.sleep(1)
        
        if work == True and ((buy == True) 
                             or (small_hp_p.number_of_potion > 0)):
            print(f"Текущее кол-во зелий: {small_hp_p.number_of_potion}")
            small_hp_p.use()


if __name__ == '__main__':
    main()