# Dictionary Literal
car1 = {
    "color": "red",
    "model": "BMW",
    "release_year": 2020,
    "is_automatic": True,
    "horse_power": 300,
    "number_door": 4

}

car2 = {
    "color": "blue",
    "model": "Audi",
    "release_year": 2005,
    "is_automatic": True,
    "horse_power": 300,
    "number_door": 4
}

car3 = {
    "color": "blue",
    "model": "Audi",
    "release_year": 2005,
    "is_automatic": False,
    "horse_power": 900,
    "number_door": 4
}


car4 = {
    "color": "blue",
    "model": "Audi",
    "release_year": 2005,
    "is_automatic": True,
    "horse_power": 300,
    "number_door": 2
}


# OOP
# Let us create a factory/blueprint
# less code
# Reusing code
# DRY = Don't Repeat Yourself

class Car:

    def __init__(self, my_color, my_model, my_release_year, my_is_automatic, my_horse_power,  km = 5,  my_number_door = 4): #magic method/ dunder method
        # Attributes/ characteristics
        self.color = my_color
        self.model = my_model
        self.release_year = my_release_year
        self.is_automatic = my_is_automatic
        self.horse_power = my_horse_power
        self.number_door = my_number_door
        self.km = 0

    # def __str__(self):
    #         return f'The car model is= {self.model}'

    # Actions / verbs

    def accelerate(self,speed):
        print(f"The car is moving at {speed}")

        return self

    def break_it(self):
        print( "Car is breaking")
        return self


    def change_gears(self,gear):
        if self.is_automatic == True:
            print("We don't have gears")
        else:
            print(f"We are changing to the {gear} gear")
            
        return self

# create an instance from the Car class
Tesla = Car("White & Red", "Model S", 2023, True, 700, 6)
Lexus = Car("orange", "LFA", 2016, False, 800, 2)

# Access The Attributes
print(Tesla.color)
print(Lexus.number_door)


#invoking the methods
Tesla.break_it().break_it().break_it().change_gears(2).accelerate(100)

Lexus.change_gears(3)

# print(Lexus.accelerate(250))


# we are running our code from the current file
# print(__name__)

# display the builtin dictionary methods
# print(dir(dict))