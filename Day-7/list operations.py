Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#list operations
l = []
l = list()
type(l)
<class 'list'>
l = [1,2,3, "str", True, [1,2,3],(1,2,3),{1,2,3},{1:1,2:2,3:3},3+8j]
l
[1, 2, 3, 'str', True, [1, 2, 3], (1, 2, 3), {1, 2, 3}, {1: 1, 2: 2, 3: 3}, (3+8j)]
l = [1,1,1,1]
l
[1, 1, 1, 1]
a = [1,2,3]
b = [4,5,6]
a+b
[1, 2, 3, 4, 5, 6]
a*3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
a = [123,456,789,413,414]
a
[123, 456, 789, 413, 414]
a[1]
456
a[3]
413
a[4]
414
a
[123, 456, 789, 413, 414]
a[1:4]
[456, 789, 413]
a[::-1]
[414, 413, 789, 456, 123]
a[3::]
[413, 414]
a[1::2]
[456, 413]
413 in a
True
414 not in a
False
max(a)
789
min(a)
123
sorted(a)
[123, 413, 414, 456, 789]
a
[123, 456, 789, 413, 414]
len(a)
5

#list methods

l
[1, 1, 1, 1]
min(l)
1
max(l)
1
id(l)
2193428231680
l = [413, 414, 415, 45,29]
min(l)
29
max(l)
415
sorted(l)
[29, 45, 413, 414, 415]
l.append(1)
l
[413, 414, 415, 45, 29, 1]
l.append(20)
l
[413, 414, 415, 45, 29, 1, 20]
l.append(3,47)
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    l.append(3,47)
TypeError: list.append() takes exactly one argument (2 given)
a.insert(8)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    a.insert(8)
TypeError: insert expected 2 arguments, got 1
a.insert(1,345)
a
[123, 345, 456, 789, 413, 414]
a.extend([7,6,54])
a
[123, 345, 456, 789, 413, 414, 7, 6, 54]
a.pop()
54
a.pop(1)
345
l
[413, 414, 415, 45, 29, 1, 20]
l.pop(0)
413
l
[414, 415, 45, 29, 1, 20]
l.remove(1)
l
[414, 415, 45, 29, 20]
del a[1]
l
[414, 415, 45, 29, 20]
del l[1]
l
[414, 45, 29, 20]
del l[1:3]
l
[414, 20]
l.clear()
l
[]
>>> l.index(45)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    l.index(45)
ValueError: list.index(x): x not in list
>>> l
[]
>>> l = [1,2,3,4]
>>> l.index(3)
2
>>> a = [1,2,3,4]
>>> b = a
>>> b
[1, 2, 3, 4]
>>> b.append(12)
>>> b
[1, 2, 3, 4, 12]
>>> a
[1, 2, 3, 4, 12]
>>> a = [1,2,3,4]
>>> c = a.copy()
>>> c
[1, 2, 3, 4]
>>> c.append(12)
>>> c
[1, 2, 3, 4, 12]
>>> a
[1, 2, 3, 4]
>>> any([1,'',False,[],(),{},set ()])
True
>>> any([0,'',False,[],(),{},set ()])
False
>>> all([1,'',False,[],(),{},set ()])
False
>>> l
[1, 2, 3, 4]
>>> l = [12,34,5,77]
>>> sort(l)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    sort(l)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
>>> sorted(l)
[5, 12, 34, 77]
>>> l
[12, 34, 5, 77]
>>> l.sort()
>>> l
[5, 12, 34, 77]
>>> l.reverse()
>>> l
[77, 34, 12, 5]
