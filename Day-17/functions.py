'''
def functionname(arg):
    #stsmt
    return  (optional)

    
functionname(parameter)
'''

'''def get(price):
    print("Original Price:",price)
    print("Total Price:",price+price*0.18)

get(1000)
get(5000)
get(800)
get(500)
get(10000)'''



'''def table(n):
    print(f'{n}-Table')
    print("--------------------")
    for i in range(1,11):
        print(f'{n} * {i} = {n*i}')

for i in range(1,21):
    table(i)'''


'''def isleap(year):
    if year%400 == 0 or (year%4 == 0 and year%100 != 0):
        return "Leap Year"
    else:
        return "Not a Leap Year"

print(isleap(2004))
print(isleap(2020))
print(isleap(2026))'''

'''def isprime(n):
    for i in range(2,n//2+1):
        if n%i == 0:
            return "Not a Prime Number"
    return "Prime Number"

print(isprime(5))'''


'''def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Pass:",pwd)
display("nithin","nithin@gmail.com","nithin@123")
display("nithin@gmail.com","nithin","nithin@123")
display("nithin@123","nithin","nithin@gmail.com")'''


'''def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Pass:",pwd)
display(name = "nithin",email = "nithin@gmail.com",pwd = "nithin@123")
display(email = "nithin@gmail.com",name = "nithin",pwd = "nithin@123")
display(pwd = "nithin@123",name = "nithin",email = "nithin@gmail.com")'''

'''def display(name,email,pwd="None"):
    print("Name:",name)
    print("Email:",email)
    print("Pass:",pwd)
display("nithin","nithin@gmail.com")
display("nithin","nithin@gmail.com","nithin@123")'''

'''def display(*names):   # * = prints tuple values
    print(names)
display("nithin")
display("srinivas","karthik")
display("nithin","srinivas","kathik")'''

def display(**names):   # ** = prints dictionary values
    print(names)
display(n1 = "nithin")
display(n1 = "nithin", n2 = "teja")