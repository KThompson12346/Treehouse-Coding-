
# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.
#
# Your code goes below here.
def num_teachers(dict):
    return len(dict) # returns the number of keys in the dictionary


def num_courses(dict):
    course_count = 0 # used as an increment value to count the number of courses
    for course in dict.values(): # for loop to count each course
        course_count += len(course) # course count is increment to the number of each course
    return course_count # course_count is returned


def courses(dict):
    course_list = [] # create an empty list to put the dictionary values in
    for course in dict.values(): # loop through the dictionary values (courses)
        course_list.extend(course) # the course_list list is extending by each course in the data dictionary
    return course_list # list of courses is returned



# def most_courses(dict):
#     course_count = 0
#     name = ''
#     for course in dict.values():
#         if len(course) > course_count:
#             course_count = len(course)
#     return course_count


def most_courses(dict):
    course_count = 0 # used to count the number 
    name = ''
    for teacher, course in dict.items():
        if len(course) > course_count:
            course_count = len(course)
            name = teacher
    return name
