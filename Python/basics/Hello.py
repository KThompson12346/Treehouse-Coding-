first_name = input("What is your first name? ")
print("Hello", first_name)
print(first_name, "is learning Python")

# Will convert the string "20" into a int
int("20")

# Will convert the int into a float
float(28)

# Converts the value into a string
str(286)

# Concatenation of two strings (can use + to concatenate strings)
first_string = "Hello nice to meet you"
second_string = ", what is your name?"
first_string += second_string

quote = "A person who never made a mistake never tried anything new"
# Will print out the length of a string
len(quote)

# Converts the string variable quote into all uppercase
quote.upper()

# Converts the string variable qoute into all lowercase
quote.lower()

# This allows for string formatting using place holders with curly brackets
subject_template = "Thanks for learning {} with us {}!"
subject_template.format("Python", "Valentina")
# Same as above without the variable
"You just bought {} {}.".format(5, "Bottles of water")

# Checks if first string is inside the second string using keyword in
"ham" in "hamster"

# Anything empty returns false, keyword not is negation
bool(1)
bool(0)
bool(not "45")

# If, Else and Elif (end condition with colons ':')
first_name = input("What is your first name? ")
print("Hello", first_name)
if first_name == "Kirome":
    print(first_name, "is learning Python")
elif first_name == "Maximiliane":
    print(first_name, "is learning with fellow students in the community! Me too :)")
else:
    age = int(input("How old are you? "))
    if age <= 6:
        print("Wow you're {}! If you're confident with your reading already...".format(age))
    print("You should totally learn Python {}!".format(first_name))
print("Have a great day {}!".format(first_name))
