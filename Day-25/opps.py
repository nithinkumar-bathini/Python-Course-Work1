'''class Flipkart:
    pass


nithin = Flipkart()
srinivas = Flipkart()
karthik = Flipkart()'''

'''class Flipkart:
    def info(self,name,phno,address):
        self.name = name
        self.phno = phno
        self.address = address
        print(f"Welcome to the Flipkart {self.name}")

nithin = Flipkart()
nithin.info('Nithin',830986123,'Hyd')
srinivas = Flipkart()
srinivas.info('Srinivas',6978347442,'AP')'''


class Flipkart:
    discount = 30

    @classmethod
    def updatediscount(cls):
        cls.discount = 40
        print(f"Updated Discount: {cls.discount}")

    def info(self,name,phno,address):
        self.name = name
        self.phno = phno
        self.address = address
        print(f"Welcome to the Flipkart {self.name}")

    @staticmethod
    def banner():
        print(f"{Flipkart.discount}% discount is going, grap the discount")

nithin = Flipkart()
nithin.info('Nithin',830986123,'Hyd')
nithin.updatediscount()
nithin.banner()
srinivas = Flipkart()
srinivas.info('Srinivas',6978347442,'AP')
srinivas.updatediscount()
srinivas.banner()