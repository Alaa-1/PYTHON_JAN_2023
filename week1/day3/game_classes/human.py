class Human:
    def __init__(self):
 
        self.name = "Generic Human"
        self.strength = 100
        self.health = 250
        self.agility = 40
        self.defense = 5
        self.mana = 10


    def display_info(self):

        print(f"{self.name}: \n strength: {self.strength} \n health: {self.health} \n defense: {self.defense}")

    def attack(self, target):
        target.display_info()
        print(f"[ATTACK] {self.name} is attacking {target.name}")
        target.defend(self.strength) # ! abstraction
        target.display_info()

    # take damage
    def defend(self, damage):
        print(f"dmg before {damage}")
        self.defense -= damage
        print(f"dmg after {damage}")
        self.health -= damage
        
        print(f"[DEFEND] {self.name} takes {damage} DMG and now has {self.health}")


# Create Instances

# human1 = Human("James", 25, 100,  50, 10)
# human2 = Human("Arthur", 10, 200, 80, 6)

# human1.attack(human2)