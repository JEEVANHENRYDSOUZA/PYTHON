1. Create a zoo.py file first. Define the hours() function, which prints the string 'Open 9-5 daily'. Then, use the interactive interpreter to import the zoo module and call its hours() function.
2. In the interactive interpreter, import the zoo module as menagerie and call its hours() function.
3. Using the interpreter, explicitly import and call the hours() function from zoo.
4. Import the hours() function as info and call it.
5. Create a plain dictionary with the key-value pairs 'a': 1, 'b': 2, and 'c': 3, and print it out.
6.Make an OrderedDict called fancy from the same pairs listed in 5 and print it. Did it print in the same order as plain?
7. Make a default dictionary called dict_of_lists and pass it the argument list. Make the list dict_of_lists['a'] and append the value 'something for a' to it in one assignment. Print dict_of_lists['a'].

Zoo file:
def hours():
    print("daily 9-5")


import zoo as pd
pd.hours()

dictionary={'a':1,'b':2,'c':3}
print(dictionary)
plain = {'a':1,'b':2,'c':3}
from collections import OrderedDict
fancy = OrderedDict(plain)
fancy
OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# 5.7
from collections import defaultdict
def some():
    return 'something for a'

dict_of_list = defaultdict(some)
print(dict_of_list['a'])


