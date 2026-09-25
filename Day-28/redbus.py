class Redbus:
    bus = {i : "Available" for i in range(1,11)}

    def dissplayseats(self):
        print("-----------Redbus------------")
        for i in Redbus.bus:
            print(i,Redbus.bus[i])
            
    def booking(self,seatno):
        for i in Redbus.bus:
            if i == seatno and Redbus.bus[i] == 'Available':
                Redbus.bus[i] = 'Booked'
                print(f"Your seat - {seatno} is successfully Booked")
                return True
        else:
            print(f"Your seat -{seatno} already booked")
            return False

class users(Redbus):
    def __init__(self,name,email,phno):
        self.name = name
        self.email = email
        self.phno = phno
        print(f"Hello {self.name}, Welcome to the Redbus")

class Driver(users):
    def __init__(self,dname,dphno):
        self.dname = dname
        self.dphno = dphno
        print(f"Your Driver Name - {dname} and {dphno}")

nithin = users('Nithin','nithin@gmail.com',987654321)
nithin.dissplayseats()
if nithin.booking(4):
    srinivas = Driver("Srinivas", 9876543456)
else:
    print("Please Book another seat")
ramprasad = users('Ramprasad','ramprasad@gmail.com',987654321)
nithin.dissplayseats()
if nithin.booking(4):
    srinivas = Driver("Srinivas", 9876543456)
else:
    print("Please Book another seat")

