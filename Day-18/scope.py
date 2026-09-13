#local variable: variable decared inside and acess only inside the function
'''def display():
    n = 10 
    print("Inside function: n")
display()
print("Outside function: ",n)'''

#global variable: variable declared outside and acess full function
'''def display(): 
    print("Inside function:",n)659
n = 10
display()
print("Outside function:",n)'''

#global keyword 
'''def display():
    global n        
    n = 10 
    print("Inside functiomn:",n)
display()
print("Outside function:",n)'''

'''def display():
    global n 
    n+=10
    print("Inside function:",n)
n = 10
display()
print("Outside function:",n)'''

'''def display():
    course = "PFS"
    def update():
        course = "JFS"
        print("Inner function:",course)
    update()
    print("Outer function:",course)
display()'''

'''def display():
    course = "PFS"
    def update():
        nonlocal course  #nonlocal used for outside function
        course = "JFS"
        print("Inner function:",course)
    update()
    print("Outer function:",course)
display()'''

'''l = [1,2,3,4,5]
print(sum(l))
sum = 20
print(sum)

l = [1,2,3,4,5]
print(max(l))
max = 20
print(max)'''

