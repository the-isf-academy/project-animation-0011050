from turtle import *
from helpers import *
pensize(20)
speed(0)

def body(color,size):
    fillcolor(color)
    begin_fill()
    right(90)
    forward(50*size)
    right(180)
    circle(40*size, -180)
    right(180)
    forward(200*size)
    right(180)
    circle(110*size,-180)
    right(180)
    forward(200*size)
    right(180)
    circle(40*size,-180)
    right(180)
    forward(50*size)
    right(90)
    left(30*size)
    circle(60,-50*size)
    end_fill()
def goggles(color,size):

    right(180)
    fillcolor(color)
    begin_fill()
    circle(50*size,180)
    setheading(0)
    forward(60*size)
    circle(50*size,180)
    forward(60*size)
    end_fill()
def backpack(color,size):
    fillcolor(color)
    begin_fill()
    forward(30*size)
    circle(30*size,90)
    setheading(270)
    forward(60*size)
    circle(30*size,90)
    forward(30*size)
    end_fill()
    left(90)
    forward(120*size)

def draw_figure(color,size):
    fillcolor("gray")
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



def draw_amogus(color,size):
    with restore_state_when_finished():
        setheading(0)
        pensize(20*size)
        fillcolor("gray")
        pencolor("black")
        begin_fill()
        body(color,size)
        setheading(90)
        penup()
        forward(200*size)
        right(90)
        forward(40*size)
        pendown()
        goggles("gray",size)
        penup()
        forward(140*size)
        left(90)
        forward(50*size)
        right(90)
        pendown()
        backpack(color,size)

# draw_amogus("red",1)
