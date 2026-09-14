'''
private -> inclass, childclass, outside
public -> inclass
protector -> inclass, childclass, outside (not recomm)
'''
# "__" : double underscore is for private
# "_" : single underscore is for protector

class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.__password = password
        self._post = []

    def getpassword(self):
        return self.__password

    def setpassword(self,password):
        self.__password = password

    @property
    def accesspost(self):
        return self._post

    @accesspost.setter
    def accesspost(self,newpost):
        return self._post.append(newpost)

nithin = Instagram('Nithin','1234567')

print(nithin.username)
print(nithin.getpassword())
print(nithin.accesspost)

nithin.username = 'nithin_123'
print(nithin.username)

nithin.setpassword = 'nithin123'
print(nithin.getpassword())

nithin.accesspost = 'python intro'
nithin.accesspost = 'string'
nithin.accesspost = 'project'
print(nithin.accesspost)
