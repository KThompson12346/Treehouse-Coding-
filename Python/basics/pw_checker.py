import sys

banner = "Happy Birthday!"
print(banner)
for letter in banner:
    print(letter.upper())
    
MASTER_PASSWORD = "opensesame" # Capital letters is constants
password = input("Please enter a secure password: ")
attempts = 1
while password != MASTER_PASSWORD:
    if attempts > 3:
        sys.exit("Too many invalid password attempts :(")
    password = input("Invalid password, try again: ")
    attempts += 1
print("Welcome to secret town!")
