# 1. Given a string of length greater than 2, return a string except 1 st and last characters.
l = "efghfd"
l1 = l[1:len(l) - 1]
print(l1)
# output: fghf
#p2
# Given 2 strings, s1, and s2 return a new string made of the first, middle and last char
# each input string.
s1 = input("string1 :")
s2 = input("String2 :")
s3=s1[0] + s2[0] + s1[len(s1) // 2] + s2[len(s2) // 2] + s1[-1] + s2[-1]
print(s3)
#  input 1 : string1 :abcdef
#  input 2 :String2 :ghijkl
# output : agdjfl


# p3
# Given 2 strings, s1 and s2, create a new string by appending s2 in the middle of s1
st1 =input("Number 1 :")
st2 =input("Number 2 :")
st1=st1[:len(st1)//2]+st2+st1[len(st1)//2:]
print(st1)

# input1 -->  Number 1 :34
# input2 -->  Number 2 :55
# output : 3554

 # p4
# 4. Find all occurrences of “India” in given string ignoring the case.
strr1 = "OK git it"
print(strr1.count("it"))

# output : 2

# 5. Find the last position of a substring “Emma” in a given string.
str1="She is the girl name ,Emma Stone"
x=str1.rfind("Emma")
print(x)

# output : 22

# p6
# Display the two substring separated by space
strrr1 ="ABCDEFGHI"
print(strrr1[:len(strrr1)//2]," ",strrr1[len(strrr1)//2:])

# output : ABCD   EFGHI


# p7
# 7. Given an input list removes the element at index 4 and add it to the 2nd position and
# also, at the end of the list.

sampleList = [34, 54, 67, 89, 11, 43, 94]
print(sampleList)
n = sampleList.pop(2)
print(sampleList)
sampleList.insert(4,n)
print(sampleList)

# output : [34, 54, 89, 11, 67, 43, 94]

#p8
# 8. Reverse the following tuple aTuple = (10, 20, 30, 40, 50,60,70,80,90,100)
aTuple = (10, 20, 30, 40, 50,60,70,80,90,100)
aTuple = aTuple[::-1]
print(aTuple)

# output :(100, 90, 80, 70, 60, 50, 40, 30, 20, 10)

#p9
# 9. Access value 20 from the following tuple aTuple = (&quot;Orange&quot;, [10, 20, 30], (5, 15, 25))
aaTuple = ("Orange", [10, 20, 30], (5, 15, 25))
print(aaTuple[1][2])

# output : 30


# p10
# Unpack the following tuple into 4 variables
aTuple = (10, 20, 30, 40 ,100,101)
a, b, c, d ,e, f = aTuple
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
'''
output : 
10
20
30
40
100
101
'''

# p11 swapping tupple
# 11. Swap the following two tuples tuple1 = (11, 22) tuple2 = (99, 88)
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1 ,"   ",tuple2)

# output : (99, 88)     (11, 22)

# p12
# 12. Copy element 44 and 55 from the following tuple into a new tuple tuple1 = (11, 22,33, 44, 55, 66)
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)
# output : (44, 55)

# p13
# 13. Modify the first item (22) of a list inside a following tuple to 222 tuple1 = (11, [22,33], 44, 55)

tuple1111 = (11, [22, 33], 44, 55)
tuple1111[1][0] = 222
print(tuple1111)

# output : (11, [222, 33], 44, 55)

#
# p14
# 14. Below are the two lists convert it into the dictionary keys = ['Ten&','Twenty','Thirty']
# values = [10, 20, 30]

keys = ['Ten&','Twenty','Thirty']
values = [10, 20, 30]
sampleDict = dict(zip(keys, values))
print(sampleDict)

# output : {'Ten&': 10, 'Twenty': 20, 'Thirty': 30}

# p15
# Merge following two Python dictionaries into one

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)

# output:{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# p16
# Check if a value 200 exists in a dictionary sampleDict = {'a,: 100, 'b': 200,'c': 300}

myDict = {'a': 100, 'b': 200,'c': 300}
print(200 in myDict.values())

# output: True

# p17

# 17. Rename key city to location in the following dictionary sampleDict = { "name": "Kelly",  "age":25,  "salary": 8000,  "city": "New york"}

sampleDict_list = {"name": "Kelly",  "age":45,  "salary": 128000,  "city": "Kolkata"}
sampleDict_list['location'] = sampleDict_list.pop("city")
print(sampleDict_list)

# output : {'name': 'Kelly', 'age': 45, 'salary': 128000, 'location': 'Kolkata'}

# p18
# 18. Get the key corresponding to the minimum value from the following dictionary sampleDict = {  'Physics': 82,  'Math': 65,  'history': 75}

sample_sub = {  'Physics': 98,  'Math': 95,  'history': 75}
print(min(sample_sub, key=sample_sub.get))

# output : history

# p19
# 19. Given a Python dictionary, Change Brad’s salary to 8500 sampleDict = { 'emp1': {'name': 'Jhon', 'salary': 7500},
# 'emp2': {'name': 'Emma', 'salary': 8000},  'emp3': {'name': 'Brad', 'salary': 6500}}



sampleDict_1 = { 'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000},  'emp3': {'name': 'Brad', 'salary': 6500}}

sampleDict_1['emp3']['salary'] = 8500
print(sampleDict_1)

# output:{'emp1': {'name': 'Jhon', 'salary': 7500}, 'emp2': {'name': 'Emma', 'salary': 8000}, 'emp3': {'name': 'Brad', 'salary': 8500}}