def disemvowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    my_list = list(word)
    for char in word:
        for letter in vowels:
            if char == letter:
                my_list.remove(char)
    word = ''.join(my_list)
    return word

greeting = input('Hello, please enter your word to disemvowel: ')
new_word = disemvowel(greeting)
print('Your word is now: {}'.format(new_word))
