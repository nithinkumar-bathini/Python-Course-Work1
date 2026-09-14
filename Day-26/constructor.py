# Constructor : Constructor is a special method it calls automatically
class Instagram:
    def __init__(self,username,password):
        self.username = username
        self.password = password
        print(f"Welcome to Instagram, {self.username}")
        print()

nithin = Instagram('Nithin','1234567')
srinivas = Instagram('Srinivas','7654321')
vardhan = Instagram('Vardhan','45675432')