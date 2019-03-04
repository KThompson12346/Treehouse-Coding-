made up of key and value
# are mutable i.e. can change as you want them to dynamically
# syntax {"key": "value"}
# will throw a 'runtime' error if accessing a key that doesn't exist
course = {"Title": "Python Collections", "Teacher": "Kenneth Love", "Videos": 22}

player = {"name": "Rex", "remaining_lives": 3, "levels": [1, 2, 3, 4],
          "items": {"Weapons": ["sword", "bow"], "Potions": ["health", "stamina"]}}

Kirome = {"first_name": "Kirome", "Job": "None"}
Kirome["last_name"] = "Thompson"
Kirome.update({"Job": "Python Teacher", "editor": "Vim"}) # update method allows for changing or setting multiple values at once
Kirome["editor"] = "any"
Kirome["brothers"] = 2
del Kirome["editor"]

# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
def word_count(a_string):
    a_string = a_string.lower() # turns the string into all lowercase
    words = a_string.split() # splits all the words up into a list according to where the whitespaces are
    my_dict = {} # creates a new dictionary that is empty
    for word in words: # for loop that loops through each word in the string words
        my_dict[word] = words.count(word) # each word in the string is then put into a key in the dictionary with my_dict[word] and then the word count for each word is placed inside each keys value words.count(word)
    return my_dict # and now the dictionary is returned
