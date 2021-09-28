import math


# 1 Write a Python Program to Find the Smallest Divisor of an Integer other than 1.
num = int(input("Enter an integer:"))
arr = []
for i in range(2, num+1):
    if(num % i == 0):
        arr.append(i)
arr.sort()
print("Smallest divisor is:", arr[0])

#output:
# Enter an integer: 89
# Smallest divisor is : 89


# 2 Write a Python Program to Check whether a Number is a Palindrome or not.



n1 = input("Enter The Number : ")
n2 = n1[::-1]
n1 = int(n1)
n2 = int(n2)

if n1 == n2:
    print("The number is Palindromic")
else:
    print("The number is not Palindromic")

# output:
#  Enter The Number : 161
# The number is Palindromic  


# 3.Write a Python Program to print the Prime Factors of an Integer

N = int(input(" Please Enter any Number: "))

for i in range(2, N + 1):
    if(N % i == 0):
        flag = 1
        for j in range(2, (i // 2 + 1)):
            if(i % j == 0):
                flag = 0
                break

        if (flag== 1):
            print(" %d is a Prime Factor of a Given Number %d" % (i, N))

# 
# Please Enter any Number: 34
# 2 is a Prime Factor of a Given Number 34
# 17 is a Prime Factor of a Given Number 34




# 4. Print the following pattern


n = int(input("Enter row Number :"))

for i in range(1, n+1):
    j = pow(2, i-1)
    while(j >= 1):
        print(j, end=" ")
        j = j//2
    print('\n')


# # 
# Enter row Number: 7
# 1

# 2 1

# 4 2 1

# 8 4 2 1

# 16 8 4 2 1

# 32 16 8 4 2 1

# 64 32 16 8 4 2 1





# 5. Print the following Pattern


n = int(input("Input --> "))

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print('\r')

# output :
# Input - -> 6
# * * * * * *
# *         *
# *         *
# *         *
# *         *
# * * * * * *


# 6. The set of input is given as ages. Then print the status according to the rules

age = int(input("Enter Age  : "))
if age > 80:
    print("very old")
elif age >= 50 and age <= 79:
    print("old")
elif age >= 18 and age <= 49:
    print("adult")
elif age >= 11 and age <= 17:
    print("young")
elif age >= 2 and age <= 10:
    print("child")
elif age == 1:
    print("in child")

# output : 
#  Enter Age: 67
# old






# 7. Convert a decimal number to a number of a given base b



def baseCon(num, base):
    n = ""
    while num > 0:
        dig = int(num % base)
        if dig < 10:
            n += str(dig)
        else:
            n += chr(ord('A')+dig-10)  # Using uppercase letters
        num //= base
    n = n[::-1]  # To reverse the string
    return n


Num1 = int(input(" Please Enter any Number: "))

b = int(input(" Please Enter any base: "))

print(baseCon(Num1,b));


# output:
# Please Enter any Number: 98
# Please Enter any base: 6
# 242
