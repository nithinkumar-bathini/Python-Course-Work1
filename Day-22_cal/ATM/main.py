import logic as atm

atm.login()
while True:
    atm.menu()
    ch = input("Enter the choice: ").upper()
    if ch == 'C':
        atm.checkbalance()
    elif ch == 'D':
        atm.deposit()
    elif ch == 'W':
        atm.withdraw()
    elif ch == 'V':
        atm.viewtransaction()
    elif ch == 'E':
        print("---------------Thankyou, visit again------------")
        break
    else:
        print("Enter the valid choice")