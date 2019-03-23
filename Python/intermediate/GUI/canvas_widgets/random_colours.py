from random import choice

def random_colour_code(): 
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    colour_code = '#'
    for i in range(0,6):
        colour_code = colour_code + choice(hex_chars)
    return colour_code
