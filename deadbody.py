from turtle import*
from helpers import*
def draw_dead(color,size):
    with restore_state_when_finished():
        fillcolor("blue")
        speed(0)
        pensize(5)
        def draw(rad):
        #shogo sung
            for i in range(2):
                circle(rad,90)
                circle(rad//2,90)
        begin_fill()
        goto(0,0)
        right(45)
        draw(80)
        penup()
        goto(0,0)
        left(90)
        forward(10)
        right(135)
        end_fill()
        pendown()
        fillcolor("#153c4e")
        begin_fill()
        left(45)
        draw(60)
        end_fill()
        penup()
        fillcolor("white")
        setheading(0)
        forward(40)
        left(90)
        forward(13)
        pendown()
        begin_fill()
        right(100)
        circle(15,210)
        forward(65)
        right(120)
        circle(13,270)
        right(120)
        circle(15,230)
        right(88)
        forward(60)
        end_fill()
        setheading(90)
        penup()
        forward(50)
        left(90)
        forward(30)
        pendown()
        fillcolor("blue")
        begin_fill()
        setheading(135)
        circle(-24,140)
        forward(48)
        circle(-26,130)
        setheading(150)
        forward(15)
        left(10)
        forward(15)
        left(10)
        forward(15)
        left(10)
        forward(15)
        left(10)
        forward(15)
        left(10)
        forward(15)
        left(10)
        forward(10)
        end_fill()
