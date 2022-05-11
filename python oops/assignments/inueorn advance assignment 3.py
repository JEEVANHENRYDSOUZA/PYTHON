1. What is the concept of an abstract superclass?

An abstract class/superclass can be considered as a blueprint for other classes. It allows you to create a set of methods that must be created within any child classes built from the abstract class. A class which contains one or more abstract methods is called an abstract class.
Whereas an abstract method is a method that has a declaration but does not have an implementation


2. What happens when a class statement's top level contains a basic assignment statement?
When a class statements’s top level contains a basic assignment statement it is called as a class attribute and it is not related to the instance of the class .it can be accessed throughout the class



3. Why does a class need to manually call a superclass's __init__ method?
During inherit when we have __init__ method present in the parent as well as in the child,when we create an instance of the child then the childs __init__ method will be called.this is hpw python resolves methods.hence if we want to use the parents __init__ method we will have to manually call it



4. How can you augment, instead of completely replacing, an inherited method?
Use super()


5. How is the local scope of a class different from that of a function?
When we define a  variable inside a function it is called as a local variable meaning it is not available to any other functions
When we define a variable outside all methods then it is called as a class variable and it can be accessed by any method present in the class in which we have defined it
