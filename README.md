# Unit 0 Project: Animation

This code is written by Julian Hua (CS9, 2021) for his unit 0 drawing project. I drew an imposter from the mobile game among us and decided to do him killing another crewmate.
>


## Intial Contents

- `README.md` You're looking at it, or at least the formatted version. Every project has a README explaining what it is.
- `project.py` When this is run, it should draw my project.
- `settings.py` This is where I stored my settings for my animation.

## Modules
There are four modules and two main files. The four modules are:

1. amogus.py - This module is called amogus.py, and it includes functions related to drawing the amogus character. It is used by project.py.

2. deadbody.py - This module is called deadbody.py, and it includes functions related to drawing the dead body of the character. It is used by project.py

3. knife.py - This module is called knife.py, and it includes functions related to drawing the knife. It is used by project.py.

4. helpers.py - This module is called helpers.py, and it includes functions related to helping with no delay. It is used by knife.py amogus.py background.py deadbody.py project.py.

5. background.py - This module is called background.py, and it includes functions related to drawing the background. It is used by project.py.

## Settings
COLOR = changes color of the character
SLEEPTIME = the time in between each frame
NUMFRAMES = he number of frames in the animation
NUMREPEATS = the number of times the animation repeats
SCREENWIDTH = the height and width of the screen
SCREENHEIGHT = the height and width of the screen
START_X =the starting xcoordinate of the drawing
START_Y = the starting ycoordinate of the drawing
SIZE = size of the drawing


## How to use
Use python3 project.py to see the animation
