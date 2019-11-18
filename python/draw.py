from turtle import *

size = 300

window = Screen()
window.bgcolor("pink")

pen = Turtle()

pen.hideturtle()
pen.penup()
pen.setposition(-size,-size)
pen.pendown()
pen.pensize(5)
for side in range(4):
  pen.forward(size * 2)
  pen.left(90)
pen.penup()

character = Turtle()
character.color("blue")
character.pensize(2)

def turnLeft():
    character.left(30)

def turnRight():
    character.right(30)

window.listen()
window.onkey(turnLeft, "Left")
window.onkey(turnRight, "Right")

while True:
    if character.xcor() > size or character.xcor() < -size:
        character.right(180)

    if character.ycor() > size or character.ycor() < -size:
        character.left(180)

    character.forward(1)

exitonclick()