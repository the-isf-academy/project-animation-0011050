from turtle import Screen, clear, forward, penup, pendown, left, right, goto, setheading, write, pencolor, bgcolor
from helpers import update_position, setup, no_delay
import settings
import time
import amogus
import knife
import deadbody
import background

def draw_animation(num_frames, size, color, sleeptime):
    left(45)
    bgcolor("white")
    for i in range(num_frames):
        with no_delay():
            clear()
            penup()
            goto(settings.START_X+i,settings.START_Y+i)
            pendown()
            amogus.draw_amogus(color,size)
            penup()
            goto(100,100)
            pendown()
            amogus.draw_amogus("blue",0.5)

        screen.update()
        time.sleep(sleeptime)
    clear()
    for i in range(100):
        with no_delay():
            clear()
            penup()
            goto(100+4*i,100-8*i)
            pendown()
            amogus.draw_amogus(color,size)
            knife.knife(0.5)
            penup()
            goto(100,100)
            pendown()
            setheading(0)
            deadbody.draw_dead("blue",0.5)
    clear()
    with no_delay():
        for i in range(10):
            background.background()
            penup()
            goto(-340,150)
            pendown()
            pencolor("red")
            style = ('Arial', 70)
            write('Dead Body Reported', font=style)



def main():
    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_animation(settings.NUMFRAMES, settings.SIZE, settings.COLOR, settings.SLEEPTIME)
    input("Press enter...")


if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()
