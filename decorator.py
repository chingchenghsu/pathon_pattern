class Tea:
        def __init__(self):
                pass
        def getCost(self):
                pass
        def getIngredient(self):
                pass

class SimpleTea(Tea):
        def __init__(self):
                self.cost =30.
                self.ingredient =" Pure Tea "

        def getCost(self):
                return self.cost  # basic ingredient 

        def getIngredient(self):
                return self.ingredient  # basic ingredient 
class TeaDecorator(Tea):
        def __init__(self, decoratedTea):
                self.simpletea = decoratedTea
        def getCost(self):
                self.simpletea.getCost()
        def getIngredient(self):
                self.simpletea.getIngredient()
class Bubble(TeaDecorator):
        def __init__(self,decoratedTea):
                self.cost = 8.
                self.ingredient =" Bubble "
                self.simpletea= decoratedTea
        def getCost(self):
                return self.cost+self.simpletea.getCost()
        def getIngredient(self):
                return self.ingredient + self.simpletea.getIngredient()

if __name__ =="__main__":
        my_simpletea = SimpleTea()
        my_package = Bubble(Milk(my_simpletea))
        my_cost = my_package.getCost()
        my_content = my_package.getIngredient()
        print my_cost
        print "We have : ", my_content
