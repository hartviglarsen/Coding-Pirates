from turtle import *

window = Screen()
window.bgcolor("pink")

pen = Turtle()

pen.hideturtle()
pen.penup()
pen.setposition(-300,-300)
pen.pendown()
pen.pensize(3)
for side in range(4):
  pen.forward(600)
  pen.left(90)
pen.penup()

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
    if character.xcor() > 300 or character.xcor() < -300:
        character.right(180)

    if character.ycor() > 300 or character.ycor() < -300:
        character.left(180)

    character.forward(1)

exitonclick()