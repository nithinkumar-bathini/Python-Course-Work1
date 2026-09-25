from abc import ABC,abstractmethod

class Payment(ABC):
    def source(self):
        print("Scanner/upiid/mobile number")
    def amount(self):
        print("Enter the amount")
    def bank(self):
        print("Select the bank")
    def pin(self):
        print("Enter the pin")
    @abstractmethod
    def paymentprocess(self):
        pass
    def paymentstatus(self):
        print("Payment Success/fail")

class HDFC(Payment):
    def paymentprocess(self):
        print("Payment done through HDFC Bank")
class ICIC(Payment):
    def paymentprocess(self):
        print("Payment done through ICIC Bank")
class UNION(Payment):
    def paymentprocess(self):
        print("Payment done through UNION Bank")
class AXIS(Payment):
    def paymentprocess(self):
        print("Payment done through AXIS Bank")

nithin = HDFC()
nithin.source()
nithin.amount()
nithin.bank()
nithin.pin()
nithin.paymentprocess()
nithin.paymentstatus()

srinivas = ICIC()
srinivas.source()
srinivas.amount()
srinivas.bank()
srinivas.pin()
srinivas.paymentprocess()
srinivas.paymentstatus()

ramprasad = UNION()
ramprasad.source()
ramprasad.amount()
ramprasad.bank()
ramprasad.pin()
ramprasad.paymentprocess()
ramprasad.paymentstatus()

vardhan = AXIS()
vardhan.source()
vardhan.amount()
vardhan.bank()
vardhan.pin()
vardhan.paymentprocess()
vardhan.paymentstatus()