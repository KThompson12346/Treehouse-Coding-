# Slicing Python
# slice stops at the number after the colon, is exclusive of the number after the colon
# if number after the colon is not in the list then slice will simply take all values up to the end of the list without throwing an out of bounds error
# to copy a list without (i.e. to sort the list) changing the original list, slice the whole list with [:]
# slice a list you get a list, slice a string you get a string

favorite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles',
                   'warm woolen mittens', 'bright paper packages tied up with string',
                   'cream colored ponies', 'crisp apple strudels']

slice1 = favorite_things[1:4]
slice2 = favorite_things[5:7]
sorted_things = favorite_things[:]
sorted_things.sort()


range() this function will give you back values within a certain range i.e. up to (exclusive) to the specified number, but returns a special type of object
numbers = list(range(20))
print(numbers)
# to get all even numbers from the list numbers you use a step method [::2], first colon slices whole list, second colon distinguishes between a normal slice and the number which is known as the step tells python how many steps to take after adding another number to the slice/list
# can have a starting number by placing a number before first colon
# can be done with strings
even_numbers = numbers[::2]
print(even_numbers)
# negative numbers will get the end of a list
backwards_numbers = numbers[-1:-5:-1]
print(backwards_numbers)

def first_and_last_4(a_list):
    return a_list[0:4:15:19]

print(first_and_last_4([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))

# a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
# Replacing slices with the above number range if I wanted to replace 11 to 14 I would do a_list[10:14] = [eleven, twelve, thirteen, fourteen]
# To delete items in a list; del a_list[0:5] i.e. the indices of the range of items you want to delete
a_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print(a_list)
a_list[10:14] = ['eleven', 'twelve', 'thirteen', 'fourteen']
del a_list[16:19]
print(a_list)

def sillycase(a_string):
    middle = int(len(a_string) // 2)
    first = a_string[:middle].lower()
    second = a_string[middle:].upper()
    a_string = first + second
    return a_string

print(sillycase("treehouse"))

# Slice Functions:
def first_4(a_string):
    return a_string[0:4]

def first_and_last_4(b_string):
    return b_string[0:4] + b_string[-4:]

def odds(c_string):
    return c_string[1::2]

def reverse_evens(d_string):
    return d_string[::2][::-1]

print("Thompson")
print(reverse_evens("Thompson"))
