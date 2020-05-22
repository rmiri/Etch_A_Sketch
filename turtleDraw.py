from turtle import Turtle, Screen, onkey, listen

window = Screen()
pen = Turtle()

def draw_pen():
    listen()

    onkey(goFoward, "Up")
    onkey(turnLeft, "Left")
    onkey(turnRight, "Right")
    onkey(goBack, "Down")

    window.exitonclick()

def goFoward():
    pen.forward(30)

def turnLeft():
    pen.left(30)

def turnRight():
    pen.right(30)

def goBack():
    pen.back(30)

draw_pen()










