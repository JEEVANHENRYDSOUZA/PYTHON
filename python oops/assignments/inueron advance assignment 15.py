1.	What are the new features added in Python 3.8 version?

Refer the link : https://docs.python.org/3/whatsnew/3.8.html
2.	What is monkey patching in Python?
Changing the behaviour of a function at run time is called as monkey patching.
this happens because functions are first class citizens in python and the name of the function has the reference to it

3.	What is the difference between a shallow copy and deep copy?
In shallow copy both the original and the cloned have the references to the same object hence a change in one object will be reflected in both
But in deep copy two distinct objects have been created hence a changes in one will not be reflected in the other

4.	What is the maximum possible length of an identifier?

79 characters
5.	What is generator comprehension?



Because a generator expression only has to yield one item at a time, it can lead to big savings in memory usage. Generator expressions make the most sense in scenarios where you need to take one item at a time, do a lot of calculations based on that item, and then move on to the next item. If you need more than one value, you can also use a generator expression and grab a few at a time. If you need all the values before your program proceeds, use a list comprehension instead.


>>> my_list = [1, 3, 5, 9, 2, 6]
>>> filtered_list = [item for item in my_list if item > 3]
>>> print(filtered_list)
[5, 9, 6]
>>> len(filtered_list)
3
>>> # compare to generator expression
... 
>>> filtered_gen = (item for item in my_list if item > 3)
>>> print(filtered_gen)  # notice it's a generator object
<generator object <genexpr> at 0x7f2ad75f89e0>
>>> len(filtered_gen) # So technically, it has no length
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'generator' has no len()
>>> # We extract each item out individually. We'll do it manually first.
... 
>>> next(filtered_gen)
5
>>> next(filtered_gen)
9
>>> next(filtered_gen)
6
>>> next(filtered_gen) # Should be all out of items and give an error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
>>> # Yup, the generator is spent. No values for you!
... 
>>> # Let's prove it gives the same results as our list comprehension
... 
>>> filtered_gen = (item for item in my_list if item > 3)
>>> gen_to_list = list(filtered_gen)
>>> print(gen_to_list)
[5, 9, 6]
>>> filtered_list == gen_to_list
True
>>> 

