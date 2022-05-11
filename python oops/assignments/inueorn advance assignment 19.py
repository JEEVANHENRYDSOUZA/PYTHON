Q1. What is the purpose of Python's OOP?

Code re-usebility
Provide modular function

Q2. Where does an inheritance search look for an attribute?

It will look in the class itself if not found then will search in the order top to bottom

Q3. How do you distinguish between a class object and an instance object?
Doubt question
Q4. What makes the first argument in a class’s method function special?



Q5. What is the purpose of the __init__ method?

__init__() method is used as constructor



Q6. What is the process for creating a class instance?
class jeevan:
    def __init__(self,name):
        self.name=name    
    def print_name(self):
        print(self.name)
        
    
        
    
a=jeevan("jeevan")#here I have created an instance of class jeevan
a.print_name()



Q7. What is the process for creating a class?

Use the class keyword as give below

      class jeevan :


Q8. How would you define the superclasses of a class?
class jeevan :
    def __init__(self):
        pass
class inheritance(jeevan): #heere jeevan is a superclass
