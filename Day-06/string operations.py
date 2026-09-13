Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#how to declare str
s = "Codegnan"
s
'Codegnan'
type(s)
<class 'str'>
# empty str
s = ''
s
''

#string concatination
a = 'python'
b = 'programming'
a+b
'pythonprogramming'
'*'*20
'********************'
'-codegnan-'*5
'-codegnan--codegnan--codegnan--codegnan--codegnan-'
'-Nithin-'*5\n
SyntaxError: unexpected character after line continuation character
'-Nithin-'*5/n
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    '-Nithin-'*5/n
NameError: name 'n' is not defined
#slicing
name = 'nithin ayaz ramprasad srinivas karthik'
names = 'nithin ayaz ramprasad srinivas karthik'
names
'nithin ayaz ramprasad srinivas karthik'
names[::]
'nithin ayaz ramprasad srinivas karthik'
names[:6]
'nithin'
names[7:12]
'ayaz '
names[12:21]
'ramprasad'
names[22:30]
'srinivas'
names[31:37]
'karthi'
names[-1:-7]
''
names[:-7]
'nithin ayaz ramprasad srinivas '
names[-7:]
'karthik'
names[::-1]
'kihtrak savinirs dasarpmar zaya nihtin'
names[:6:1]
'nithin'
names[:6:2]
'nti'
names[::2]
'nti yzrmrsdsiia ati'
"nithin" in names
True
"ramprasad" not in names
False
"prabhas" in names
False
"mahesh" not in names
True

ord("a")
97
chr(97)
'a'

ord("A")
65
chr(65)
'A'
ord(1)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    ord(1)
TypeError: ord() expected string of length 1, but int found
chr(1)
'\x01'
chr(10)
'\n'
chr(20)
'\x14'
chr(30)
'\x1e'
ord("nithin")
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    ord("nithin")
TypeError: ord() expected a character, but string of length 6 found
ord("n")
110
ord('ni')
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    ord('ni')
TypeError: ord() expected a character, but string of length 2 found
 sorted(names)
 
SyntaxError: unexpected indent
sorted(names)
[' ', ' ', ' ', ' ', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'd', 'h', 'h', 'i', 'i', 'i', 'i', 'i', 'k', 'k', 'm', 'n', 'n', 'n', 'p', 'r', 'r', 'r', 'r', 's', 's', 's', 't', 't', 'v', 'y', 'z']
max(names)
'z'
min(names)
' '
sort(names)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    sort(names)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
names
'nithin ayaz ramprasad srinivas karthik'
len(names)
38
len[0]
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    len[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
len(names[1])
1

#case conversion method
s = "python Programming language"
s
'python Programming language'
s.upper()
'PYTHON PROGRAMMING LANGUAGE'
s.lower()
'python programming language'
s.swapcase()
'PYTHON pROGRAMMING LANGUAGE'
s.capitalize()
'Python programming language'
s.join()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.join()
TypeError: str.join() takes exactly one argument (0 given)
s.title()
'Python Programming Language'
"AaBbCcDdEeFfGgHhIiJjKk".casefold()
'aabbccddeeffgghhiijjkk'
"AaBbCcDdEeFfGgHhIiJjKk".casefold().upper()
'AABBCCDDEEFFGGHHIIJJKK'

# alinement methods
s
'python Programming language'
s.center(50,"-")
'-----------python Programming language------------'
s.ljust(40,"+")
'python Programming language+++++++++++++'
s.rjust(40,"/")
'/////////////python Programming language'
'123'.zfill(4)
'0123'
'13'.zfill(10)
'0000000013'
'234567'.zfill(3)
'234567'

#finding and index
s
'python Programming language'
s.find("p")
0
s.find("python")
0
s.find(e)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    s.find(e)
NameError: name 'e' is not defined
>>> s.find("e")
26
>>> s.index("e")
26
>>> s.rfind("e")
26
>>> s.find('o')
4
>>> s.rfind('o')
9
>>> 
>>> #replace
>>> s
'python Programming language'
>>> s.replace('o','z')
'pythzn Przgramming language'
>>> s.replace('g','1')
'python Pro1rammin1 lan1ua1e'
>>> s.maketrance('aeiou','@#$%^')
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s.maketrance('aeiou','@#$%^')
AttributeError: 'str' object has no attribute 'maketrance'. Did you mean: 'maketrans'?
>>> s.maketrans('aeiou','@#$%^')
{97: 64, 101: 35, 105: 36, 111: 37, 117: 94}
>>> s.translate(s.maketrans('aeiou','@#$%^'))
'pyth%n Pr%gr@mm$ng l@ng^@g#'
>>> 
>>> #encode and decode
>>> 
>>> text = "Hello "
>>> text.code()
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    text.code()
AttributeError: 'str' object has no attribute 'code'. Did you mean: 'encode'?
>>> text.encode()
b'Hello '
>>> b'Hello '.decode()
'Hello '
>>> text = '@#$'
>>> text.encode()
b'@#$'
>>> '@#$'.decode()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    '@#$'.decode()
AttributeError: 'str' object has no attribute 'decode'. Did you mean: 'encode'?
