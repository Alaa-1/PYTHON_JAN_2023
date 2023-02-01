from game_classes.human import Human

class Barbarian(Human):
    def __init__(self, name ):
        super().__init__()

        self.name = name
        self.strength += 50
        self.health +=10
        self.defense -=15

    def berserker_rage(self, target):
        
        target.defend(self.strength*2)
        print(f"[RAGE] {self.name} swings his weapon harming everyone")
        print(f"[RAGE] {target.name} now has {target.health} HP")


# barb = Barbarian("Rufus")

# print(barb.name)