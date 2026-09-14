data = {
    123456 : {'name':'Nithin','pin':1234,'balance':5000,'history':[]},
    234561 : {'name':'Karthik','pin':2345,'balance':6000,'history':[]},
    345612 : {'name':'Vishnu','pin':3456,'balance':7000,'history':[]},
    456123 : {'name':'Ramprasad','pin':4567,'balance':8000,'history':[]},
    561234 : {'name':'Srinivas','pin':5678,'balance':9000,'history':[]}
}

def login():
    global acc_num
    acc_num = int(input("Enter the account number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]['pin'] == pin:
        print("Login Successfull")
        return True
    else:
        print("Invalid Login")

def menu():
    print(f"Welcome to the ATM, {data[acc_num]['name']}")
    print("[C]heck Balance")
    print("[D]eposit")
    print("[W]ithdraw")
    print("[v]iew Transaction")
    print("[E]xit")

def checkbalance():
    print(f"Hello {data[acc_num]['name']}")
    print("Current Balance: ",data[acc_num]['balance'],end='\n\n')

def deposit():
    amount = int(input(("Enter the Amount to deposit:")))
    data[acc_num]["balance"] += amount
    data[acc_num]["history"].append(f"{amount} is deposited")
    print(f"{amount} is Deposited Successfully")
    checkbalance()

def withdraw():
    amount = int(input("Enter the amount to Withdraw: "))
    if data[acc_num]["balance"] >= amount:
        data[acc_num]["balance"] -= amount
        data[acc_num]["history"].append(f"{amount} is Withdraw")
        print(f"{amount} is withdraw Successfully")
    else:
        print("Insufficient Balance")

def viewtransaction():
    if data[acc_num]["history"]:
        print("===== Transaction History =====")
        for i in data[acc_num]["history"]:
            print(i)
        else:
            print("===== End of the History =====")
    else:
        print("No Transaction History")

