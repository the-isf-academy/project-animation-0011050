"""from turtle import Screen, clear, forward, penup, pendown, left, right, goto
from helpers import update_position, setup, no_delay
import settings
import time
import amogus


def draw_animation(num_frames, size, color, sleeptime):
    left(45)

    for i in range(num_frames):
        if i < num_frames // 2:
            penup()
            forward(1)
            pendown()
        with no_delay():
            amogus.draw_amogus(color,size)
        screen.update()
        time.sleep(sleeptime)
        clear()


def main():
    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_animation(settings.NUMFRAMES, settings.SIZE, settings.COLOR, settings.SLEEPTIME)
    input("Press enter...")


if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()"""



from turtle import Screen, clear, forward, penup, pendown, left, right, goto
from helpers import update_position, setup, no_delay
import settings
import time
import amogus


def draw_animation(num_frames, size, color, sleeptime):
    left(45)

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



def main():
    for i in range(settings.NUMREPEATS):
        setup(settings.START_X,settings.START_Y)
        draw_animation(settings.NUMFRAMES, settings.SIZE, settings.COLOR, settings.SLEEPTIME)
    input("Press enter...")


if __name__ == '__main__':
    screen = Screen()
    screen.setup(settings.SCREENWIDTH,settings.SCREENHEIGHT)
    main()
