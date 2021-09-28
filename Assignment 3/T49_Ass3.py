# 1. Write a Python function to find the Max of three numbers.

def max_3(a,b,c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c
    
a=int(input("no 1   :"))
b=int(input("no 2   :"))
c=int(input("no 3   :"))

ans=max_3(a,b,c)

print("The max Among The 3 is : ",ans)



# output:
# no 1   :4 
# no 2   :5
# no 3   :7
# The max Among The 3 is :  7

# 2. Write a Python function to sum all the numbers in a list.

def Sum_x(mylist):
    s=0
    for i in mylist:
        s=s+i;
    return s

n = int(input("Enetr The List Range : "))

k=[]
for x in range(n):
    l=int(input())
    k.append(l)

print("The Sum of elements In the List : ",Sum_x(k))


# output:
# Enetr The List Range : 10
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# The Sum of elements In the List :  55



# 3. Write a Python function to multiply all the numbers in a list.


def Mult_x(herlist):
    s=1
    for i in herlist:
        s=s*i;
    return s

n = int(input("Enetr The List Range : "))

m=[]
for x in range(n):
    l=int(input())
    m.append(l)

print("The Sum of elements In the List : ",Mult_x(m))

# output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# The Sum of elements In the List :  5040



# 4. Write a Python function to calculate the factorial of a number (a non-
# negative integer). The function accepts the number as an argument.

def fact(num):
    return 1 if (num==1 or num==0)else num*fact(num-1)

number = int(input("Enter a Number :"))
print("factorial of the number",number," is ::: ",fact(number))


# output:
# Enter a Number :8
# factorial of the number 8  is :::  40320

# 5. Write a Python function that accepts a string and calculate the number
# of upper case letters and lower case letters.

def Case_Up_Low(name):
    up =0
    low=0
    for i in range(len(name)):
        if (name[i]>='A'and name[i]<'Z'):
            up+=1
        elif (name[i]>='a'and name[i]<'z'):
            low+=1
    print("UpperCase letter : ",up,"\nLowercase letter : ",low)

n = str(input("Enter The String : "))
Case_Up_Low(n)

# output:
# Enter The String : ABGCHJadghkloiuy
# UpperCase letter :  6     
# Lowercase letter :  10 


# 6. Write a Python function that takes a list and returns a new list with
# unique elements of the first list.


def uni_List(lst):
    e=[]
    for i  in lst:
        if i not in e:
            e.append(i)
    return e

k=[1,2,3,4,4,4,5,6,6,7]


print("The unique elemnets are : ",uni_List(k))


# output:

# The unique elemnets are :  [1, 2, 3, 4, 5, 6, 7]

# 7. Write a Python function to check whether a number is perfect or not. Go
# to the editor

def per(n):
    t=0
    for i in range(1,n):
        if(n%i==0):
            t=t+i
    if(t==n):
        print("Perfect Number ")
    else :
        print("not a perfect number ")
num = int(input("Enter a number "))
per(num)

# output:
# Enter a number 7
# not a perfect number 


#8. Write a Python function that checks whether a passed string is
# palindrome or not.


def isPalindrom(w):
    s=w
    s = s[::-1]
    if w==s:
        print(w," is a Palindrom  ")
    else:
        print("not a palindrom ")


name = str(input("Enter a string : "))
isPalindrom(name)

# output:
# Enter a string : acdca
# acdca  is a Palindrom



# 9. Write a Python function to check whether a string is a pangram or not.
# Go to the editor


def isPanagram(s):
    c=0
    Alp ="abcdefghijklmnopqrstuvwxyz"
    for i in Alp:
        if i not in s.lower():
            c=c+1
            print("not a pangram string ")
    if(c==0):
        print(s,"is a panagram string")

name = str(input("Enter a string ::  "))
isPanagram(name)

# output:
# Enter a string ::  The quick brown fox jumps over the lazy dog
# The quick brown fox jumps over the lazy dog is a panagram string


# 10. Write a Python program that accepts a hyphen-separated sequence
# of words as input and prints the words in a hyphen-separated sequence
# after sorting them alphabetically.

def hyphenSepated(s):
    list_1=[n for n in s.split('-')]
    list_1.sort()
    print("output :\n",'-'.join(list_1))

i = input("input :")
hyphenSepated(i)

# output:
# input :green-red-yellow-black-white
# output :
#  black-green-red-white-yellow



# 11. Write a python program to show the permutation and
# combination of a inputted List.




def combo(lst, n):
      
    if n == 0:
        return [[]]
      
    l =[]
    for i in range(0, len(lst)):
          
        m = lst[i]
        remLst = lst[i + 1:]
          
        for p in combo(remLst, n-1):
            l.append([m]+p)
              
    return l

def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = [] 
    for i in range(len(lst)):
       m = lst[i]
       remLst = lst[:i] + lst[i+1:]
       for p in permutation(remLst):
           l.append([m] + p)
    return l

a ="abc"
list_1 =[x for x in a]
print("combination :",combo(list_1, 2))
b=list('123')

print("permutation")
for p in permutation(b):
    print (p)
          
'''


output : 


combination : [['a', 'b'], ['a', 'c'], ['b', 'c']]
permutation
['1', '2', '3']
['1', '3', '2']
['2', '1', '3']
['2', '3', '1']
['3', '1', '2']
['3', '2', '1']


'''