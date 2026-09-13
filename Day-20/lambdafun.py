'''
var = lambda arg : exp
'''
'''
wish = lambda name : f"Welcome to the course {name}"
print(wish("srinivas"))
print(wish("karthik"))

gst = lambda price : price + price*0.18
print(gst(1000))
print(gst(2000))

avg = lambda a,b,c : (a+b+c)/3
print(avg(3,4,5))
print(avg(8,10,15))

iseven = lambda a : "Even" if a%2 == 0 else "Odd"
print(iseven(10))

largest = lambda a,b,c : a if a>b and a>c else (b if b>c else c)
print(largest(23,34,12))

isvowel = lambda a : "Vowel" if a in "aeiouAEIOU" else "Consonant"
print(isvowel('u'))
print(isvowel('k'))
'''

'''l = [1,2,3,4,5,6,7]
update = list(map(lambda i : i+10, l))
print(update)

t = (789,421,3453,24235,35430)
discount = list(map(lambda i : i-i*0.18,t))
print(discount)'''

'''l = [1,2,3,4,5,6,7]
update = list(filter(lambda i : i%2 != 0,l))
print(update)

t = (789,421,3453,24235,35430)
discount = list(filter(lambda i : i > 1000,t))
print(discount)'''

'''l = ['nithin@codegnan.com','nithin@gmail.com','nithin@yahoo.com','nithin@outlook.com']
domain = list(map(lambda i : i.split('@')[-1],l))
print(domain)'''

'''from functools import reduce
l = [4,2,4,64,75,2,4645,8]
res = reduce (lambda sum, i : sum + i, l)
print(res)

res1 = reduce(lambda sum,i : pro`df` * i , l)
print(res1)'''


'''seats = {'s1' : True,
         's2 ': False,
         's3' : False,
         's4' : False,
         's5' : True,
         's6' : True}
avbseats = list(filter(lambda i : seats[i]!=True,seats))
print(avbseats)'''

'''products = {
    'eggs' : 80,
    'sugar' : 60,
    'salt' : 20,
    'butter' : 40,
    'milk' : 30
}
res1 = list(filter(lambda i : products[i]>50,products))
print(res1)'''

products = {
    'eggs' : 80,
    'sugar' : 60,
    'salt' : 20,
    'butter' : 40,
    'milk' : 30
}
print(dict(sorted(products.items(),key = lambda i : i[1])))
print(dict(sorted(products.items(),key = lambda i : i[1],reverse=True)))

