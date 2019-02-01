import re

names_file = open("names.txt", encoding = "utf-8") # Opens up names.txt, specifies the encoding type of the file
data = names_file.read() # Content of names.txt is read into the variable data
names_file.close() # Closes the file after it has been opened and read
#
# last_name = r'Love'
# first_name = r'Kenneth'

 # r tells Python that the string after it is a raw string print(re.match(r'Love', data))
#print(re.match(last_name, data)) # .match() compares the beginning of the string in data (names.txt) with the argument given
#print(re.search(first_name, data)) # .search() compares anywhere in the string in data (names.txt) with argument given

# \w matches any unicode characters, lower case
# \W matches anything thing is not a unicpode character, upper case
# \s == [\t\n\r\f\v] matches any white space, lower case
# \S matches anything that is not white space, upper case
# \d matches any number from 0 to 9, lower case
# \D matches anything that is not a number, upper case
# \b matches word boundaries/edges of a word, lower case
# \B matches anything that is not the edge of a word, upper case
# {3} counts something that appears 3 times
# {,3} counts something that appears 0 to 3 times
# {3,} counts something that appears more than 3 times
# {3,5} counts something that appears 3, 4, 5 times
# ? counts something that appears 0 or 1 time, place after
# * something that appears at least 0 times
# + something that appears at least once
# Sets:
# [aple] Will match the set of characters to apple
# [a-z] Will match any lower case letters from a to z
# [^2] Will match anything that is not a 2

# print(re.match(r"\w, \W", data))
# print(re.findall(r"\(?\d{3}\)?-?\s?\d{3}-\d{4}", data)) # Searches the whole file/variable with file
# print(re.findall(r"\w*, \w+", data))

# print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
# print(re.findall(r'\b[trehous]{9}\b', data, re.IGNORECASE))

# def first_number(string):
#     return re.search(r'\d', string)

# def numbers(count, string):
#     return re.search(r"\d" * count, string)
#
# def find_emails(string):
#     return re.findall(r"\b[-\w\d+.]+@[-\w\d.]+", string)

# print(re.findall(r"""
#     \b@[-\w\d.]* # first a word boundary, an @, and then any number of characters
#     [^gov\t]+ # ignore one or more instances of the letters 'g', 'o', or 'v' and a tab.
#     \b # Match another word boundary
# """, data, re.VERBOSE|re.I))
# print("----------------------------------------------------------------------------")
# print(re.findall(r"""
#     \b[-\w]+, # Find a word boundary, one or more hyphens or characters, and a comma
#     \s # Find 1 whitespace
#     [-\w] # one or more hyphens and characters and explicit spaces
#     [^\t\n] # Ignore tabs and newlines
# """, data, re.X)) # re.X == re.VERBOSE (same thing)
# print("----------------------------------------------------------------------------")
# # good_numbers = re.findall(r"[^5\^6\^7]", data) # Will find all matches in data that are not 5, 6, or 7
# line = re.search(r'''
#     ^(?P<name>[-\w ]*,\s[-\w ]+)\t # Last and first names, ^ marks beginning of the string
#     (?P<email>[-\w\d.+]+@[-\w\d.]+)\t # Email
#     (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t # Phone
#     (?P<job>[\w\s]+,\s[\w\s.]+)\t? # Job and Company
#     (?P<twitter>@[\w\d]+)?$ # Twitter, $ marks end of the string
# ''', data, re.X|re.M) # re.MULTILINE or re.M makes the end of a line the end of the string
# print(line)
# print(line.groupdict())

print("----------------------------------------------------------------------------")

# names = re.search(r'''
#     ^(?P<lastname>[-\w\s]+,)
#     (?P<firstname>[-\w\s])$
# ''', data, re.M)
names = re.match(r'''
    ^(?P<fullname>[-\w ]+,\s[-\w ]+)$
''', data, re.X|re.M)
print(names)
