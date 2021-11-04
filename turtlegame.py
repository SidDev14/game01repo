import turtle

win = turtle.Screen()
win.tracer(0)

#Creating our jet

t = turtle.Turtle()
t.shape("triangle")
t.color("blue")
t.shapesize(2,2)
t.up()
t.goto(0,-200)

def moveleft():
    t.left(15)

def moveright():
    t.right(15)

win.listen()
win.onkeypress(moveleft,"Left")
win.onkeypress(moveright,"Right")

while True:
    win.update()

    # move out jet
    t.fd(0.1)
