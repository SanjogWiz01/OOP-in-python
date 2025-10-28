class area:
    def rectangle(self,length,breadth):
        return length*breadth
    def square(self,side):
        return side*side
    def circle(self,radius):
        pi=3.14
        return pi*radius*radius
a=area()
print("Area of Rectangle:",a.rectangle(5,3))
print("Area of Square:",a.square(4))
print("Area of Circle:",a.circle(7))
