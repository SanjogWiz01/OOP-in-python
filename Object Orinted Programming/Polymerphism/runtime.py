class a:
 def sound(self):
   print("hello world!")
class b(a):
 
    def sound(self):
        return "Bark"

class C(a):
    def sound(self):
        return "Meow"

# Polymorphic behavior
animals = [a(), C(), b()]
for a in animals:
    print(a.sound())