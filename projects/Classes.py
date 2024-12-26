# we use classes to difine new types
# in class we use upper letters & in variables we use underscore "_" in functions we use underscore too
# EmailClass
#also there is something call constructors
class Point:
    def move(self):
        print("move")
    def draw(self):
        print("draw")
# we can use object for the onne class like point1.x =10


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()
point1.move()

point2= Point()
point2.x =20
print(point2.x)