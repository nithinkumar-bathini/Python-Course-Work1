#Single Inheritance
'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24hrs")

nithin = whatsappv1()
nithin.message()

srinivas = whatsappv2()
srinivas.message()
srinivas.status()
'''

#Multilevel Inheritance
'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24hrs")

class whatsappv3(whatsappv2):
    def groups(self):
        print("You can create group and talk with multiple")

nithin = whatsappv1()
nithin.message()

srinivas = whatsappv2()
srinivas.message()
srinivas.status()

vardhan = whatsappv3()
vardhan.message()
vardhan.status()
vardhan.groups()
'''

#Multiple or Hybrid Inheritance
'''
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24hrs")

class whatsappv3:
    def groups(self):
        print("You can create group and talk with multiple")

class whatsappv4:
    def community(self):
        print("You can multiple groups")

class whatsappv5(whatsappv4,whatsappv3,whatsappv2):
    def channels(self):
        print("You can post regulary with huge crowd")

nithin = whatsappv1()
nithin.message()

srinivas = whatsappv2()
srinivas.message()
srinivas.status()

vardhan = whatsappv3()
vardhan.groups()

karthik = whatsappv5()
karthik.message()
karthik.status()
karthik.groups()
karthik.community()
karthik.channels()
'''

#Hierarchical Inheritance
class whatsappv1:
    def message(self):
        print("You can send a message")

class whatsappv2(whatsappv1):
    def status(self):
        print("You can upload status for 24hrs")

class whatsappv3(whatsappv1):
    def groups(self):
        print("You can create group and talk with multiple")

nithin = whatsappv1()
nithin.message()

srinivas = whatsappv2()
srinivas.message()
srinivas.status()

ramprasad = whatsappv3()
ramprasad.message()
ramprasad.groups()