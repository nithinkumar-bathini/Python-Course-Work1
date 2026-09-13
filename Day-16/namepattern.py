n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''

#A
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j == n-1 or i == m:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
* * * * * 
*       * 
*       * 
'''

#B
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1 or i == m:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
* * * * * 
*       * 
* * * * * 
'''

#C
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or  i == n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*         
*         
*         
* * * * * 
'''

#D
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''

#E
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or  i == m:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*         
* * * * * 
*         
* * * * * 
'''

#F
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or  i == m:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*         
* * * * * 
*         
*         
'''

#G
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or  i == n-1 or (j == n-1 and i >= m) or (i == m and j >= m):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
nter the size: 5
* * * * * 
*         
*   * * * 
*       * 
* * * * * 
'''

#H
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if  j == 0 or  j == n-1 or i == m:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*       * 
*       * 
* * * * * 
*       * 
*       * 
'''

#I
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == m:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
    *     
    *     
    *     
* * * * * 
'''

#J
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == m or (i == n-1 and j <= m):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
    *     
    *     
    *     
* * *     
'''

#K
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or (i == m and j <= m) or (i == j and i >= m) or (i+j == n-1 and i <= m):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*       * 
*     *   
* * *     
*     *   
*       * 
'''

#L
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*         
*         
*         
*         
* * * * * 
'''

#M
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and i <= m) or (i+j == n-1 and i <= m):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*       * 
* *   * * 
*   *   * 
*       * 
*       * 
'''

#N
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if (i == j and i <= m)  or (i == j and i >= m) or j == 0 or j == n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*       * 
* *     * 
*   *   * 
*     * * 
*       * 
'''

#O
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
*       * 
*       * 
* * * * * 
'''

#P
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or (j == n-1 and i <= m) or i == m:
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
* * * * * 
*         
*         
'''

#Q
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i == n-1 or j == n-1 or (i == j and j >= m):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
*   *   * 
*     * * 
* * * * * 
'''

#R
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or (j == n-1 and i <= m) or i == m or (i == j and j >= m):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*       * 
* * * * * 
*     *   
*       * 
'''

#S
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == m or i == n-1 or (j == 0 and i <= m) or (j == n-1 and i >= m):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
*         
* * * * * 
        * 
* * * * * 
'''

#T
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or j == m:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
    *     
    *     
    *     
    *     
'''

#U
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or i == n-1 or j == n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*       *
*       *
*       *
*       *
* * * * * 
'''

#V
n = int(input("Enter the size: "))
m = n // 2
for i in range(n):
    for j in range(n):
        if i <= m:
            if j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        else:
            if j == i - m or j == n - i + m - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
'''
Output:
Enter the size: 5
*       * 
*       * 
*       * 
  *   *   
    *     
'''

#W
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j == 0 or j == n-1 or (i == j and j >= m) or (i+j == n-1 and j <= m):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:  
Enter the size: 5
*       * 
*       * 
*   *   * 
* *   * * 
*       * 
'''

#X
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if (i == j and i <= m) or i+j == n-1 or (i == j and i >= m) :
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*       * 
  *   *   
    *     
  *   *   
*       * 
'''

#Y
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if (j == m and i >= m) or (i == j and i <= m) or (i+j == n-1 and i <= m):
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
*       * 
  *   *   
    *     
    *     
    *     
'''

#Z
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or i+j == n-1:
            print('*',end=" ")
        else:
            print(" ",end=" ")
    print()
'''
Output:
Enter the size: 5
* * * * * 
      *   
    *     
  *       
* * * * * 
'''
