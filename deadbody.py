from turtle import*
fillcolor("#00FFFF")
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
forward(50)
left(90)
forward(20)
pendown()
begin_fill()
right(100)
circle(10,210)
forward(70)
right(120)
circle(8,270)
right(120)
circle(10,240)
right(95)
forward(65)
end_fill()

input()
