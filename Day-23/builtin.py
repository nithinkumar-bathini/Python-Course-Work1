# Import the sys module for system-related operations
'''import sys

print(sys.argv)
print(sys.version)
print(sys.path)
print("start")
sys.exit()
print("end")'''

# Import platform module to get system information
'''import platform

print(platform.system())
print(platform.release())
print(platform.processor())'''

# math is a built-in Python module that provides mathematical functions and constants
'''import math

print(math.pi)
print(math.e)
print(math.log(2,2))
print(math.sin(30))
print(math.cos(30))
print(math.tan(30))
print(math.degrees(30))
print(math.radians(30))
print(math.factorial(5))
print(math.gcd(8,12))
print(math.sqrt(36))
print(math.pow(2,3))'''

'''import math

print(round(12.000001))
print(round(12.3))
print(round(12.6666))
print(round(12.999999))
print(math.ceil(12.000001))
print(math.ceil(12.3))
print(math.ceil(12.66666))
print(math.ceil(12.99999))
print(math.floor(12.000001))
print(math.floor(12.3))
print(math.floor(12.6666))
print(math.floor(12.9999))'''

# random is used to generate random numbers and select random elements
#without seed
'''import random 

print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l = ['r','p','c']
print(random.choice(l))

lang = ['python','java','css','javascript','flask']
print(random.choices(lang,k=2))

random.shuffle(lang)
print(lang)'''

#with seed: Set a starting value for random number generation
'''import random 
random.seed(9)
print(random.random())
print(random.randint(1,6))
print(random.uniform(1,6))

l = ['r','p','c']
print(random.choice(l))

lang = ['python','java','css','javascript','flask']
print(random.choices(lang,k=2))

random.shuffle(lang)
print(lang)'''

# Counter is used to count how many times each element occurs
'''from collections import Counter
s = "python programming"
res = Counter(s)
print(res)'''

# defaultdict automatically provides a default value for missing keys
'''from collections import Counter,defaultdict
products = ['sugar','salt','milk']
res = defaultdict(list)
for i in products:
    res[i].append(['des','rev','com'])
print(res)'''

# deque is a double-ended queue that allows insertion and deletion from both ends
from collections import Counter, defaultdict, deque

l = deque([])
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.popleft()
l.popleft()
l.append(50)
l.append(60)
l.popleft()
print(l)

l = deque([])
l.appendleft(10)
l.appendleft(20)
l.appendleft(30)
l.appendleft(40)
l.pop()
l.pop()
l.appendleft(50)
l.appendleft(60)
l.pop()
print(l)

