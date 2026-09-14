import random

name = input("Enter the name: ").title()
dob = input("Enter the DOB[DD-MM-YYYY]:")
spc = ['@','!','#','$','%','&','*','+','.',',']

password = name + random.choice(spc) + dob[-4:]

print("Generated Password:",password)
