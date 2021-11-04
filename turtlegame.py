import turtle
import random


win = turtle.Screen()
win.tracer(0)

#Creating our jet

jet = turtle.Turtle()
jet.shape("triangle")
jet.color("blue")
jet.shapesize(1.5,1.5)
jet.up()
jet.goto(0,-200)


jetspeed  = 0.3

# Creating our enemy 

enemy = turtle.Turtle()
enemy.shape("circle")
enemy.color("red")
enemy.up()

enemy.goto(random.randint(-280,280),random.randint(-280,280))


def moveleft():
    jet.left(15)

def moveright():
    jet.right(15)

win.listen()
win.onkeypress(moveleft,"Left")
win.onkeypress(moveright,"Right")

while True:
    win.update()

    # move out jet
    jet.fd(jetspeed)

    #enemy and jet collision 

    if jet.distance(enemy) < 15:
        enemy.goto(random.randint(-280,280),random.randint(-280,280))


