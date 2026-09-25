'''file = open("demo.txt","r")
print(file.read())
file.seek(0)
print(file.readline())
file.seek(0)
print(file.readlines())
file.close()'''

'''with open("demo.txt","r") as file:
    print(file.read())
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())'''

#It is going to create a new file
'''with open("demos.txt","w") as file:
    file.write("Hello World")'''

#It is going to overwrite the existing file content
'''with open("demo.txt","w") as file:
    file.write("Hello World")'''

#append mode
with open("demo.txt","a") as file:
    file.write("\nfile operation")

with open("demo.txt","a+") as file:
    file.write("\nfile operation")
    file.seek(0)
    print(file.read())

with open("demo.txt","w+") as file:
    file.write("\nfile operation")
    file.seek(0)
    print(file.read())

with open("demo.txt","r+") as file:
    file.write("\nfile operation")
    file.seek(0)
    print(file.read())