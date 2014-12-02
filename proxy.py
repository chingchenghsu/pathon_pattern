class SchoolGirl:
        def __init__(self,a,b):
                self.age = a
                self.name=b

class GiveGift:
        def __init__(self):
                pass
        def GiveFlower(self):
                pass
        def GiveDoll(self):
                pass
        def GiveCandy(self):
                pass
class Pursuiter(GiveGift):
        def __init__(self, gg):
                self.girl = gg
        def GiveFlower(self):
                print self.girl.name, ", I love you, I want to give you a Flower!"
        def GiveDoll(self):
                print self.girl.name, ", I love you, I want to give you a Doll!" 
        def GiveCandy(self):
                print self.girl.name, ", I love you, I want to give you a Candy!
                
                
                class Proxyer(GiveGift):
        def __init__(self,a,b,mygirl):
                self.age = a
                self.name = b
                self.mypursuiter = Pursuiter(mygirl)
                self.mypursuiter.girl = mygirl
        def GiveFlower(self):
                self.mypursuiter.GiveFlower()
        def GiveDoll(self):
                self.mypursuiter.GiveDoll()
        def GiveCandy(self):
                self.mypursuiter.GiveCandy()

if __name__ =="__main__":
        Mary = SchoolGirl(26,"Mary Lee")
        myproxyer = Proxyer(30,"John Huang",Mary)
        myproxyer.GiveFlower()
        myproxyer.GiveDoll()
        myproxyer.GiveCandy()
        print "But I am ", myproxyer.name, ", I am just a proxy of my boss !!"

