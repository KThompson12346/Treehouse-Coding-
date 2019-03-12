# Columns: Name, Day/Month, Celebrates, Age
BIRTHDAYS = (
    ("James", "9/8", True, 9),
    ("Shawna", "12/6", True, 22),
    ("Amaya", "28/2", False, 8),
    ("Kamal", "29/4", True, 19),
    ("Sam", "16/7", False, 22),
    ("Xan", "14/3", False, 34),
)

# Problem 1: Celebrations
# Loop through all of the people in BIRTHDAYS
# If they celebrate their birthday, print out
# "Happy Birthday" and their name
print("Celebrations:")
for person in BIRTHDAYS:
    if person[2]: # takes the 3rd index, True or False value;
        print("Happy Birthday, {}".format(person[0]))

print("-"*20)

# Problem 2: Half birthdays
# Loop through all of the people in BIRTHDAYS
# Calculate their half birthday (six months later)
# Print out their name and half birthday
print("Half birthdays:")

for person in BIRTHDAYS:
    name = person[0]
    birthdate = person[1].split('/') # splits each persons birthdate into a list of two the day and month
    birthdate[1] = int(birthdate[1]) + 6 # takes the birth month and adds 6 to represent half a year;
    if birthdate[1] > 12: # if the above line brings the birth month over 12 then;
        birthdate[1] = birthdate[1] - 12 # take 12 from the birth month to wrap it back round modulo arithmetic
    birthdate[1] = str(birthdate[1]) # turn the birth month back into a string so it can be joined back with the birth date
    print(name, "/".join(birthdate)) # print out the name and the birth date both as strings


print("-"*20)

# Problem 3: Only school year birthdays
# Loop through the people in BIRTHDAYS
# If their birthday is between September (9)
# And June (6), print their name
print("School birthdays:")

for person in BIRTHDAYS:
    name = person[0]
    birthdate = person[1].split('/')
    birthdate[1] = int(birthdate[1])
    if birthdate[1] in range(1, 7) or birthdate[1] in range(9, 13): # checks if the birth months is between 1-6 and 9-12
        print(name) # if it is it prints out the name


print("-"*20)

# Problem 4: Wishing stars
# Loop through BIRTHDAYS
# If the person celebrates their birthday,
# AND their age is 10 or less,
# Print out their name and as many stars as their age
print("Stars:")

for person in BIRTHDAYS:
    name = person[0]
    age = person[-1] # gets the last item in the list
    celebrates = person[-2] # gets the second item in the list; a True or False value
    if celebrates and age <= 10: # checks whether celebrates is True or False and if the age of each person is less than or equal to 10
        stars = '' # is an empty string for now
        for star in range(age): # for each star in the range of the persons age
            stars += '*' # this line adds a star string to the variable stars according to the age of person 
        print(name, stars)

print("-"*20)
