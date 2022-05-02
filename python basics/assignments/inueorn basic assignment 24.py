1.	What is the relationship between def statements and lambda expressions ?
Lambda expressions also called as lambda functions are functions without name
2. What is the benefit of lambda?
The benefit of using lambda function is that they are functions without name
3.Compare and contrast map, filter, and reduce.
Filter function as the name suggest will remove out the data for which it evaluates to Boolean true
Map function all elements of an sequence which is iterable  will be converted to value evaluated by an expression
Reduce function is used to apply a particular function passed in its argument to all the elements of an interable sequence
4. What are function annotations, and how are they used?
Function annotations provide a way of associating various parts of a function with arbitrary pythoncexpressions at compile time.
Annotations of simple parameters def func(x: expression, y: expression = 20):
Whereas the annotations for excess parameters are as − def func (**args: expression, **kwargs: expression):
5. What are recursive functions, and how are they used?
When a function is calls itself it is called recursive,They are generally used Inplace of iteration
That is any iterative code can be converted to recursion and vice versa
6. What are some general design guidelines for coding functions?
Keep the name of the function such that it depicts its working
7. Name three or more ways that functions can communicate results to a caller.
a.use of the return keyword
b.yeild
c. print
