Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#dict
#mutable order hetro dynamic unidu
d = {}
d
{}
type(d)
<class 'dict'>
d = {1:4,2:8,3:13}
d
{1: 4, 2: 8, 3: 13}
d = {}
d[1] = 1
d[12.3] = 1
d['str'] = 1
d[(1,2,3)] = 1
d[2+3j] = 1
d[True] = 1
d[[1,2,3]] =1
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    d[[1,2,3]] =1
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[{1,2,3}] = 1
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[{1,2,3}] = 1
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1}
d[False] = 1
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1}
d[1] = 1
d[[2] = 12.3
  
SyntaxError: invalid syntax
d[2] = 12.3
  
d[3] = 'str'
  
]
SyntaxError: unmatched ']'
d[2] = 12.3
d[3] = 'str'
d[4] = 2+3j
d[5] = True
d[6] = [1,2,3]
d[7] = (1,2,3)
d[8] = {1,2,3}
d[9] = frozenset({1,2,3})
d[10] = {1:1,2:2}
d[11] = None
d
{1: 1, 12.3: 1, 'str': 1, (1, 2, 3): 1, (2+3j): 1, False: 1, 2: 12.3, 3: 'str', 4: (2+3j), 5: True, 6: [1, 2, 3], 7: (1, 2, 3), 8: {1, 2, 3}, 9: frozenset({1, 2, 3}), 10: {1: 1, 2: 2}, 11: None}]
d = {}
d[1] = 2
d
{1: 2}
d[1] = 3
d
{1: 3}

#dict operations
data = {'name':'nithin','course': 'pfs','batch':65}
data
{'name': 'nithin', 'course': 'pfs', 'batch': 65}
data['name']
'nithin'
data['pfs']
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    data['pfs']
KeyError: 'pfs'
data['batch']
65
data.get['pfs']
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    data.get['pfs']
TypeError: 'builtin_function_or_method' object is not subscriptable
data
{'name': 'nithin', 'course': 'pfs', 'batch': 65}
'nithin' in data
False
'name' in data
True
data.get('name')
'nithin'
data.get('batch')
65
data.get('age')
data.get('batch','key is not present')
65
data
{'name': 'nithin', 'course': 'pfs', 'batch': 65}
data[age] = 21
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    data[age] = 21
NameError: name 'age' is not defined
data['age']=21
data
{'name': 'nithin', 'course': 'pfs', 'batch': 65, 'age': 21}
data['phnno'] = 9876543210
data
{'name': 'nithin', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 9876543210}
data.update({'email':'nithin@gmail.com','py':2026})
data
{'name': 'nithin', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 9876543210, 'email': 'nithin@gmail.com', 'py': 2026}
data.popitem()
('py', 2026)
data.pop('course')
'pfs'
data.pop('email')
'nithin@gmail.com'
id(data)
2454726654592
data.popitem()
('phnno', 9876543210)
data
{'name': 'nithin', 'batch': 65, 'age': 21}
id(data)
2454726654592
del data['name']
data.clear()
data
{}
>>> data = {'name': 'nithin', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 9876543210}
>>> data
{'name': 'nithin', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 9876543210}
>>> len(data)
5
>>> data.keys()
dict_keys(['name', 'course', 'batch', 'age', 'phnno'])
>>> data.values()
dict_values(['nithin', 'pfs', 65, 21, 9876543210])
>>> data.items()
dict_items([('name', 'nithin'), ('course', 'pfs'), ('batch', 65), ('age', 21), ('phnno', 9876543210)])
>>> sorted(data)
['age', 'batch', 'course', 'name', 'phnno']
>>> max(data)
'phnno'
>>> min(data)
'age'
>>> d = {1:1,2:2}
>>> m = d
>>> m[3] = 3
>>> m
{1: 1, 2: 2, 3: 3}
>>> d
{1: 1, 2: 2, 3: 3}
>>> d = {1:1,2:2}
>>> m = d.copy()
>>> m[3] = 3
>>> m
{1: 1, 2: 2, 3: 3}
>>> d
{1: 1, 2: 2}
>>> data
{'name': 'nithin', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 9876543210}
>>> data.setdefault('py',2026)
2026
>>> data.setdefault('age',22)
21
>>> data.setfefault('key',2026)
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    data.setfefault('key',2026)
AttributeError: 'dict' object has no attribute 'setfefault'. Did you mean: 'setdefault'?
>>> data.setdefault('key',2026)
2026
>>> data
{'name': 'nithin', 'course': 'pfs', 'batch': 65, 'age': 21, 'phnno': 9876543210, 'py': 2026, 'key': 2026}
>>> dict.from{['python','mysql','java'],0}
SyntaxError: invalid syntax
>>> dict.fromkeys{['python','mysql','java'],0}
SyntaxError: invalid syntax
>>> dict.fromkeys(['python','mysql','java'],0)
{'python': 0, 'mysql': 0, 'java': 0}
