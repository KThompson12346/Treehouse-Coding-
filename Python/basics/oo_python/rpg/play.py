# MRO = Method Resolution Order, defines the class search path used by Python to search for the right method to use in classes having multi-inheritance.

from thieves import Thief

Kirome = Thief(name="kirome", sneaky=True) # explicitly assigning name and sneaky attributes
print(Kirome)
print(Kirome.sneaky)
print(Kirome.agile)
print(Kirome.hide(7))

#####################################

a_string = ["apple", 5.2, "dog", 8]

def combiner(string):
    temp = ""
    total = 0
    for char in string:
        if isinstance(char, (str)):
            temp += char
        elif isinstance(char, (int, float)):
                total += char
    return temp + str(total)

print(a_string)
print(combiner(a_string))

class Letter:
    def __init__(self, pattern=None):
        self.pattern = pattern

    def __str__(self):
        string = []
        for char in self.pattern:
            if char == '.':
                string.append('dot')
            if char == '_':
                string.append('dash')
        return '-'.join(string)

a_string = ['.', '.', '.', '_', '_']
print(a_string)
a = Letter(['.', '.', '.', '_', '_'])
print(a.__str__)
