import math

def split_check(total, num_of_people):
    if (num_of_people <= 1):
        raise ValueError("Need more than one person to split check")
    return math.ceil(total / num_of_people)

try: # Code block is expecting an error, so use try/except block for error handling
    total_due = float(input("What is the total? "))
    num_of_people = int(input("How many people? "))
    amount_due = split_check(total_due, num_of_people)
except ValueError as err:
    print("Oh no! that's not a valid value, try again...")
    print("({})".format(err))
else:
    print("Each person owes £{}".format(amount_due))
