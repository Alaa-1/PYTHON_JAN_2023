# OOP

# Contructor (def __init__(self))
# Attributes / instance methods
# Methods

class Ninja:

    # class variables
    # stored in the CLASS itself
    # not part of the constructor / no self
    dojo_name = "Nefel"
    all_ninjas = []
    
    # contructor / self is the instance
    def __init__(self, name, weapon,  belt, health = 100):

        self.name = name
        self.weapon = weapon
        self.health = health
        self.belt = belt
        Ninja.all_ninjas.append(self)

    """ __main__ - means it ran directly from the file
        __repr__ = overwrite the <__main__.Ninja object at 0x0000019479413C10>
    """

    # def __repr__(self):
    #     return f"name: {self.name},\n weapon: {self.weapon},\n health: {self.health}, \n belt: {self.belt}"

    # @ is a decorator
    @classmethod   
    def information(cls):
        print(f"The name of the Dojo: {cls.dojo_name}")
        print(f"It has {len(cls.all_ninjas)} ninjas")


    @staticmethod
    def is_valid(ninja_name):
        if len(ninja_name) > 3:
            return True
        else: 
            return False
   

    def display_stats(self):
        print(f"The ninja name is {self.name}.\n Their health is {self.health} HP.\n They have a {self.belt} belt.")
        
    def attack(self, enemy):
        print(f"{self.name} is attacking {enemy.name}")
        enemy.health -= int(self.weapon.power)
        # print(f"{enemy.health}: the type is: {type(enemy.health)}")
        # print(f"{self.weapon.power}: the type is: {type(self.weapon.power)}")
        print(f"{enemy.name} got attacked with {self.weapon.type} and their health now is {enemy.health}")

        return self


# Instantiate the class
# Create instances

# ninja1 = Ninja("Michelangelo", "Nunchuks", 150, "orange")
# ninja2 = Ninja("Naruto", "shurikens", "black")
# ninja3 = Ninja("Donatello", "bo staff",80 ,"purple")




# Access an attr
# print(ninja1.belt)

# invoke a method
# ninja1.display_stats()
# ninja2.display_stats()
# print("-"*40)
# ninja1.display_stats()


# access a class variable

# print(Ninja.all_ninjas)

# ninja1.information()

# ninja1.is_valid(ninja1.name)


# * ------ Association Between Classes --------
# another Class

class Weapon:

    def __init__(self, power, durability, size, type):
        
        self.power = power
        self.durability = durability
        self.size = size
        self.type= type


# create instances of the class Weapon
my_weapon = Weapon(50, 100, "big", "Nunchuks")
enemy_weapon = Weapon(25, 40, "small", "bo staff")
# ninja100 = Ninja("Rafaelo", my_weapon, "blue", 350)


# make ninja1 attack ninja2

ninja1 = Ninja("Michelangelo", my_weapon, 150, "orange")
ninja2 = Ninja("Naruto", "shurikens", "black")
ninja3 = Ninja("Donatello", enemy_weapon ,"purple", 80)

ninja1.attack(ninja3).attack(ninja3)