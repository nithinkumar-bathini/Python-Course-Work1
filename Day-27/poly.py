#method overridding

class Hotstar:
    def __init__(self,name):
        print(f'Welcome to the Hotstar, {name}--------------')
    def auth(self):
        print("You can login/register")
    def dashboard(self):
        print("You can see the dashboard")
    def search(self):
        print("You can search")
    def history(self):
        print("You can see the history")
    def playcontrollers(self):
        print("Play start pause")
    def ads(self):
        print("You can see ads")
    def quality(self):
        print("You can see low quality")
    def device(self):
        print("Single device")
    def access(self):
        print("Limited access")
    def download(self):
        print("You can't dowmload")

class PremiumHotstar(Hotstar):
    def __init__(self, name):
        print(f'Welcome to the Premium Hotstar, {name}-------------')
    def ads(self):
        print("You won't see ads")
    def quality(self):
        print("You can see high quality")
    def device(self):
        print("Multiple device")
    def access(self):
        print("Unlimited access")
    def download(self):
        print("You can dowmload")

nithin = Hotstar("Nithin")
nithin.auth()
nithin.dashboard()
nithin.search()
nithin.history()
nithin.playcontrollers()
nithin.ads()
nithin.quality()
nithin.device()
nithin.access()
nithin.download()

srinivas = PremiumHotstar("Srinivas")
srinivas.auth()
srinivas.dashboard()
srinivas.search()
srinivas.history()
srinivas.playcontrollers()
srinivas.ads()
srinivas.quality()
srinivas.device()
srinivas.access()
srinivas.download()
