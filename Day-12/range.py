#range(start,end+1,step):(0,,1)

''' for i in range(1,11):
    print(i)'''

''' for i in range(2,21,2):
    print(i) '''

'''for i in range(5,101,5):
    print(i) '''

''' for i in range(20,0,-1):
    print(i) '''

'''for i in range(19,0,-2):
    print(i) '''

''' s = 'Python Programming'
for i in range(len(s)):
    print(i)

s = "Python Programming"
for i in range(len(s)):
    print(i,s[i]) '''

''' s = (456,4567,4567,543,4356)
for i in range(len(s)):
    print(i)

s = (456,4567,4567,543,4356)
for i in range(len(s)):
    print(i,s[i]) '''

# enumerate = gives the sequence of number

'''s = [6789,6789,6789,7689]
for i in enumerate(s):
    print(i) '''

''' s = [6789,6789,6789,7689]
for i in enumerate(s):
    print(i[0],i[1]) '''

'''d = [6789,6789,6789,7689]
for i in enumerate(d):
    print(i[0],i[1],d[i[1]]) '''

'''for i in range(1,11):
    if i == 5:
        break
    print(i) '''

'''for i in range(1,11):
    if i == 5:
        continue
    print(i) '''

'''for i in range(1,11):
    if i == 15:
        break
    print(i)
else:
    print("End of the loop")'''

'''l = [12,13,15,16,18,19]
n = 12
for i in l:
    if i == n:
        print(n,"Found")
        break
else:
    print(n,"Not Found")'''

pin = 1234
for i in range(5):
    epin = int(input("Enter the pin: "))
    if epin == pin:
        print("Unlock phone")
        break
    else:
        print("Invalid pin")
else:
    print("Try after 30 seconds")