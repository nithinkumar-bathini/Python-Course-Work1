'''def display(n):
    if n == 11:
        return
    print(n)
    display(n+1)
display(1)'''

'''def display(n):
    if n == 11:
        return
    display(n+1)
    print(n)
display(1)'''

'''def display(s,ind):
    if ind == len(s):
        return
    print(s[ind],end="")
    display(s,ind+1)
display("COdegnan",0)

def display(s,ind):
    if ind == len(s):
        return
    
    display(s,ind+1)
    print(s[ind],end="")
display("COdegnan",0)'''

'''def display(s,ind,w):
    if len(s)-w+1 == ind:
        return
    print(s[ind:ind+w])
    display(s,ind+1,w)
s = input("Enter the string: ")
w = int(input("Enter the width: "))
display(s,0,w)'''

'''def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind] + display(l,ind+1)
l = [1,2,3,4,5]
print(display(l,0))'''

'''def display(l,ind):
    if ind == len(l):
        return 0
    return l[ind] + display(l,ind+1)
l = 4567
print(display(l,0))'''

'''def display(l):
    if l == 0:
        return 0
    return l%10 + display(l//10)
l = 43567
print(display(l))'''

'''def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
print(factorial(5))
print(factorial(6))
print(factorial(7))'''


'''n = int(input("Enter the number: "))
if n == 1:
    print(0)
elif n == 2:
    print(0,1)
else:
    a,b = 0,1
    print(a,b)
    for i in range(n-2):
        a,b = b,a+b
        print(b,end = " ")'''

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
for i in range(20):
    print(fib(i))