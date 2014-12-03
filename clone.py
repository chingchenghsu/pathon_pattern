class Resume:
        def __init__(self,name):
                self.name =name

        def SetPersonInfo(self,sex,age):
                self.sex=sex
                self.age =age
        def SetWorkExperience(self,timearea,company):
                self.timearea=timearea
                self.company=company
        def PrintOut(self):
                print " Person: ",self.name," ",self.sex," ", self.age
                print " Working Experience:  ",self.timearea," ",self.company

        def Clone(self):
                return self
if __name__ =="__main__":

        resume1 = Resume("John Huang");
        resume1.SetPersonInfo("M",30);
        resume1.SetWorkExperience("1998-2000","IBM");
        resume1.PrintOut()

        resume2 =resume1.Clone();
        resume2.SetWorkExperience("2000-2005","Google");
        resume2.PrintOut()
