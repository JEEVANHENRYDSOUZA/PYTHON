Q1. Which two operator overloading methods can you use in your classes to support iteration?

__iter__ and  __next__ 

Q2. In what contexts do the two operator overloading methods manage printing?
__str__   and  _ _repr__


Q3. In a class, how do you intercept slice operations?

Internally we use __getitem__ when we perform slice operation

Q4. In a class, how do you capture in-place addition?

__iadd__
In place addition is a+=1
Normal addition is a+b

Q5. When is it appropriate to use operator overloading?
When we add additional functionalities to the already existing methods then we should go or operator overloading

Example addition of two numbers can be performed but we cant a number and a  string hence in such scenario use operator overloading
