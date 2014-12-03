class WorkExperience:
        def __init__(self,workdate,company):
                self.workdate = workdate
                self.company=company
class Resume:
        def __init__(self,name):
                self.name =name

        def SetPersonInfo(self,sex,age):
                self.sex=sex
                self.age =age
        def SetWorkExperience(self,date,company):
                self.mywork = WorkExperience(date,company)
                self.mywork.workdate = date
                self.mywork.company = company
        def PrintOut(self):
                print " Person: ",self.name," ",self.sex," ", self.age
                print " Working Experience:  ",self.mywork.workdate," ",self.mywork.company
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
