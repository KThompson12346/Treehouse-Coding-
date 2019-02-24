shopping_list = []

def show_help():
    print("What items would you like to buy?")
    print("""
    Enter "DONE" when you have finished choosing items.
    Enter "HELP" for instructions.
    Enter "SHOW" to show the list of items
    """)


def add_to_list(item):
    shopping_list.append(item)
    print("Your item was added to shopping list, number of items currently in your shopping list is {}".format(len(shopping_list)))


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
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)
show_list()
