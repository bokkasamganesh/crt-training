'''high order function: 
syntax:
map(funtion_name, iterable)'''

'''syntax:
filter function_name, itarable)'''

'''import function:
syntax:
from functon import reduce
reduce(function_name, sequence)'''

'''Anonymus function or lamda function
A function without a name is called as anonymoys function or lamda function
anonymous function are not defined using def keyword rather they are defined using lamda keyword
syntax:
lamda argument_list: expression'''

'''# write a python function to print the squares of n?

x=lambda n:print(n*n)
x(26)'''


'''# write a lamda function add 10 to a number?
add=lambda n:n+10
print(add(5))'''

'''# write a python program to check whether a user enteredd integer is even using lambda function?
even=lambda n:n%2==0
print(even(6))'''

'''# write a python program to square the numbers in the list using lambda function?
num=[1,2,3,4,5]
squared=lambda :[val*val for val in num]
print(squared())

# other format
num=[1,2,3,4,5]
squared=lambda num:list(map(lambda n:n*n,num))
print(squared(num))

#other fromat
num=[1,2,3,4,5]
res=[]
for i in num:
    val=i+i
    res.append(val)
print(res)

# other format
num=[1,2,3,4,5]
double=lambda n:n*n
res=list(map(double,num))
print(res)'''


'''# write a python program to readthe list of wordsas input from the user and return the length of each word for the list?

size=int(input("enter the size of the list:"))
words=[]
for i in range(size):
    val=input("enter the word:")
    words.append(val)
print("user entered list is:",words)
len=list(map(lambda n:len(n),words))
print("length of each word in the list is:",len)'''

'''# write a python program to read three integer values as input in same line and print the summation of it?

num=list(map(int,input("enter three integer values:").split()))
print(num)
print(sum(num))'''

'''# write a python program to read a list of elements as input from the user & print the square vlaues of list elements
# sample tast case:
# enter the numbers: [2,4,6,8,10]
#square list: [4,16,36,64,100]

num=list(map(int,input("enter the numbers:").split()))
sqr=list(map(lambda n:n*n,num))
print("square list:",sqr)

# other format of traditonal

size=int(input('enter the size of list :'))
list=[]
new=[]
for i in range(size):
    val=int(input('enter the value :'))
    list.append(val)
print(list)
for i in list:
    i=i*i
    new.append(i)
print(new)'''

'''# write a python program to read a list of numbers and print the list of even and odd number without using loops and conditional statements?

num=list(map(int,input('enter the numbers :').split()))
even=list(filter(lambda i:i%2==0,num))
odd=list(filter(lambda i:i%2!=0,num))
print(f"user entered list : {num}")
print(f"even numbers: {even}")
print(f"odd numbers: {odd}")'''


'''# Sales Data Analysis (Lists & Loops) 
#Problem Statement: 
# A shop records daily sales for a week in a list. You need to: 
# 1. Find the maximum sales in a single day.
# 2. Find the total sales of the week. 

sales=list(map(int,input('enter the sales in a week :').split()))
print(max(sales))
print(sum(sales))'''

'''# Student Grades Analyzer  
# Problem Statement:
 # A student’s grades in 3 subjects are given as a tuple. You need to: 
#1. Calculate the average marks. 
#2. Check if the student passed or failed. 
#Passing Rule: 
#• Average ≥ 40 and 
#• No subject has marks < 35 
#Input Format: 
#• 3 integers separated by space. 
#Output Format: 
#• Line 1: Average (up to 2 decimal places) 
#• Line 2: "Passed" or "Failed" 
#Constraints: 
#• 0 ≤ marks ≤ 100 
#Sample Test Cases: 
#Input 1: 
#45 50 30 
#Output 1: 
#41.67 
#Failed 

marks=tuple(map(int,input('enter 3 subjects marks ;').split()))
avg=sum(marks)/3
res=list(map(lambda i:i>=35,marks))
res="faild" if(False in res)else "passed"
print(f"avg : {avg}")
print(res)'''
'''
n=int(input())
n=list(str(n))
x=n.count('3')
y=n.count('6')
print(x+y)

#other format
n=input().strip()
print(sum(1 for d in n if d in ['3','7']))
'''

'''
str=list(input().split())
print(str)
print(len(max(str)))
'''
'''
str=list(input().split())
print(str)
print(len(max(str)))
'''
 
'''# 3: Even Odd Rearrangement
# Rearrange integers so that even numbers come first, then odd numbers. Order must be preserved in both groups?

arr = list(map(int, input().split()))
evens = [str(x) for x in arr if x%2==0]
odds  = [str(x) for x in arr if x%2!=0]
print(" ".join(evens+odds))'''

# Given a sentence, print its words in reverse order without reversing the characters inside words?
''' s=input().strip()
print(*s.split()[::-1])
# other format
s=input().strip()
print(' '.join(reversed(s.split())))'''

'''# Problem 5: Palindrome Check
# Problem Statement:
# Check whether a given string is a palindrome or not. Ignore case sensitivity?
s=input().strip()
s=s.lower()
if s==s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")'''

'''# 6: Sum of Digits
# Problem Statement:
# Given an integer N, find the sum of its digits.
n=int(input().strip())
s=0
for i in str(n):
    s+=int(i)
print(s)'''

'''# 7: Second Largest
# Problem Statement:
# Given N numbers, find the second largest unique number to complete the code in two lines?
arr=list(map(int,input().split()))
u=sorted(set(arr))
print(u[-2])
'''

'''# Problem 8: Count Vowels
# Problem Statement:
# Count the number of vowels (a, e, i, o, u) in a given string?
s=input().strip().lower()
vowels='aeiou'
count=0
for i in s:
    if i in vowels:
        count+=1
print(count)
'''

'''#  Factorial
# Problem Statement:
# Find the factorial of a given number N?
n=int(input().strip())
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
'''

'''# Problem 10: Fibonacci Series
# Problem Statement:
# Print the first N Fibonacci numbers.
n=int(input().strip())
a,b=0,1
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b'''