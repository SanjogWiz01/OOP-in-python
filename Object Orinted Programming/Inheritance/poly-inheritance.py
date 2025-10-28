class Bird:
    def sound(self):
        print("Some generic bird sound")

class Sparrow(Bird):
    def sound(self):
        print("Chirp chirp")

class Crow(Bird):
    def sound(self):
        print("Caw caw")

birds = [Sparrow(), Crow()]
for b in birds:
    b.sound()  # Different outputs, same method name
