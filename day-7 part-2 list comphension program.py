# write a python program a list of even number from 1 to n using list list comprehension
n=int(input("enter the number :"))
even_num=[val for val in range(1,n+1) if val%2==0]
print(even_num)