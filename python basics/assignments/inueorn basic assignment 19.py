1. Make a class called Thing with no contents and print it. Then, create an object called example from this class and also print it. Are the printed values the same or different?
2. Create a new class called Thing2 and add the value 'abc' to the letters class attribute. Letters should be printed.
3. Make yet another class called, of course, Thing3. This time, assign the value 'xyz' to an instance (object) attribute called letters. Print letters. Do you need to make an object from the class to do this?
4. Create an Element class with the instance attributes name, symbol, and number. Create a class object with the values 'Hydrogen,' 'H,' and 1.
5. Make a dictionary with these keys and values: 'name': 'Hydrogen', 'symbol': 'H', 'number': 1. Then, create an object called hydrogen from class Element using this dictionary.
6. For the Element class, define a method called dump() that prints the values of the object’s attributes (name, symbol, and number). Create the hydrogen object from this new definition and use dump() to print its attributes.
7. Call print(hydrogen). In the definition of Element, change the name of method dump to __str__, create a new hydrogen object, and call print(hydrogen) again.
8. Modify Element to make the attributes name, symbol, and number private. Define a getter property for each to return its value.
9. Define three classes: Bear, Rabbit, and Octothorpe. For each, define only one method: eats(). This should return 'berries' (Bear), 'clover' (Rabbit), or 'campers' (Octothorpe). Create one object from each and print what it eats.
10. Define these classes: Laser, Claw, and SmartPhone. Each has only one method: does(). This returns 'disintegrate' (Laser), 'crush' (Claw), or 'ring' (SmartPhone). Then, define the class Robot that has one instance (object) of each of these. Define a does() method for the Robot that prints what its component objects do.
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
