Q1. Define the relationship between a class and its instances. Is it a one-to-one or a one-to-many partnership, for example?
We can  create many instances of the same class so it is one to many
Q2. What kind of data is held only in an instance?
Data which is only related to the instance of the object I supposed to be stored as an instance variable
Q3. What kind of knowledge is stored in a class?
Classes are basically a blue print of the object
Q4. What exactly is a method, and how is it different from a regular function?
Functions defined inside of a class are called as methods .
Q5. Is inheritance supported in Python, and if so, what is the syntax?
Yes python supports  inheritance
class name:
    def __init__(self):
        print("jeevan")
        
        
        
class jeevan(name):
    pass

class jeevan inherits class name
or class jeevan is the childclass and the class name is the parent class
Q6. How much encapsulation (making instance or class variables private) does Python support?
Python does not have private variables but it supports encapsulation by following a convention. In python everything is public
Q7. How do you distinguish between a class variable and an instance variable?
Class variable are those which are not defined inside any method and __init__
Instance variable are those which are related to the instance and which are defined in the __init__ method

class person:
    jeevan=1 #this is a class attribute
    def __init__(self,firstname,lastname):
        self.firstname=firstname #this is an instance attribute
        self.lastname=lastname#this is an instance attribute
        print(self.firstname) #this is an instance attribute
print(self.lastname) #this is an instance attribute
    

Q8. When, if ever, can self be included in a class's method definitions?
Yes it can be included to access instance variables in the method
Q9. What is the difference between the _ _add_ _ and the _ _radd_ _ methods?
Python will first try __add__(), and if that returns Not Implemented Python will check if the right-hand operand implements __radd__, and if it does, it will call __radd__() rather than raising a TypeError
Q10. When is it necessary to use a reflection method? When do you not need it, even though you support the operation in question?

Q11. What is the _ _iadd_ _ method called?
__iadd__ is called when we do inplace addition as a+=1--a=a+1
Q12. Is the _ _init_ _ method inherited by subclasses? What do you do if you need to customize its behavior within a subclass?
Yes the subclass does inherit the parent class’s __init__ use super(childclass,self).__init__() to access it .
