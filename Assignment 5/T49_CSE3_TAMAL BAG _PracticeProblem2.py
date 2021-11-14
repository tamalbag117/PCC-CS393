# Question 1:



# code


def starValue(arr, n):
    star = 0
    for i in arr:
        star = star + 1 if (i % n == 0) else star
    return star

def getStarValues(arr): 
    star_values = [starValue(arr[0:i], v) for i, v in enumerate(arr)]
    for a, b in zip(arr, star_values):
        print(f"Star value of {a} = {b}")
    return star_values

num_array = list(map(int, input("Enter the space-seperated number sequence: ").split()))
print(f"Maximum Star Value: { max( getStarValues(num_array) ) }")


# output :

Enter the space-seperated number sequence: 1 2 3 4 5 
Star value of 1 = 0
Star value of 2 = 0
Star value of 3 = 0
Star value of 4 = 0
Star value of 5 = 0
Maximum Star Value: 0




#question 2

#code

from itertools import permutations

def isBeautifulPermutation(arr):
    for x, y in zip(arr[:-1], arr[1:]):
        if (x & y == 0):
            return False
    return True

def printBeautifulPermutation(arr):
    for i in arr:
        if (isBeautifulPermutation(i)):
            print(*i, sep=", ", end="\n")

num_array = list(map(int, input("Enter the space-seperated number sequence: ").split()))
printBeautifulPermutation(permutations(num_array))



#output


Enter the space-seperated number sequence: 1 2 3 4 5
2, 3, 1, 5, 4
4, 5, 1, 3, 2


