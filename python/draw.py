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

character = Turtle()
character.color("blue")

def turnLeft():
    character.left(30)

def turnRight():
    character.right(30)

window.listen()
window.onkey(turnLeft, "Left")
window.onkey(turnRight, "Right")

while True:
    character.forward(1)

exitonclick()