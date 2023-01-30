# functions

 # what is a function?

# a set of instructions

# function can have paramters (optional)

#* with no parameters 

def greeting():
    return "Good afternoon"

# call it / inovke it
# greeting() 
# result = greeting()

# print(result)

#              param1  param2
#                v       v
# def greeting2(name, age):
#     return f"Hello {name} your age is: {age}"


# #                argument
# #                 v
# print(greeting2("19, John"))

#* positional argument
def greeting2(name, age):
    return f"Hello {name} your age is: {age}"

# print(greeting2(age =19, name = "john"))

# keyword argument

# ---------------------------------
#* default parameters

# say hello multiple times

#         parameter  another_parameter
#            v       v
# def say_hi( name = "unknown", times = 3):

    # for i in range (times):
    #     print("hello " + name)


# invoke/ calling the function
# name of func
#  |      arg 1  arg 2
# v        v      v
# say_hi('John', 10)



#* return multiple things

def greetings3(name, age, day):

    return {"name": name, "age": age,  "day": day}

# print(greetings3("rufus", "Monday", 38))

