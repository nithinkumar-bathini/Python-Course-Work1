Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
a = 10
float(a)
10.0
str(a)
'10'
complex(a)
(10+0j)
bool(a)
True
list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
f = 13.4
int(f)
13
complex(f)
(13.4+0j)
str(f)
'13.4'
bool(f)
True
list(f)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
>>> c = 12+3j
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> str(c)
'(12+3j)'
>>> bool(c)
True
>>> s = 'codegnana'
>>> a = '876554'
>>> int(s)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'codegnana'
>>> int(a)
876554
>>> float(s)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'codegnana'
>>> float(a)
876554.0
>>> complex(a)
(876554+0j)
>>> bool(a)
True
>>> list(a)
['8', '7', '6', '5', '5', '4']
>>> list(s)
['c', 'o', 'd', 'e', 'g', 'n', 'a', 'n', 'a']
>>> tuple(s)
('c', 'o', 'd', 'e', 'g', 'n', 'a', 'n', 'a')
>>> set(s)
{'n', 'd', 'a', 'e', 'c', 'g', 'o'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
