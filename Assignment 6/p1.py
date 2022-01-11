# 21. a. Write a Python Program to Check 
# whether a Number is a Palindrome or not.
# b. Write a program to input N numbers 
# and then print the second largest number

num =int(input("Enter number:"))
temp=num
sum=0
while(num>0):
    dig=num%10
    sum=sum*10+dig
    num=num//10
if(temp==sum):
    print("The number is a palindrome!")
else:
    print("The number isn't a palindrome!")