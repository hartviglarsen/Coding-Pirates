from turtle import *

window = Screen()
window.bgcolor("pink")

pen = Turtle()
pen.penup()

pen.setposition(-300,-300)

pen.pendown()
pen.pensize(3)
for side in range(4):
  pen.forward(600)
  pen.left(90)

exitonclick()