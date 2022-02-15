import turtle
import random
import time


def momentum(aMass, bMass, aVel, bVel):
    GalTransform = -bVel
    aVel += GalTransform
    bVel += GalTransform
    V1 = aVel

    aVel = ((aMass - bMass) / (aMass + bMass)) * V1
    bVel = ((2 * aMass) / (aMass + bMass)) * V1

    aVel -= GalTransform
    bVel -= GalTransform

    return (aVel, bVel)


win = turtle.Screen()
win.title('Conservation of Momentum using Galilean Transformation')
win.setup(1000, 500)
win.bgcolor('black')
win.tracer(0)

pen = turtle.Pen()
pen.color('red')
pen.up()
pen.goto(0, 200)
pen.hideturtle()


class Ball(turtle.Turtle):
    def __init__(self, mass, velocity, xpos, nr):
        super().__init__(shape='circle')
        self.mass = mass
        self.velocity = velocity
        self.nr = nr
        self.xpos = xpos
        self.list = ['red', 'blue', 'green', 'cyan', 'yellow']
        self.color(random.choice(self.list))
        self.up()
        self.shapesize(mass / 2)
        self.radius = mass * 5
        self.goto(xpos, 0)
        self.bounce = 'ready'

    def move(self):
        self.goto(self.xcor() + self.velocity, self.ycor())

        if self.xcor() > 500 - self.radius or self.xcor() < -500 + self.radius:
            self.velocity *= -1
            self.bounce = 'ready'


obj = []
ball1 = Ball(5, 2.0, -200, 1)
ball2 = Ball(2, -3.0, 200, 2)
ball3 = Ball(12, -4, 3, 3)


obj.append(ball1)
obj.append(ball2)
obj.append(ball3)

count = 0


time.sleep(3)
while True:
    time.sleep(0.01)
    count += 1
    win.update()

    for i in obj:
        if i.bounce == 'wait' and count % 20 == 0:
            i.bounce = 'ready'
        i.move()

        for j in range(len(obj)):
            if i.nr != obj[j].nr:

                if i.xcor() + i.radius >= obj[j].xcor() - obj[j].radius and i.xcor() - i.radius <= obj[j].xcor() + obj[
                    j].radius:
                    if i.bounce == 'ready' and obj[j].bounce == 'ready':
                        values = momentum(i.mass, obj[j].mass, i.velocity, obj[j].velocity)
                        # print("Values: ",values)
                        i.velocity = values[0]
                        i.bounce = 'wait'
                        obj[j].velocity = values[1]
                        obj[j].bounce = 'wait'

