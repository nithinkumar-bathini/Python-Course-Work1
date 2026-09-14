#super method : 
'''
class whatsappv1:
    def status(self):
        print("You can upload the status fo 24hrs")

class whatsappv2(whatsappv1):
    def status(self):
        super().status()
        print("You add music and you can react")

a = whatsappv1()
a.status()

b = whatsappv2()
b.status()
'''

#this is class method
class whatsappv1:
    def status(self):
        print("You can upload the status fo 24hrs")

class whatsappv2:
    def status(self):
        print("You add music and you can react")

class whatsappv3(whatsappv1,whatsappv2):
    def status(self):
        whatsappv1.status(self)
        whatsappv2.status(self)
        print("You can add to the cross platfoms")

a = whatsappv3()
a.status()