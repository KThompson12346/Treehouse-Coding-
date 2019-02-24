# del keyword deletes the label not the object
# pop method removes the value/object in the list
# do not modify a list when looping through the list it gives unexpected results. Copy a list to remove/modify from a list properly
books = [
    "Learning Python: Powerful Object-Oriented Programming - Mark Lutz",
    "Automate the Boring Stuff with Python: Practical Programming for Total Beginners - Al Sweigart",
    "Python for Data Analysis - Wes McKinney",
    "Fluent Python: Clear, Concise, and Effective Programming - Luciano Ramalho",
    "Python for Kids: A Playful Introduction To Programming - Jason R. Briggs",
    "Hello Web App: Learn How to Build a Web App - Tracy Osborn",
]

video_games = [
    "The Legend of Zelda: Breath of the Wild",
    "Splatoon 2",
    "Super Mario Odyssey",
]

print("suggested gift: {}".format(books[0]))

# for in loops where I want to iterate through a list 
print("books:")
for book in books:
    print("* " + book)

def display_wishlist(display_name, wishes):
    items = wishes.copy()
    print(display_name + ":")
    suggested_gify = items.pop(0)
    print("======>>", suggested_gift, <<=====)
    for item in items:
        print("* " + wish)
        print()

display_wishlist("Books", books)
display_wishlist("Video Games", video_games)
