from turtle import *
speed(0)

def knife_blade(size):
    fillcolor("#C0C0C0")
    left(35)
    begin_fill()
    forward(140)
    right(120)
    for i in range(95):
        forward(5/3)
        right(1)
    setheading(0)
    left(125)
    forward(32)
    end_fill()

def knife_handle(size):
    fillcolor("#964B00")
    begin_fill()
    left(90)
    forward(40)
    left(90)
    forward(32)
    left(90)
    forward(40)
    end_fill()

def knife(size):
    pensize(10)
    setheading(0)
    knife_blade(size)
    knife_handle(size)


def draw_knife(size):
    with restore_state_when_finished():
        pensize(10)
        setheading(0)
        knife_blade(size)
        knife_handle(size)
