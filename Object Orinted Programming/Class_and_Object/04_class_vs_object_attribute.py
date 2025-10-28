class name:
    name="sanjog"
don=name
print(don.name)     #sanjog
ram=name
don.name="ram"
print(don.name)    #ram 
#class attribute is shared by all instances of the class
print(ram.name)    #ram