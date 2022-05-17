
Q1. What is the meaning of multiple inheritance?
Multiple inheritance occurs when we inherit features from more than one parent


Q2. What is the concept of delegation?

Delegation provides a proxy object for any class thay you want on top of the main class. its like a wrapper to your class so that you can access limited resources of the main class.
it Wraps the object of main class into a smaller object with limited access
Simply Delegation means that you can include a instance of another class as an instance variable, and forward messages to the instance.


Q3. What is the concept of composition?

We use composition when we want to describe a has a relationship .in other words it so happen that we do nat want to use all the methods present in the parent class we only want to use some  or pick methods according to our needs .at this time we should go for inheritance

Q4. What are bound methods and how do we use them?
A bound method is the one which is dependent on the instance of the class as the first argument.


Q5. What is the purpose of pseudoprivate attributes?
pseudoprivate attributes are also useful in larger frameworks or tools, both to avoid introducing new method names that might accidentally hide definitions elsewhere in the class tree and to reduce the chance of internal methods being replaced by names defined lower in the tree. If a method is intended for use only within a class that may be mixed into other classes, the double underscore prefix ensures that the method won't interfere with other names in the tree, especially in multiple-inheritance scenarios
Pseudoprivate names also prevent subclasses from accidentally redefining the internal method's names,

