from game_classes.human import Human


# from human import Human

class Warrior(Human):
    def __init__(self, name):
        super().__init__()

        self.name = name
   


    def heal(self):
        self.health += self.mana

        print(f"[WARRIOR] {self.name} heals for {self.mana} and now has {self.health}")


    def attack(self, target):
        print(f"[BROKEN ATTACK] {self.name} is attacking {target.name}")
# warrior1 = Warrior("legend")
# warrior2 = Warrior("Grand")

 
# warrior1.attack(warrior2)
# warrior1.heal()