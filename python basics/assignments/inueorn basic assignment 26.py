birthday=[]
for i in range(5+1):
    birthday.append(i+1997)
    
print(birthday)

third_birthday=birthday[3]
print(third_birthday)

max=0
for i in range(len(birthday)-1):
    if(birthday[i]>=birthday[i+1]):
        max=birthday[i]
    else:
        max=birthday[i+1]
        

print(max)
#c=max(birthday)
#print(c)

array=["mozerrella","cinderella","salonmella"]
for i in range((len(array)-1)):
    if array[i]=="cinderella":
        array[i]=array[i].upper()
        


print(array)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
surprise=["Grouchu","Chico","Harpo"]
print(len(surprise))
for i in range(len(surprise)):
    if(i==(len(surprise)-1)):
        surprise[i]=surprise[i].lower()

print(surprise)        
surprise.reverse()
#surprise.capitalize()
for i in range(len(surprise)):
    surprise[i]=surprise[i].capitalize()
    
print(surprise)

e2f={"dog":'chein',"cat":'chat',"walrus":"morse"}
print(e2f["walrus"])
print(e2f)

f2e={value:key for key,value in e2f.items()}
print(f2e)
s={value for value in e2f.values()}
print(s)
print(type(s))
nesteddict={"animals":{"cats":["henri","grumpy","octri"]},"plants":{"octopi":{}},"others":{"emus":{}}}
for k,v in nesteddict.items():
    if k=="animals":
        print(v.keys())
print(nesteddict.keys()) 
print(nesteddict['animals']['cats'])
