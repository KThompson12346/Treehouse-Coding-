# Problem 1: Warm the oven
# Write a while loop that checks to see if the oven
# is 350 degrees. If it is, print "The oven is ready!"
# If it's not, increase current_oven_temp by 25 and print
# out the current temperature.

current_oven_temp = 75

# Solution 1 here
while current_oven_temp < 350:
    current_oven_temp += 25
    print(current_oven_temp)
    if current_oven_temp == 350:
        print("The oven is ready!")


# Problem 2: Total and average
# Complete the following function so that it asks for
# numbers from the user until they enter 'q' to quit.
# When they quit, print out the list of numbers,
# the sum and the average of all of the numbers.

def total_and_average():
    # Solution 2 here
    numbers = []
    condition = True
    while condition:
        user = input("Enter a number: (press 'q' to quit) ")
        if user == 'q'.lower():
            break
        numbers.append(float(user))
    print("The list of numbers is: {}".format(numbers))
    print("The sum of the numbers is: {}".format(sum(numbers)))
    print("The average of the numbers is: {}".format(sum(numbers) / len(numbers)))

total_and_average()

# Problem 3: Missbuzz
# Write a while loop that increments current by 1
# If the new number is divisible by 3, 5, or both,
# print out the number. Otherwise, skip it.
# Break out of the loop when current is equal to 101.

current = 1
divisible_3 = current % 3 == 0 # This value evaluates to false as 0 is falsey
divisible_5 = current % 5 == 0
# Solution 3 here
while current < 101:
    if not current % 3 or current % 5 == 0:
        print("current is: {}".format(current))
    current += 1
