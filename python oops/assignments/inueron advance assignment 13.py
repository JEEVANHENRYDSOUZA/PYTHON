Q1. Is an assignment operator like += only for show? Is it possible that it would lead to faster results at the runtime?
Yes it is because if we do a=a+1 python interpretor has to look for memory twice and when we do a+=1 it has to look for memory only once


Q2. What is the smallest number of statements you'd have to write in most programming languages to replace the Python expression a, b = a + b, a?
Use a temporary variable as
  temp=a
  a=a+b
b=temp


Q3. In Python, what is the most effective way to set a list of 100 integers to 0?

Use list comprehension as
List1=[0 for  I in range(101)]

Q4. What is the most effective way to initialise a list of 99 integers that repeats the sequence 1, 2, 3? S If necessary, show step-by-step instructions on how to accomplish this.

List1=[1,2,3]*33

Q5. If you're using IDLE to run a Python application, explain how to print a multidimensional list as efficiently?
my_list = [[1,1],[2,2],[3,3],[4,4],[5,5]] # 2 dimensional List
for x in range(len(my_list)):
    for y in range(len(my_list[x])):
        print(my_list[x][y],end=" ")


time complexity -o(n^2)



Q6. Is it possible to use list comprehension with a string? If so, how can you go about doing it?
Yes we can as

List1=[ I for I in “ineuron”]


Q7. From the command line, how do you get support with a user-written Python programme? Is this possible from inside IDLE?

Get support with a user-written Python Programme: Start a command prompt (Windows) or terminal window (Linux/Mac). If the current working directory is the same as the location in which you saved the file, you can simply specify the filename as a command-line argument to the Python interpreter.
Get support with a User-written Python Program from IDLE: You can also create script files and run them in IDLE. From the Shell window menu, select File → New File. That should open an additional editing window. Type in the code to be executed. From the menu in that window, select File → Save or File → Save As… and save the file to disk. Then select Run → Run Module. The output should appear back in the interpreter


Q8. Functions are said to be “first-class objects” in Python but not in most other languages, such as C++ or Java. What can you do in Python with a function (callable object) that you can't do in C or C++?
As in python functions are first class objects when we can pass function to function or return function and store it in a variable,first class objects basically implies that whatever we can do with other objects same thing can be done with functions


Q9. How do you distinguish between a wrapper, a wrapped feature, and a decorator?
Wrappers around the functions are also knows as decorators which are a very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class. Decorators allow us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it. In Decorators, functions are taken as the argument into another function and then called inside the wrapper function.

Q10. If a function is a generator function, what does it return?

It return lazy iterator which  helps in achieving memory optimization

Q11. What is the one improvement that must be made to a function in order for it to become a generator function in the Python language?
Use yield keyword

Q12. Identify at least one benefit of generators.
Memory opotimization can be achieved using generators
