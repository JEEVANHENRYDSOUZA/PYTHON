class things:
    print("hi")
    def __init__(self):
        pass
        
object1=things() 

class ofcourrsething3:
    def __init__(self):
        self.letters="abc"
        print(self.letters)
        
        
object2=ofcourrsething3()



class elemement:
    def __init__(self,symbol,element,number):
        self.symbol=symbol
        self.element=element
        self.number=number
        print(self.symbol)
        print(self.element)
        print(self.number)
        
object3=elemement('h', 'hydrogen', 1)


dictionary={'name':'hydrogen','symbol':'h','number':2}
class elemement3:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
        print(self.name)
        print(self.symbol)
        print(self.number)
        
    def dump(self):
        print(self.name)
        print(self.symbol)
        print(self.number)
        
object4=elemement3(**dictionary)
object4.dump()

class elemements3:
    def __init__(self,name,symbol,number):
        self.name=name
        self.symbol=symbol
        self.number=number
        print(self.name)
        print(self.symbol)
        print(self.number)
        
    def __str__(self):
        print(self.name)
        print(self.symbol)
        print(self.number)
        
object4=elemements3(**dictionary)
object4.__str__()




class elemementprivate:
    def __init__(self,name,symbol,number):
        self._name=name
        self._symbol=symbol
        self._number=number
        
        
    @property
    def name(self):
        return (self.__name)
    @property
    def symbol(self):
        return (self.__symbol)
    @property
    def number(self):
        return (self.__number)
        
object4=elemementprivate(**dictionary)






class bear:
    def eats():
        print("berris")
class octhropour:
    def eats():
        print("humans")
class rabbit:
    def eats():
        print("carrots")
        
        
bear.eats()
octhropour.eats()
rabbit.eats()


class Laser:
    def does(self):
        return('disitegrate')
class Claw:
    def does(self):
        return('crush')
class SmartPhone:
    def does(self):
        return('ring')
        
class Robot:
    def __init__(self):
        self.laser = Laser()
        self.claw = Claw()
        self.smartphone = SmartPhone()
    def does(self):
        return ('Laser is %s, Claw is %s, SmartPhone is %s' % (self.laser.does(),self.claw.does(),self.smartphone.does()))

r = Robot()
print(r.does())