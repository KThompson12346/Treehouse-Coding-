first_tuple = (1, 2, 3)
second_tuple = (2, 3, 4)
third_tuple = (3, )
fourth_tuple = tuple([4, 5, 6])
print('first tuple {}, second tuple {}, third tuple {}, fourth tuple {}'.format(first_tuple, second_tuple, third_tuple, fourth_tuple))

a = 5
print('a is {}'.format(a))
b = 20
print('b is {}'.format(b))
a, b = b, a # swaps the values around a is 20 and b is 5, on the right side b, a is packed into a tuple
print('a is {} and b is {}'.format(a, b))
c = b, a # is a tuple
print('c is a tuple of b and a: {}'.format(c))

# packing values into a tuple
def add(*nums):
    total = 0
    for num in nums:
        total += num
    return total
print('3 + 3 = {}'.format(add(3,3)))


def multiply(*args):
    total = 1
    for num in args:
        total *= num
    return total
print('2 * 3 = {}'.format(multiply(2*3)))

# code works but no need to convert each string into a tuple
def stringcases(a_string):
    upper = tuple([a_string.upper()])
    lower = tuple([a_string.lower()])
    title = tuple([a_string.title()])
    reverse = tuple([a_string[::-1]])
    return tuple([upper, lower, title, reverse])

print(stringcases('Kirome nahum Thompson'))

# method takes two iterables and makes a list of tuples using a combination of the corresponding indecies from each iterable
def combo(iterable_a, iterable_b):
    list_a = list(iterable_a)
    list_b = list(iterable_b)
    index = 0
    a_tuple = ()
    tuple_list = []
    for value_a in iterable_a:
        temp_a = list_a[index]
        temp_b = list_b[index]
        a_tuple = tuple([temp_a, temp_b])
        tuple_list.append(a_tuple)
        index += 1
    return tuple_list

combo('123', 'abc')
