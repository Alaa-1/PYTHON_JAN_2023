# Loops

# * For Loop
# range
# Start, Stop, Step
#    v     v   v
#   0   number  1  (default values)
# [1, 10[
1,2,3,4,5,6,7,8,9,10


#incr
# for unicorn in range(11):

#     print(unicorn)

# Decr
# for idx in range(10, 0, -1):
#     print(idx)

animals = ["tiger", "elephant", "bird", "cat"]

# Iterate through a list

# for i in range(len(animals)):
#     print(animals[i])

name = "Smith"


# for animal in animals:
#     print(animal)

# iterate through a string

# for char in name:
#     print(char)

# Iterate through dict

person = {
    'name': 'Morpheus',
    'age' : 55,
    'is_covid' : False
}

# for k, v in person.items():
#     print(k, v)

    
# for i in range(len(animals)):
#     print(i, animals[i])

# for idx, animal in enumerate(animals):

#     print(idx, animal)



person = {
    'name': 'Morpheus',
    'age' : 55,
    'is_covid' : False,
    'children': [
        {
            "name": 'Arthur',
            "age": 15
            },
            {
            "name": "jane",
            "age": 6
            }
        ]
}


# for child in person['children']:
#     # print(child)
#     for k, v in child.items():
#         print(k, v)


# WHILE
# exit a loop in the terminal Ctrl + c

count = 0
while count <= 5:
    print("looping - ", count)
    count += 1
