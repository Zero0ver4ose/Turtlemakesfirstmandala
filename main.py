from turtle import Turtle, Screen
import random


'''_______________________________Function______________________________________________'''
def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        schiggy.forward(100)
        schiggy.right(angle)

'''''____________________________________________________________________________________'''

schiggy = Turtle()
schiggy.shape("turtle")
schiggy.color("green")

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for shape_side_n in range(3,11):
    schiggy.color(random.choice(colours))
    draw_shape(shape_side_n)















screen = Screen()
screen.exitonclick()


