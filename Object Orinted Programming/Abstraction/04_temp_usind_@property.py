class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property # Getter for fahrenheit  
    # Convert celsius to fahrenheit
    def fahrenheit(self):
        return (self._celsius * 9/5) + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) * 5/9

# object  creatiob 
temp = Temperature(100)
print("Fahrenheit:", temp.fahrenheit)
temp.fahrenheit = 212
print("Celsius:", temp._celsius)
''' Property attribute.

fget
  function to be used for getting an attribute value
fset
  function to be used for setting an attribute value
fdel
  function to be used for del'ing an attribute
doc
  docstring

Typical use is to define a managed attribute x:'''