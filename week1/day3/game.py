from game_classes.barbarian import Barbarian
from game_classes.warrior import Warrior


# declare the instances

barbarian1 = Barbarian("Conan")
warrior1 = Warrior("Arthur")


while barbarian1.health > 0 and warrior1.health > 0:

    print("The barbaian is approach the knight")

    response = ""

    while not response == "1" and not response == "2":
        response = input("what to do? \n 1)attack \n 2) special attack \n >>>")

        if response == "1":
            barbarian1.attack(warrior1)
        elif response == "2":
            barbarian1.berserker_rage(warrior1)
        else:
            print(" >> Please enter a valid option")


  
# endgame
if barbarian1.health > 0:
    print("Congratulations, you Won!")
elif warrior1.health <= 0:
    print("double KO")
else:
    print("the Knight Won")