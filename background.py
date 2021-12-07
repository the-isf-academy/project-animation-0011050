from turtle import *
import random
from helpers import *
speed(0)

def background():
    with restore_state_when_finished():
        bgcolor('black')
        pencolor('white')
        fillcolor("white")
        for i in range(20):
            r1 = random.randint(-400,400)
            r2 = random.randint(-400, 400)
            rc = random.randint(1, 2)
            penup()
            goto(r1,r2)
            pendown()
            begin_fill()
            circle(rc,360)
            end_fill()
