# This is a comment

""" 
This is a doc string
"""


#? ---------- Primitive data types ----------

#* int
int_to_float = float(7)

int_to_complex = complex(35)

#* String
word = "Hello word !"

another_word = "World"

random = 45
# print(type(random))
# print(type(word))
# print(f"Your ticket number is{random}")

upper_case = word.split()
# print(upper_case)

#* Boolean
is_admin = True

#? ---------- Composite data types ----------

# ! Lists

empty_list = []

#                   0          1         2           3          4
super_heroes = ["superman", "hulk", "spiderman", "superman", "batman", 5, False]

#* add an element to the list at the end
# super_heroes.append("WonderWoman")
# add an element at specfic position

# super_heroes.insert(0,"Antman")

#* remove from the back (by default)
# super_heroes.pop()

# super_heroes.remove()

#* Change a value in the list
# print(super_heroes)

new_hero = "Captain America"
super_heroes[0]= new_hero

# print(super_heroes)

#! Dictionaries

# key, value pairs

dog_dict = {
    'name': 'spark',
    'age': 2,
    'color': "black",
    'has_owner' : False
}
dog_name = dog_dict['name']

dog_dict['fav_food'] = "meat"

#* check if a key exists
# if "owner" in dog_dict:
#     print("found it")       
# else:
#     print("Not found")

#* remove an element from dict

value = dog_dict.pop()
dog_dict.clear()



# print(dog_dict)


#* Tuples (immuatable)

dog = ('Bruce', 'cocker spaniel', 19, False)

# dog_1 = dog[0]
# dog_2 = dog[1]
# dog_3 = dog[2]
# dog_4 = dog[3]


weather1 = "sunny"
weather2 = "raining"
is_windy = True

#? ------------- Conditions  ---------------

if weather2 == 'sunny' and not is_windy:
    print("Let's go out")
else :
     print("Binge watch a movie")
