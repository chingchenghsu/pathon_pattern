class Person:
        def __init__(self):
                pass
        def Legs(self):
                print "Have Legs"
        def Eyes(self):
                print "Have Eyes"
        def Nose(self):
                print "Have Nose"
        def Hands(self):
                print "Have Hands"

class TallPerson(Person):
        def __init__(self):
                print "create tall person"
        def Legs(slef):
                print "The legs are tall"

class HighNosePerson(Person):
        def __init__(self):
                print "create high nose person"
        def Nose(self):
                print "The nose is high"
class PersonDirector:
        def __init__(self, person):
                self.thisperson = person
                print "Now I try to create person"
        def Create(self):
                self.thisperson.Eyes()
                self.thisperson.Nose()
                self.thisperson.Legs()
                self.thisperson.Hands()
                print "Person Creation is Done !"

if __name__=="__main__":
        myperson = HighNosePerson()
        myperson_director = PersonDirector(myperson)
        myperson_director.Create();
