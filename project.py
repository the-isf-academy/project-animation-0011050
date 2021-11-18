from turtle import Screen, clear, forward, penup, pendown
from helpers import update_position, setup, no_delay
import settings
import time
import amogus

def draw_animation(num_frames, size, color, sleeptime):
    for i in range(num_frames):
        if i < num_frames // 2:
            forward(1)
        if i > num_frames // 2:
            penup()
            forward(-1)
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
    main()
