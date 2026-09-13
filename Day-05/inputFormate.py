Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Input Fuctions
#int float complex str list tuple set dict bool

a = input()
nithin
a
'nithin'
a = input("Enter your name")
Enter your namePrabhas
a
'Prabhas'
b = int(input("Enter b: "))
Enter b: 21
b
21
cgpa = float(input("Enter CGPA: "))
Enter CGPA: 7.62
cgpa
7.62
names = 'nithin,srinivas,ayaz'
names.split()
['nithin,srinivas,ayaz']
names.split(",")
['nithin', 'srinivas', 'ayaz']
names.split("-")
['nithin,srinivas,ayaz']
courses =  'python django flask'
courses.split(',')
['python django flask']
courses.split(",")
['python django flask']
courses = 'python-django-flask'
courses
'python-django-flask'
courses.split()
['python-django-flask']
courses.split('-')
['python', 'django', 'flask']
courses = tuple(input("Enter Courses: ").split()
                python django
                
SyntaxError: invalid syntax. Perhaps you forgot a comma?
courses = tuple(input("Enter Courses: ").split())
                
Enter Courses: python django flask
courses
                
('python', 'django', 'flask')
courses = set(input("Enter Courses: ").split())
                
Enter Courses: python django flask
courses
                
{'flask', 'django', 'python'}
courses = dict(input("Enter Courses: ").split())
                
Enter Courses: python django flask
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    courses = dict(input("Enter Courses: ").split())
ValueError: dictionary update sequence element #0 has length 6; 2 is required
map(int,courses)
                
<map object at 0x0000026043A5BBC0>

marks = intput().split()
                
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    marks = intput().split()
NameError: name 'intput' is not defined. Did you mean: 'input'?
marks = input().split()
                
25,50,390,500
marks
                
['25,50,390,500']
map(int.marks)
                
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    map(int.marks)
AttributeError: type object 'int' has no attribute 'marks'
map(int,marks)
                
<map object at 0x00000260437E1440>
list(map(int,marks))
                
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    list(map(int,marks))
ValueError: invalid literal for int() with base 10: '25,50,390,500'
marks = list(map(int,input("Enter marks ").split()))
                
Enter marks 25 30 45 67
marks
                
[25, 30, 45, 67]
marks = tuple(map(int,input("Enter marks ").split()))
                
Enter marks 25 30 45 67
marks
                
(25, 30, 45, 67)
marks = set(map(int,input("Enter marks ").split()))
                
Enter marks 25 30 45 67
marks
                
{25, 67, 45, 30}
marks = dict(map(int,input("Enter marks ").split()))
                
Enter marks 25 30 45 67
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    marks = dict(map(int,input("Enter marks ").split()))
TypeError: object is not iterable
Cannot convert dictionary update sequence element #0 to a sequence

a,b = [1,2]
...                 
>>> a
...                 
1
>>> b
...                 
2
>>> a,b,c = (1,12.3,"str")
...                 
>>> a
...                 
1
>>> b
...                 
12.3
>>> email,password = input("Enter email and password").split())
SyntaxError: unmatched ')'
>>> email,password = input("Enter email and password").split()
Enter email and passwordnithin@gmail.com 12345
>>> email
'nithin@gmail.com'
>>> password
'12345'
>>> 
>>> status = eval(input())
True
>>> status
True
>>> type(status)
<class 'bool'>
>>> status = eval(input())
2+3j
>>> status
(2+3j)
>>> type(status)
<class 'complex'>
>>> status = eval(input())
[1,2,3,4]
>>> status
[1, 2, 3, 4]
>>> status = eval(input())
(1,2,3,4)
>>> status
(1, 2, 3, 4)
>>> type(status)
<class 'tuple'>
>>> status = eval(input())
{1:1,2:2,3:3}
>>> status
{1: 1, 2: 2, 3: 3}
>>> type(status)
<class 'dict'>
