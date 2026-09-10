Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Trimming method
s = '      Hello     Nithin      '
s
'      Hello     Nithin      '
s.strip()
'Hello     Nithin'
s.lstrip()
'Hello     Nithin      '
s.rstrip()
'      Hello     Nithin'
s.replace(' ','')
'HelloNithin'

#spliting
s = 'java-python-flask-mysql-flaskapi-c'
s
'java-python-flask-mysql-flaskapi-c'
s.split('-')
['java', 'python', 'flask', 'mysql', 'flaskapi', 'c']
s.split('-',2)
['java', 'python', 'flask-mysql-flaskapi-c']
s.rsplit('-',2)
['java-python-flask-mysql', 'flaskapi', 'c']

l = '''nithin'''
l  = '''nithin
srinivas
ramprasad
ayaz
karthik
'''
l
'nithin\nsrinivas\nramprasad\nayaz\nkarthik\n'
' '.join(l)
'n i t h i n \n s r i n i v a s \n r a m p r a s a d \n a y a z \n k a r t h i k \n'
'.'.join(l)
'n.i.t.h.i.n.\n.s.r.i.n.i.v.a.s.\n.r.a.m.p.r.a.s.a.d.\n.a.y.a.z.\n.k.a.r.t.h.i.k.\n'
'@'.join(l)
'n@i@t@h@i@n@\n@s@r@i@n@i@v@a@s@\n@r@a@m@p@r@a@s@a@d@\n@a@y@a@z@\n@k@a@r@t@h@i@k@\n'
a = 'string.py'
a.partition('.')
('string', '.', 'py')
a = 'string.py.java.png.txt'
a.partition('.')
('string', '.', 'py.java.png.txt')
a.rpartition('.')
('string.py.java.png', '.', 'txt')
s = 'nithin.kumar'
s.startswith('nit')
True
s.startswith('abc')
False
s.endswith('mar')
True
s.endswith('xyz')
False
'python.13'.islower()
True
>>> 'Python.13'.islower()
False
>>> 'PYTHON.13'.isupper()
True
>>> 'PYTHON@#$123'.isupper()
True
>>> 'nithin'.isalpha()
True
>>> 'nithin123'.islower()
True
>>> 'NITHIN123'.isalpha()
False
>>> '1234'.isnum()
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    '1234'.isnum()
AttributeError: 'str' object has no attribute 'isnum'. Did you mean: 'isalnum'?
>>> 'nithin123'.isalnum()
True
>>> '13234'.isalnum()
True
>>> 'nithin@#$'.isalnum()
False
>>> '     '.isspace()
True
>>> '     nithin'.isspace()
False
>>> 'Hello Nithin'.istitle()
True
>>> 'HELlo Nithin'.istitle()
False
>>> 'my_var'.isidentifier()
True
>>> '_name'.isidentifier()
True
>>> 'my@var'.isidentifier()
False
>>> '123445'.isdecimal()
True
>>> 'Nit123'.isdecimal()
False
>>> 'ASFDFH'.isdecimal()
False
>>> '12345'.isdigit()
True
>>> '123456'.isnumeric()
True
>>> 'nithin123'.isdigit()
False
>>> '1223nithi'.isnumeric()
False
