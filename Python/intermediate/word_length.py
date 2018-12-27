import re

# EXAMPLE:
# >>> find_words(4, "dog, cat, baby, balloon, me")
# ['baby', 'balloon']

names_file = open("names.txt", encoding = "utf-8")
data = names_file.read()
names_file.close()

def find_words(count, string):
    return re.search(r"\w{" + str(count) + ",}", string)

print(find_words(10, data))
