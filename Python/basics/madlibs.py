# MadLibs - Practice Input and Output
#
# Template:
#    I enjoy practice! I find it helps me to __(verb)__ better.
#    Without practice, my __(noun)__ would probably not even work.
#    My code is getting more __(adjective)__ every single day!


# TODO: Prompt the user for parts of speech and store them in variables
verb = input("Please enter a verb: ")
noun = input("Please enter a noun: ")
adjective = input("Please enter an adjective: ")


# TODO: Output the template to the screen with the blanks filled out with what the user stated
print("I enjoy practice! I find helps me to {} better. without practice, my {} would probably not even work. My code is getting more {} every single day!".format(verb, noun, adjective))
