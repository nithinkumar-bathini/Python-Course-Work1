Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#set operations
s = {}
s
{}
s = set()
s
set()
type(s)
<class 'set'>
s = {1,2,3,4,5,6,134124,124,23456,413}
s
{23456, 1, 2, 3, 4, 5, 6, 134124, 124, 413}
s = {1,1,1,1}
s
{1}
s = set()
s.add(1)
s
{1}
s.add(12.3)
s
{1, 12.3}
s.add("str")
s
{1, 12.3, 'str'}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add([2,3])
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    s.add([2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add(False)
s
{False, 1, 12.3, 'str'}
a = {1,2,3,4,5}
b = {3,5,6,7,8}
2 in a
True
10 not in a
True
a | b
{1, 2, 3, 4, 5, 6, 7, 8}
a & b
{3, 5}
a - b
{1, 2, 4}
b - a
{8, 6, 7}
a ^ b
{1, 2, 4, 6, 7, 8}
a
{1, 2, 3, 4, 5}
#{1}{1,2}{1,2,3,4,5}{1,2,3,4}{4,5}
a
{1, 2, 3, 4, 5}
{1}<=a
True
{1,2,3}<=a
True
{1,2,3}>=a
False
{7,8,9}>=a
False
a>={3,4,5}
True
m = {1,2,3}
n = {4,5,6}
n.isdisjoint(m)
True
a.isdisjoint(b)
False
a = {12,43,1,4,67,89,65}
a
{65, 1, 67, 4, 89, 43, 12}
sorted(a)
[1, 4, 12, 43, 65, 67, 89]
max(a)
89
min(a)
1
len(a)
7
a.count(1)
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    a.count(1)
AttributeError: 'set' object has no attribute 'count'
all({1,0,2,3,4})
False
all({1,4,12,43})
True
any({1,0,0,0})
True
sum(a)
281
a
{65, 1, 67, 4, 89, 43, 12}
a = {1,2,3}
b = a
b.add(4)
b
{1, 2, 3, 4}
a
{1, 2, 3, 4}
a = {1,2,3}
b = a.copy()
b.add(4)
b
{1, 2, 3, 4}
a
{1, 2, 3}
a.add(100)
a.add({20,30})
... Traceback (most recent call last):
...   File "<pyshell#129>", line 1, in <module>
...     a.add({20,30})
... TypeError: cannot use 'set' as a set element (unhashable type: 'set')
... a.update(20,30)
... Traceback (most recent call last):
...   File "<pyshell#130>", line 1, in <module>
...     a.update(20,30)
... TypeError: 'int' object is not iterable
... a.update({20,30,40})
... a
... {1, 2, 3, 100, 20, 40, 30}
... a.pop()
... 1
... a.pop()
... 2
... a.pop()
... 3
... a.remove(100)
... a
... {20, 40, 30}
... a.discord(20,40)
... Traceback (most recent call last):
...   File "<pyshell#138>", line 1, in <module>
...     a.discord(20,40)
... AttributeError: 'set' object has no attribute 'discord'. Did you mean: 'discard'?
... a.discard(20,40)
... Traceback (most recent call last):
...   File "<pyshell#139>", line 1, in <module>
...     a.discard(20,40)
... TypeError: set.discard() takes exactly one argument (2 given)
... a.discard(20)
... a
... {40, 30}
... a.clear()
... a
... set()
... 
... a = frozenset({1,2,3,4})
... a
... frozenset({1, 2, 3, 4})
... a.add(20)
... Traceback (most recent call last):
...   File "<pyshell#147>", line 1, in <module>
...     a.add(20)
... AttributeError: 'frozenset' object has no attribute 'add'
... a.remove(1)
... Traceback (most recent call last):
...   File "<pyshell#148>", line 1, in <module>
...     a.remove(1)
... AttributeError: 'frozenset' object has no attribute 'remove'
SyntaxError: multiple statements found while compiling a single statement
