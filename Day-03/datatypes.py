Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#data Types
#int float complex
a = 12
type(a)
<class 'int'>
b = 13.4
type(b)
<class 'float'>
c = 12+4j
type(c)
<class 'complex'>
c = 12+6j
c
(12+6j)

#sequence
#str list tuple
s = "Nithin"
id(s)
2251943763888
s
'Nithin'
l = [1,2,3,4,5,5,6]
l
[1, 2, 3, 4, 5, 5, 6]
type(l)
<class 'list'>
id(l)
2251943636160
t = (1,2,3,4,5,5,6)
t
(1, 2, 3, 4, 5, 5, 6)
id(t)
2251942702416
l.append(20)
l
[1, 2, 3, 4, 5, 5, 6, 20]
>>> id(l)
2251943636160
>>> type(l)
<class 'list'>
>>> t.append(20)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    t.append(20)
AttributeError: 'tuple' object has no attribute 'append'
>>> t
(1, 2, 3, 4, 5, 5, 6)
>>> type(t)
<class 'tuple'>
>>> id(t)
2251942702416
>>> 
>>> #mapping
>>> #set dict
>>> s = (1,2,3,4,5)
>>> s
(1, 2, 3, 4, 5)
>>> type(s)
<class 'tuple'>
>>> s = {1,2,3,4}
>>> type(s)
<class 'set'>
>>> s.append(20)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    s.append(20)
AttributeError: 'set' object has no attribute 'append'
>>> type(s)
<class 'set'>
>>> id(s)
2251943450144
>>> d = {"name": "name","id": 10, "stock" : True}
>>> d
{'name': 'name', 'id': 10, 'stock': True}
>>> type(d)
<class 'dict'>
>>> id(d)
2251943787968
>>> s = frozenset({1,2,3,4,5})
>>> s
frozenset({1, 2, 3, 4, 5})
>>> 
>>> a = True
>>> b = False
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
