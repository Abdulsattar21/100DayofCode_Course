from turtle import Turtle, Screen
import random as r
#importing the random class with just a r instead of random. etc...

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = Turtle()
tim.shape("turtle")
tim.color("red")
tim.speed(1000)

# for _ in range(3, 10):
#     x = r.random()
#
#     angle = 360 / _
#     a = 0
#     while a != _:
#         tim.right(angle)
#         tim.forward(100)
#         a += 1

while True:
    b = r.randint(1,4)
    if b == 1:
        tim.right(90)
        tim.color(r.choice(colours))
        tim.forward(17.5)
    elif b == 2:
        tim.right(180)
        tim.color(r.choice(colours))
        tim.forward(17.5)
    elif b == 3:
        tim.right(270)
        tim.color(r.choice(colours))
        tim.forward(17.5)
    elif b == 4:
        tim.right(360)
        tim.color(r.choice(colours))
        tim.forward(17.5)

screen = Screen()
screen.exitonclick()


