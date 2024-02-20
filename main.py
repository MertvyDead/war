import random
from abstract import Warrior, Armor



class Death_knight(Warrior):
    def __init__(self, name, attack_power, health):
        super().__init__(name, attack_power, health)
        
    def death_strike(self, other_warrior):
        svmp = other_warrior.health
        other_warrior.get_damage(self)
        cvmp = svmp - other_warrior.health
        self.health += cvmp
        
class Roggue (Warrior):
    def __init__(self, name, attack_power, health):
        super().__init__(name, attack_power, health)
    def evicerate(self, other_warrior):
        other_warrior.get_damage(self)
        other_warrior.get_damage(self)
        other_warrior.get_damage(self)

la = Armor(2)
ha= Armor(3)


war = Death_knight('Arthas', 20, 100)
war1 = Roggue('Valeera',20, 100,)
war.armor = ha.armor_strenght
war1.armor = la.armor_strenght


class Battle:
    @staticmethod
    def battle(war1:Death_knight,war2:Roggue, rounds = 2):
        dsp = 0
        cp = 0 
        for i in range(rounds):
            while war1.health>0 and war2.health > 0:
                who_beat=random.randint(0,20)
                print(who_beat)
                if who_beat<=10:
                    if  dsp <= 2:
                        war1.attack(war2)
                        print(f'{war1.name} attack {war2.name} \n{war2.name} hp {war2.health}')
                        dsp += 1
                    else:
                        war1.death_strike(war2)
                        print (f'{war1.name} use death strike on {war2.name}\n{war1.name} hp:{war1.health}\n{war2.name} hp: {war2.health}')
                        dsp = 0
                else:
                    if cp <= 4:
                        war2.attack(war1)
                        print(f'{war2.name} attack {war1.name} \n{war1.name} hp {war1.health}')
                        cp+=1
                    else:
                        war2.evicerate(war2)
                        print (f'{war2.name} use evicerate on {war1.name}\n{war1.name} hp:{war1.health}')
                        cp = 0
            else:
                if war1.health<=0:
                    print(war2.name,'победилa')
                    break 
                if war2.health<=0:
                    print(war1.name,'победил')
                    break    


Battle.battle(war,war1)