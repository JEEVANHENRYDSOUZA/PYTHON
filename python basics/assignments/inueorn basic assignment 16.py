Assignment 16 Solutions
1. Create a list called years_list, starting with the year of your birth, and each year thereafter until the year of your fifth birthday. For example, if you were born in 1980. the list would be years_list = [1980, 1981, 1982, 1983, 1984, 1985].
years_list = [ele for ele in range(1997,1997+6)]
print(years_list)
[1997, 1998, 1999, 2000, 2001, 2002]
2. In which year in years_list was your third birthday? Remember, you were 0 years of age for your first year.
print(years_list[3])
2000
3.In the years list, which year were you the oldest?
print(years_list[-1])
2002
4. Make a list called things with these three strings as elements: "mozzarella", "cinderella", "salmonella".
things = [ele+'ella' for ele in ['mozzar','cinder','salmon']]
print(things)
['mozzarella', 'cinderella', 'salmonella']
5. Capitalize the element in things that refers to a person and then print the list. Did it change the element in the list?
for ele in range(len(things)):
    if things[ele] == 'cinderella':
        things[ele] = things[ele].capitalize()
print(things)
['mozzarella', 'Cinderella', 'salmonella']
6. Make a surprise list with the elements "Groucho," "Chico," and "Harpo."
suprise_list = ['Groucho','Chico','Harpo']
print(suprise_list)
['Groucho', 'Chico', 'Harpo']
7. Lowercase the last element of the surprise list, reverse it, and then capitalize it.
print(suprise_list[-1].lower()[::-1].capitalize())
Oprah
8. Make an English-to-French dictionary called e2f and print it. Here are your starter words: dog is chien, cat is chat, and walrus is morse.
e2f = {'dog':'chien','cat':'chat','walrus':'morse'}
print(e2f)
{'dog': 'chien', 'cat': 'chat', 'walrus': 'morse'}
9. Write the French word for walrus in your three-word dictionary e2f.
print(e2f.get('walrus'))
morse
10. Make a French-to-English dictionary called f2e from e2f. Use the items method.
f2e = dict([ele[::-1] for ele in e2f.items()])
print(f2e)
{'chien': 'dog', 'chat': 'cat', 'morse': 'walrus'}
11. Print the English version of the French word chien using f2e.
print(f2e.get('chien'))
dog
12. Make and print a set of English words from the keys in e2f.
print(list(e2f.keys()))
['dog', 'cat', 'walrus']
13. Make a multilevel dictionary called life. Use these strings for the topmost keys: 'animals', 'plants', and 'other'. Make the 'animals' key refer to another dictionary with the keys 'cats', 'octopi', and 'emus'. Make the 'cats' key refer to a list of strings with the values 'Henri', 'Grumpy', and 'Lucy'. Make all the other keys refer to empty dictionaries.
life = {
    'animals':{
        'cats':['Henri','Grumpy','Lucy'],
        'octopi':{},
        'emus':{}
    },
    'plants':{},
    'other':{}
}
print(life)
{'animals': {'cats': ['Henri', 'Grumpy', 'Lucy'], 'octopi': {}, 'emus': {}}, 'plants': {}, 'other': {}}
14. Print the top-level keys of life.
print(list(life.keys()))
['animals', 'plants', 'other']
15. Print the keys for life['animals'].
print(list(life['animals'].keys()))
['cats', 'octopi', 'emus']
16. Print the values for life['animals']['cats']
print(life['animals']['cats'])
