Python 3.14.0 (tags/v3.14.0:ebf955d, Oct  7 2025, 10:15:03) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.

===================================================== RESTART: C:/Users/nithi/OneDrive/Desktop/Python-Course-Work/Day-2/keywords.py ====================================================
Traceback (most recent call last):
  File "C:/Users/nithi/OneDrive/Desktop/Python-Course-Work/Day-2/keywords.py", line 3, in <module>
    print(keyword.kwkist)
AttributeError: module 'keyword' has no attribute 'kwkist'. Did you mean: 'kwlist'?
>>> 
===================================================== RESTART: C:/Users/nithi/OneDrive/Desktop/Python-Course-Work/Day-2/keywords.py ====================================================
Traceback (most recent call last):
  File "C:/Users/nithi/OneDrive/Desktop/Python-Course-Work/Day-2/keywords.py", line 3, in <module>
    print(keyword.kwkist)
AttributeError: module 'keyword' has no attribute 'kwkist'. Did you mean: 'kwlist'?
>>> 
===================================================== RESTART: C:/Users/nithi/OneDrive/Desktop/Python-Course-Work/Day-2/keywords.py ====================================================
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
35
>>> a=b=c=10
>>> a
10
>>> b
10
>>> c
10
>>> a,b,c = 10,20,30
>>> a
10
>>> b
20
>>> c
30
>>> a,b = 10,20
>>> a
10
>>> b
20
>>> a,b = b,a
>>> a
20
>>> b
10
>>> del a
>>> a
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    b
NameError: name 'b' is not defined
