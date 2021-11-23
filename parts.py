from turtle import setheading, color, begin_fill, left, forward, right, end_fill, circle
from helpers import restore_state_when_finished

def draw_amogus(color,size):
    with restore_state_when_finished():
        fillcolor("gray")
        pencolor("black")
        begin_fill()
        body(color,size)
        setheading(90)
        penup()
        forward(200*size)
        right(90)
        forward(50*size)
        pendown()
        goggles("gray",size)
        penup()
        forward(140*size)
        left(90)
        forward(50*size)
        right(90)
        pendown()
        backpack(color,size)
