class Warrior():
    def __init__(self, name, dmg,health):
        self.name = name    
        self.health = health
        self.attack_power = dmg
        self.armor = 0
    
    def show_cr_info(self):
        inf= (f'{self.name} Здоровье: {self.health}')
        print(inf)
    def attack (self, other_warrior):
        other_warrior.get_damage(self)
    def get_damage(self, other_warrior):
        self.health-=(other_warrior.attack_power - self.armor)

    def new_hp(self, new_health):
        self.health = new_health
    def reset_hp(self):
        self.health = 100
        
class Armor(): 
    def __init__(self, armor_strenght) -> None:
        self.armor_strenght = armor_strenght