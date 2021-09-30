# 1. Implement stack using Python.
stack_in_python= []
i=0
print('Enter the values , press enter to stop')
while i<10:
    val=input()
    if val=='':
        break
    stack_in_python.append(val)
print('Initial stack')
print(stack_in_python)
print('\npress p to pop , press just enter to stop')
while i<10:
    val=input()
    if val=='p':
        print(stack_in_python.pop())
    else:    
        break
print('\nStack after elements are popped:')
print(stack_in_python)



#      output--->

# 1,2,3,4,4,6,7,

# Initial stack
# ['1,2,3,4,4,6,7,']

# press p to pop , press just enter to stop
# p
# 1,2,3,4,4,6,7,


# Stack after elements are popped:
# []


# 2. Reduce a string of lowercase characters in range ascii[‘a’..’z’]by doing a series of operations.

st = input()
while True:
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            st = st[:i]+st[i+2:]
            break
    else:
        break
print(st if st else "Empty String")


#    output--->

# sssdhht
# sdt

#3. Represent an integer number in Roman.
def printRoman(n):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    ro = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
      
    while n:
        div = n // num[i]
        n %= num[i]
  
        while div:
            print(ro[i], end = "")
            div -= 1
        i -= 1

 


number = int(input("Enter the Number : "))
print("Roman value is:", end = " ")
printRoman(number)



#    output-->
# Enter the Number : 546
# Roman value is: DXLVI


# 4. Find the Twins primes between a range( Twin primes are pairs of prime numbers that have
# just one number between them: 5 and 7, 11 and 13, and 29 and 31).
def is_prime(n):
   for i in range(2, n):
      if n % i == 0:
         return False
   return True

def twins_Prime(f,l):
   for i in range(f,l):
      j = i + 2
      if(is_prime(i) and is_prime(j)):
         print(i,"and",j)

n1= int(input("num one ::"))
n2 =int(input("num two ::"))
twins_Prime(n1, n2)




#   output--->
# num one ::7
# num two ::99
# 11 and 13
# 17 and 19
# 29 and 31
# 41 and 43
# 59 and 61
# 71 and 73


# 5. Find out the palindromic prime numbers between a range.


def Palin(n):
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if temp == rev:
        return True
    else:
        return False


def Prime(n):
    
    if n == 1:
        return False
   
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True


n1=int(input("Enter the 1st number  : "))
n2=int(input("Enter the 2nd number  : "))
print("The prime palindromes in this range are : ")
for i in range(n1, n2+1):
    if Palin(i) and Prime(i):
        print(i,end=" ")


#      output--->

# Enter the 1st number  : 1
# Enter the 2nd number  : 1000
# The prime palindromes in this range are :
# 2 3 5 7 11 101 131 151 181 191 313 353 373 383 727 757 787 797 919 929 