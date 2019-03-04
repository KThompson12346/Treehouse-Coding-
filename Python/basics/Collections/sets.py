set_one = set([1, 2, 3]) # create sets using the set() function
set_two = {4, 5, 6} # or create sets by just using {} curly brackets
print(type({})) # empty set is not {} this will create an empty dict
print(type(set())) # to create the empty use the set() function
set_three = {1, 11, 13, 7, 5, 3}
low_primes = {1, 3, 5, 7, 11, 13}
print(low_primes)
low_primes.add(17) # adding a value to the set use the .add() function
print('low_primes after adding 17, low_primes = {}'.format(low_primes))

low_primes.update({19, 23}, {2, 29}) # can update a set with .update() will add the set to the set which the method is called on
print('low_primes after being updated: {}'.format(low_primes))

low_primes.add(15)
print('low_primes with unwanted 15: {}'.format(low_primes))
low_primes.remove(15) # to remove a value use .remove()
print('low_primes after 15 is removed with .remove(): {}'.format(low_primes))

# Set Math:
# Union - Combination of two or more sets, no repeatitions of numbers are regarded
# Difference - Finds everything which is in the first set but not in the second
# Symmetric Difference - Is everything which is unique to each/every set
# Intersection - Gives a new set which contains every item which is in both sets
print('====> Set Math <====')
set1 = set(range(10))
set2 = {1, 2, 3, 5, 7, 11, 13, 17, 19, 23}
print('set1 = {}'.format(set1))
print('set2 = {}'.format(set2))
print('Union of set1 and set2: {}'.format(set1.union(set2))) # can also use the | (pipe) to get the union

print('Difference of set1 and set2: {}'.format(set1.difference(set2))) # can use - (hyphen) to get the difference, will give a different result when done the other way around

print('Symmetric difference of set1 and set2: {}'.format(set1 ^ set2)) # can also use .symmetric_difference()

print('Intersection of set1 and set2: {}'.format(set1.intersection(set2))) # can also use & for intersection, will give a different result when done the other way around

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}

def covers(topics):
    course_list = []
    for key, value in COURSES.items():
        if topics.intersection(value):
            course_list.append(key)
    return course_list

covers({'loops', 'booleans'})


def covers_all(all_topics):
    course_list = []
    for key, value in COURSES.items():
        if all_topics.issubset(value): #
            course_list.append(key)
    print('courses that cover all is: {}'.format(course_list))
    return course_list

covers_all({'functions'})
