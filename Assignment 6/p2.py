# b. Write a program to input N numbers and 
# then print the second largest number

n = int(input("How many numbers you want to enter? "))
l=[]
for i in range(0, n):
    a = int(input())
    l.append(a)  
    a=int(input())  
print(l)

list.sort(l)
print("Second Largest Number =", l[n-2])


