# Packing takes multiple variables and places into one variable
# Unpacking takes one variable (of a whole group) and unpacks the variables into new variables
# ** or double asterisks when in a method signature is packing, when in a method call is unpacking (should be the last argument given )

# kwargs means keyword arguments, ** will pack whatever you pass into it into one variable
# this method is given one argument and when called it is given two
def packer(**kwargs):
    print(kwargs)


packer(name="Kirome", num=42, spanish_inquisition=None)


# this method is given two keyword arguments and when called below it is given one argument a dict that is unpacked
def unpacker(first_name=None, last_name=None):
    if first_name and last_name:
        print("Hi {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

upacker(**{"last_name": "Thompson", "first_name": "Kirome"})


# Unpacking a dictionary - Pulling multiple keys and their values of out of a dictionary to feed them to a function.
# Packing a dictionary - Putting multiple keyword arguments into a single dictionary.

# below unpacks a dict into the string format method
def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format(**dict)
# above and below is doing the same thing below but without using unpacking
def favorite_food(dict):
    return "Hi, I'm {name} and I love to eat {food}!".format(name='yourname', food='yourfood')


course_minutes = {'Python Basics': 232, 'Django Basics': 237, 'Flask Basics': 189, 'Java Basics': 133}

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))


list(enumerate("abc")) # takes an ordered iterable (list, string, tuple) and walks through the iterable and gives us back a tuple of the iterable in order for example [(0, a), (1, b), (2, c)]

for index, letter in enumerate("abcdefghijklmnopqrstuvwxyz"):
    print("{}: {}".format(index+1, letter))
