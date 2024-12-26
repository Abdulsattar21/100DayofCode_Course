'''
 check the class file first
 __init__ is the shortcut for initial value
 self is to represent the object
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


point = Point()
