1)	. What is the difference between enclosing a list comprehension in square brackets and parentheses?
It would become a tuple
2)	What is the relationship between generators and iterators?
                    Generator are subclass of iterator
3)	What are the signs that a function is a generator function?
Generator functions allow us to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
4) What is the purpose of a yield statement?
Converts a function to a generator function.generates a range like function

5) What is the relationship between map calls and list comprehensions? Make a comparison and contrast between the two ?
Ans: The main differences between map calls and list comprehensiosn are:
1.	List comprehension is more concise and easier to read as compared to map.
2.	List comprehension allows filtering. In map, we have no such facility. For example, to print all odd numbers in range of 50, we can write [n for n in range(50) if n%2 != 0]. There is no alternate for it in map
3.	List comprehension are used when a list of results is required as final output.but map only returns a map object. it needs to be explicitly coverted to desired datatype.
4.	List comprehension is faster than map when we need to evaluate expressions that are too long or complicated to express
5.	Map is faster in case of calling an already defined function on a set of values.
