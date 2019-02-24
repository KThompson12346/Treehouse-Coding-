# Create a new empty list named shopping list
shopping_list = []

def show_help():
    print("What items would you like to buy?")
    print("""
    Enter "DONE" when you have finished choosing items.
    Enter "HELP" for instructions.
    Enter "SHOW" to show the list of items
    """)


# Create a function named add_to_list that declares a parameter named item
    # Add the item to the list
def add_to_list(item):
    shopping_list.append(item)
    # Notify user that the item was added, and state the number of items in the list currently
    print("Your item was added to shopping list, number of items currently in your shopping list is {}".format(len(shopping_list)))


# define a function named show_list that prints all the items in the list
def show_list():
    print("Your items are: ")
    for item in shopping_list:
        print("- " + item)


show_help
while True:
    new_item = input("> ")

    if new_item == "DONE":
        break # break will break out of the loop
    elif new_item == "HELP":
        show_help()
        continue # continue will complete the current iteration of the loop
    # Enable the SHOW command to show the list. Don't forget to update the HELP documentation
    elif new_item == "SHOW":
        show_list()
        continue
    # Call add_to_list with new_item as an argument
    add_to_list(new_item)
show_list()
