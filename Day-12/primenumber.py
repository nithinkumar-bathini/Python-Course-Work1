#check number is prime number or not
n = 13
for i in range(1,n):
    if n%i == 0:
        print("Not a prime number")
        break
else:
    print("Prime number")


#print prime numbers 1 to n
n = int(input("Enter the limit: "))
for num in range(2,n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)