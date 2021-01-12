#This is a demo task.

#Write a function:

#def solution(A)

#that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

#For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

#Given A = [1, 2, 3], the function should return 4.

#Given A = [−1, −3], the function should return 1.

#Write an efficient algorithm for the following assumptions:

#N is an integer within the range [1..100,000];
#each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    s = set(A) # create a set
    for i in range(1, len(A) + 1): # loop from 1 to the length of the list +1
        if i not in s: # if i is not in the set s then we've found the missing number
            return i # i is returned, i.e. the missing number
    return len(A) + 1 # the last index +1 is returned if end of list is met





l = [1, 3, 6, 4, 1, 2, 5]

print(solution(l))
