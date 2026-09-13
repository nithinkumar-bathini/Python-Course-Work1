#Print Numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

#Print Numbers from 10 to 1
i = 10
while i > 0:
    print(i)
    i -= 1

#Print Multiples of 5 from 5 to 50
i = 5
while i <= 50:
    print(i)
    i += 5

#Print a String
s = 'while loop'
i = 0
while i<len(s):
    print(s[i])
    i += 1

#Print a String in Reverse Order
s = 'while loop'
i = len(s)-1
while i >= 0:
    print(s[i])
    i -= 1

#Print All Elements of a List Using a While Loop
l = [5467,5678,6789,987]
i = 0 
while i < len(l):
    print(l[i])
    i += 1

#print numbers in reverse order
n = 8765
while n>0:
    print(n%10)
    n//=10

#sum of digits
n = 98765432456
sumofdigits = 0
while n>0:
    sumofdigits += n%10
    print(sumofdigits)
    n //= 10
print("Sum of digits: ",sumofdigits)

#product of digits of a number
n = 98765432456
productofdigits = 1
while n > 0:
    productofdigits *= n%10
    n//=10
print("product of digits: ",productofdigits)


#reverse a number
n = 34567
res = 0
while n > 0:
    rem = n%10
    res = res*10+rem
    n//=10
print(res)

#print sum of their even numbers
n = 876543456
res = 0
while n > 0:
    rem= n%10
    if rem%2 == 0:
        res += rem
    n//=10
print(res)

#remove 0's and print
l = [7,9,23,0,0,0,12,0,13,0,1,0,4,0,1,0,0,1,4,5,6,6,13,0]
while 0 in l:
    l.remove(0)
print(l)

#Sum Elements from Both Ends of a List
l = [2,3,6,76,12,4,1,5,61,4,5,2,23]
i,j = 0, len(l)-1
while i <= j:
    if i == j:
        print(l[i])
    else:
        print(l[i]+l[j])
    i+=1
    j-=1

#bill generation
data = {
    'sugar' : 50,
    'salt' : 30,
    'cooking oil':90,
    'chilli powder': 70,
    'eggs':70,
    'peanuts':85,
    'rice':130,
    'butter':130,
    'bread':200,
    'wheatfloor': 100
}
bill = 0
while True:
    product = input("Enter the product name or [E]xit: ")
    if product == 'E' or product == 'e':
        print("Thanks for shopping")
        print("Total bill:",bill)
        break
    else:
        quantity = int(input("Enter the quantity: "))
        bill += data[product]*quantity