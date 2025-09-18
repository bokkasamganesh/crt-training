# display stars
# enter the value of N : 5
'''
* * * * *
* * * * * 
* * * * * 
* * * * *
* * * * *'''

'''n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("* ",end="")
    print()
    '''


'''
    *
    **
    ***
    ****
    *****
    '''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("* ",end="")
    print()'''

'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
'''    

'''
    * * * * *
    * * * *
    * * *
    * *
    *
    '''

'''
n=int(input('enter the value of n : '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    '''

'''
* * * * *
 * * * *
  * * *
   * *
    *
'''
'''
n=int(input('enter the value of n : '))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(" * ",end="")
    print()
    for k in range(1,n-i+1):
        print(" ",end=" ")
'''
'''
        *
       * *
      * * *
     * * * *
    * * * * *
     * * * *
      * * *
       * *
        *
        '''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
'''


'''
    *
  * * *
* * * * *

'''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()
'''
'''
n=int(input('enter the value of n : '))
for i in range(n,0,-1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,2*i):
        print("*",end=" ")
    print()
   '''
'''
n=int(input('enter the value of n: '))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{i},end" "")
'''
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

'''
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''
'''
n=int(input('enter the value of n: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''

'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''
'''
n=int(input('enter the value of n: '))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
'''

'''
         1
       1 2
     1 2 3
   1 2 3 4
 1 2 3 4 5        
'''

'''
n=int(input('enter the value of n: '))
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()
'''

'''
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
'''
'''
n=int(input('enter the value of n: '))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(i,end=" ")
    print()
'''

'''
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
'''
'''
n=int(input('enter the value of n: '))
for i in range(1,n+1):
    for j in range(n,0,-1):
        print(j,end=" ")
    print()
'''

'''
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j,end=" ")
    print()
'''

'''
1 1 1 1 1
2 2 2 2
3 3 3
4 4
5
'''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(i,end=" ")
    print()
'''
'''
1 1 1 1 1
0 0 0 0
1 1 1
0 0
1
'''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        if i%2!=0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
'''

'''
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
'''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(n,0,-1):
        if j>=i:
            print(j,end=" ")
    print()
'''

'''
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
'''
'''
n=int(input('enter the value of n : '))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if j<=i:
            print(i,end=" ")
    print()
'''

'''
1 0 1 0 1
1 0 1 0
1 0 1
1 0
1
'''
'''
n=int(input('enter the value of n : '))
for i in range(1,n+1):
    for j in range(1,n-i+2):
        if j%2!=0:
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()
'''

''''
     1
    1 2
   1 2 3
  1 2 3 4
 1 2 3 4 5
  1 2 3 4
   1 2 3
    1 2
     1    
  
'''

'''
A
A B
A B C
A B C D
A B C D E
'''
# line-1-2

n=int(input('enter the value of n : '))
for i in range(1, n+1):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()

# line-1-1

n = int(input("enter the value of n : "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end=" ")
    print()

#line-1-3
n = int(input("enter the value of n : "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(97 + j), end=" ")
    print()

#line-1-4
n = int(input("enter the value of n : "))
for i in range(1, n + 1):
    for j in range(i):
        print(chr(96 + i), end=" ")
    print()
