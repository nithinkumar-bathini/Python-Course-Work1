Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#python Operators

#arthemetic operators

a = 10
b = 5
a+b
15
a-b
5
a*b
50
a/2
5.0
a//2
5
a**2
100
a**3
1000
2**3
8
16**2
256
16***2
SyntaxError: invalid syntax
16//2
8
16/2
8.0
3%2
1
5%2
1
4%2
0

#Comparision operators

a = 10
b = 5
a
10
b
5
a<b
False
a>b
True
a<=b
False
a>=b
True
a == b
False
a != b
True

#assinment operators

a = 20
b = a+10
a = a+10
a
30
a = a+20

a
50
a += 10
a
60
a -=10
a
50
a *= 10
a
500
a /= 2
a
250.0
a //= 2
a
125.0
a = 1000
a /=2
a
500.0
a//=2
a
250.0
a
250.0

#Relational operators
email = True
password = False
email and password
False
login = True
login = False
Display_products = True
login or display_products
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    login or display_products
NameError: name 'display_products' is not defined. Did you mean: 'Display_products'?
login or Display_products
True
's' in 'aeiou'
False
'a' in 'aeiou'
True
'n' in 'nithin'
True
's' in 'nithin'
False
's' in 'srinivas'
True
7%2==0 and 3%2==0
False
6%2==0 and 3%2==0
False
6%2==0 or 3%2==0
True

#Membership operator
#str list tuple set dict
s = 'python programming'
'python' in s
True
'nithin' in s
False
'nithin' not in s
True
l = [1,2,3,4]
3 in l
True
5 in l
False
5 not in l
True
t = (10,20,30,40)
20 in t
True
20 not in t
False
20,30 in t
(20, True)
s = {'name' : 'nithin','batch': 65, 'course' : 'pfs'}
s
{'name': 'nithin', 'batch': 65, 'course': 'pfs'}
'name' in s
True
'nithin' in s
False

#Identity Operator
 l = [1,2,3,4]
 
SyntaxError: unexpected indent
l = [1,2,3,4]
m = [1,2,3,4]
l is m
False
l in m
False
l
[1, 2, 3, 4]
m
[1, 2, 3, 4]
l is m
False
l in m
False
l = m
l
[1, 2, 3, 4]
l is m
True
n = m
n in m
False
>>> 
>>> #Bitwise Operators
>>> 
>>> # 1. logic 2.
>>> 
>>> 11 & 12
8
>>> 11 | 12
15
>>> 11 ^ 12
7
>>> 11 << 12
45056
>>> 11 >> 12
0
>>> 2<<2
8
>>> 2 << 4
32
>>> 
>>> #Output operators
>>> 
>>> a= 10
>>> b = 3.14
>>> c = 'python'
>>> print(a,b,c)
10 3.14 python
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 3.14 c= python
>>> print("a=",a,"b=",b,"c=",c,sep='\t')
a=	10	b=	3.14	c=	python
>>> print("a=",a,"b=",b,"c=",c,sep='\n')
a=
10
b=
3.14
c=
python
>>> 
>>> print(f'a={a} b={b} c={c}')
a=10 b=3.14 c=python
>>> 
>>> #output Formating
>>> print("a=",a,"b=",b,"c=",c)
a= 10 b= 3.14 c= python
>>> print(f'a={a} b={b} c={c}')
a=10 b=3.14 c=python
>>> print('a=%d b=%f c=%s'%(a,b,c))
a=10 b=3.140000 c=python
>>> print('a=%d b=%f c=%s'.format(a,b,c))
a=%d b=%f c=%s
