'''fa = eval(input("Follows Account: "))
if fa:
    cf = eval(input("Close Friend: "))
    if cf:
        print("Story Visible")
    else:
        print("Not in Close Friends List")
else:
    print("Follow the Account First")'''


'''reg = eval(input("Registered: "))
if reg:
    fee = eval(input("Fee Paid: "))
    if fee:
        print("Tournament Entry Confirmed")
    else:
        print("Entry Fee Pending")
else:
    print("Registration Required")'''

'''link = eval(input("Enter Link: "))
if link:
    pg = eval(input("Enter Permission: "))
    if pg:
        print("Accesed")
    else:
        print("Access Denined")'''

data = {
    'nithin':{'status':True,'python':90,'mysql':94,'flask':96},
    'srinivas':{'status':True,'python':89,'mysql':83,'flask':79},
    'ayaz':{'status':False,'python':None,'mysql':None,'flask':None},
    'ramprasad':{'status':True,'python':83,'mysql':79,'flask':80},
    'karthik':{'status':True,'python':90,'mysql':89,'flask':79}
}

name = input("Enter the name: ")
if name in data:
    if data[name]['status']:
        sum = data[name]['python'] + data[name]['mysql'] + data[name]['flask']
        avg = sum/3
        print(f"Hello {name}!!!")
        print(f"Your average score is {avg}")
        if avg >= 90:
            print("Outstanding Performance")
        elif avg >= 80:
            print("Very Good")
        elif avg >= 70:
            print("Good, Work Hard")
        elif avg >= 35:
            print("Better luck next time")
        else:
            print("You Failed the exam, try hard")
    else:
        print(f'{name} did not attend the exam, bring your parents')
else:
    print(f'{name} not found')