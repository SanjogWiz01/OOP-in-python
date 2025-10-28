# Example of Compile-Time Polymorphism in Python using Method Overloading

class Calculator:
    def add(self, a, b=None, c=None):
        if b is not None and c is not None:
            return a + b + c
        elif b is not None:
            return a + b
        else:
            return a

calc = Calculator()
print(calc.add(2, 3))        # Output: 5
print(calc.add(2, 3, 4))     # Output: 9
print(calc.add(5))           # Output: 5