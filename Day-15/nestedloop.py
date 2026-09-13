for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()
'''
Output:
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * * 
'''

for i in range(5):
    for j in range(5):
        print(j%2,end=' ')
    print()
'''
Output:
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
0 1 0 1 0 
'''

for i in range(5):
    for j in range(5):
        print(i%2,end=' ')
    print()
'''
Output:
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
1 1 1 1 1 
0 0 0 0 0 
'''

for i in range(5):
    for j in range(5):
        print((i+j)%2,end=' ')
    print()
'''
Output:
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1
0 1 0 1 0
'''

for i in range(5):
    for j in range(5):
        print(i+j,end=' ')
    print()
'''
Output:
0 1 2 3 4
1 2 3 4 5
2 3 4 5 6
3 4 5 6 7
4 5 6 7 8
'''

c = 1
for i in range(5):
    for j in range(5):
        print(c,end=' ')
        c+=1
    print()
'''
Output:
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''

for i in range(5):
    for j in range(i+1):
        print('*',end=" ")
    print()
'''
Output:
* 
* * 
* * * 
* * * * 
* * * * * 
'''

for i in range(5):
    for j in range(5-i):
        print('*',end=' ')
    print()
'''
Output:
* * * * *
* * * *
* * *
* *
*
'''

n = 5
for i in range(n):
    for sp in range(n-i-1):
        print(' ',end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()
'''
Output:
        *
      * *
    * * *
  * * * *
* * * * *
'''

n = int(input("Enter the size: "))
for i in range(n):
    for sp in range(i):
        print(" ",end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * *
  * * * *
    * * *
      * *
        *
'''

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i <= m:
        for j in range(i+1):
            print('*',end=' ')
    else:
        for k in range(n-i):
            print('*',end=' ')
    print()
'''
Output:
Enter the size: 9
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

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i <= m:
        print('* '*(i+1),end=' ')
    else:
        print('* '*(n-i),end=' ')
    print()
'''
Output:
Enter the size: 9
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

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i <= m:
        print(' '*(m-i),'*'*(i+1),end=' ',sep='')
    else:
        print(' '*(i-m),'*'*(n-i),end=' ',sep='')
    print()
'''
Output:
Enter the size: 9
    * 
   ** 
  *** 
 **** 
***** 
 **** 
  *** 
   ** 
    * 
'''