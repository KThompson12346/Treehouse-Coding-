print('Welcome to the Fibonacci number sequence calculator!')
print('____________________________')
number = int(input('Please enter a number, so the calculator can print out the sequence of numbers:'))

if (number <= 1):
    print('the number you entered is less than 1 and not part of the Fibonacci number sequence')
elif (number >= 1):
    fib = [0] * (number + 2) # is the first number in the sequence which is 0
    fib[1] = 1 # second number in the sequence which is 1
    print(fib[0]) # prints out first number in sequence
    print(fib[1]) # prints out second number in sequence
    for i in range(2, number + 1): # range starts from 2 as the first two numbers in fib sequence are manually created
        fib[i] = fib[i - 1] + fib[i - 2] # will add the two previous numbers together to get the current number in the sequence
        print(fib[i])
