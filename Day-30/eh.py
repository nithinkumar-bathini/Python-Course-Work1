'''try:
    d = {1:1,2:2,3:3}
    print(d[5]) #KeyError
    print("a"+7) #TypeError
    print(n) #NameError
    a = int(input("Enter the number: ")) #ValueError
    l = [1,2,3,4]
    print(l[5]) #IndexError
    print(10/0) #ZeroDivisionError
except Exception as e:
    print("Error Occured: ",e)
else:
    print("No errors")
finally:
    print("End of the Program")'''

'''except (TypeError,NameError,ValueError,IndexError,ZeroDivisionError,KeyError) as e:
    print("Error Occured: ",e)'''

try:
    amount = int(input("Enter the amount: "))
    if amount < 0 :
        raise Exception("Amount needs to be greater then 0")
except Exception as e:
    print("Error Occured: ",e)
else:
    print("No errors")
finally:
    print("End of the Program")


    