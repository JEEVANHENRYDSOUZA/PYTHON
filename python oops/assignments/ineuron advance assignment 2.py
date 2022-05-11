Q1. What is the relationship between classes and modules?

A module is .py file which can contain a class 

Q2. How do you make instances and classes?

class jeevan:
    class_var=1#this is a class variable
    def __init__(self): #in this we create an instance of the object
        self.book=0;#this is an instance attribute


Q3. Where and how should be class attributes created?
class jeevan:
    class_var=1#this is a class variable
    def __init__(self):
        self.book=0;#this is an instance attribute



Q4. Where and how are instance attributes created?

class jeevan:
    def __init__(self):
        self.book=0;#this is an instance attribute


Q5. What does the term "self" in a Python class mean?
Self keyword indicates the current object that it is working on 



Q6. How does a Python class handle operator overloading?
in Python, overloading is achieved by overriding the method which is specifically for that operator, in the user-defined class. For example, __add__(self, x) is a method reserved for overloading + operator, and __eq__(self, x) is for overloading ==.


Operator overloading means provided extended meaning than beyond what is already defined

Q7. When do you consider allowing operator overloading of your classes?
Operator overloading means provided extended meaning than beyond what is already defined


Q8. What is the most popular form of operator overloading?
When add two string thus based on the type of the object corresponding method gets called



Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code?
Class and objects
