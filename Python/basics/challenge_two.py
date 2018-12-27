name = input("What's your name? ")

# TODO: Ask the user by name if they understand Python while loops
print("{}, do you you understand Python while loops?".format(name))
understand = input("Enter yes or no: ")

# TODO: Write a while statement that checks if the user doesn't understand while loops
# TODO: Since the user doesn't understand while loops, let's explain them.
# TODO: Ask the user again, by name, if they understand while loops.
while understand != "yes":
    if understand == "no":
        print("No problem {}, a while loop in Python is a block of code that will keep executing until the specified condition is false. How about now {}, do you understand Python while loops?".format(name, name))
        understand = input("Enter yes or no: ")
        
# TODO: Outside the while loop, congratulate the user for understanding while loops
print("Yay, that's great")
