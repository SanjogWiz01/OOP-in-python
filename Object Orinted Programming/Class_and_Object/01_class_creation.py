class animal:
    def __init__(self,name):
          self.name=name
    def speak(self):
           print("Woof! My name is " , self.name)
dog=animal("Buddy")
dog.speak()
