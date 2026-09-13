Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#tuple
#tuple declaration
t = ()
t
()
t = tuple()
t
()
t = (1,2,3,4)
t
(1, 2, 3, 4)
t = (1)
t
1
t = (1,)
t
(1,)
t = (1,1,1,1)
t
(1, 1, 1, 1)
t = (1,23,4,"str",[1,23],(1,2,3),{1,2,3},{1:1,2:2}, True)
t
(1, 23, 4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
type(t)
<class 'tuple'>

#tuple operations
t
(1, 23, 4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t = (1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[1]
23.4
t[-1]
True
t[2]
'str'
t[::1]
(1, 23.4, 'str', [1, 23], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2}, True)
t[-1::]
(True,)
t[-1::1]
(True,)
t[-1:8]
(True,)
t[-1:-8]
()
t[-1:-8:1]
()
23.4 in t
True
True in t
True
t = (12,3,43,567,433,87,988)
t
(12, 3, 43, 567, 433, 87, 988)
sorted(t)
[3, 12, 43, 87, 433, 567, 988]
max(t)
988
min(t)
3
len(t)
7
t
(12, 3, 43, 567, 433, 87, 988)
>>> t.index(43)
2
>>> t.append(5)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    t.append(5)
AttributeError: 'tuple' object has no attribute 'append'
>>> sum(t)
2133
>>> all(12,3,43)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    all(12,3,43)
TypeError: all() takes exactly one argument (3 given)
>>> t.count(t)
0
>>> t
(12, 3, 43, 567, 433, 87, 988)
>>> t = (1,23,45,45,23,45)
>>> t.count(45)
3
>>> any((45,1))
True
>>> all((3,5,6))
True
>>> t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    t[4].append(5)
AttributeError: 'int' object has no attribute 'append'
>>> t = (1,2,3)
>>> a,b,c = t
>>> a
1
>>> b
2
>>> c
3
>>> t[4].append(5)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    t[4].append(5)
IndexError: tuple index out of range
>>> t = (1,2,3,4,[1,2,3],5)
>>> t[4].append(4)
>>> t
(1, 2, 3, 4, [1, 2, 3, 4], 5)
>>> t = (1,2,3,4)
>>> sum(t)
10
>>> 
