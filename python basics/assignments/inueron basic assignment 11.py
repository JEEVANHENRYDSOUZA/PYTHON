1.	Create an assert statement that throws an AssertionError if the variable spam is a negative integer.
2.	spam =int(input("enter a value "))
3.	assert spam >=0
4.	print("the number is negative")

2. Write an assert statement that triggers an AssertionError if the variables eggs and bacon contain strings that are the same as each other, even if their cases are different (that is, 'hello' and 'hello' are considered the same, and 'goodbye' and 'GOODbye' are also considered the same).
string1=input("enter string one")
string2=input("enter string two")
string1.upper()
string2.upper()

assert not(string1==string2)
print("both the strings are not same")

3. Create an assert statement that throws an AssertionError every time.
assert False

5.	What are the two lines that must be present in your software in order to call logging.debug()?
Import logging #importing the logging module of python
#setting up the logger
logging.basicConfig(filename=”c:\\python\\jeevan.log”)

6.What are the two lines that your program must have in order to have logging.debug() send a logging message to a file named programLog.txt?

6. What are the five levels of logging?
Debug,info,warning,error and critical
7.What line of code would you add to your software to disable all logging messages?
logging.disable = True

8.Why is using logging messages better than using print() to display the same message?
The logging package has a lot of useful features:
•	Easy to see where and when (even what line no.) a logging call is being made from.
•	You can log to files, sockets, pretty much anything, all at the same time.
•	You can differentiate your logging based on severity.
•	One of the biggest advantages of proper logging is that you can categorize messages and turn them on or off depending on what you need. 
Print doesn't have any of these.

9. What are the differences between the Step Over, Step In, and Step Out buttons in the debugger?
Step over – An action to take in the debugger that will step over a given line. If the line contains a function the function will be executed and the result returned without debugging each line.
Step into – An action to take in the debugger. If the line does not contain a function it behaves the same as “step over” but if it does the debugger will enter the called function and continue line-by-line debugging there.
Step out – An action to take in the debugger that returns to the line where the current function was called.
10.After you click Continue, when will the debugger stop ?
When the execution of the entire program is completed or when a breakpoint occurs in the program
11. What is the concept of a breakpoint?
Breakpoints are most commonly used to interrupt a running program immediately before the execution of a programmer-specified instruction. This is often referred to as an instruction breakpoint
