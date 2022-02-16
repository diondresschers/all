# Only for Windows users: python3 -m pip install windows-curses
# Cursus documentation: https://docs.python.org/3/library/curses.html

import curses
from curses import wrapper # The wrapper makes the initialization easier
import time

def main(stdscr): # std = Standard, scr = Screen
  curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_YELLOW) # Now you've set the color with ID 1, to a foreground of BLUE and a background of YELLOW


  # Now do the above, but with simple Python CONSTANTS:
  curses.init_pair(2, curses.COLOR_MAGENTA, curses.COLOR_GREEN)
  BLUE_AND_YELLOW = curses.color_pair(1)
  MAGENTA_AND_YELLOW = curses.color_pair(2) # Now you can refer to this CONSTANT





  stdscr.clear() # clear the screen
  stdscr.addstr("hello world") # str = String. Add a string to the screen.
  stdscr.addstr(2, 20, "now I am here") # Use another location (first the Y-location or line, then the X-location)

  # Not all will work properly, all may relate to the OS, and terminal what and if it will output
  stdscr.addstr(4, 10, "is this bold", curses.A_BOLD) # Makes this text Bold.
  stdscr.addstr(5, 11, "is this underline", curses.A_UNDERLINE)
  stdscr.addstr(6, 12, "is this blink?", curses.A_BLINK) # did not work in Linux
  stdscr.addstr(7, 13, "is this reverse?", curses.A_REVERSE)
  stdscr.addstr(8, 14, "is this dim?", curses.A_DIM)# did not work in Linux
  stdscr.addstr(9, 15, "is this standout?", curses.A_STANDOUT)# Same as A_REVERSE
  stdscr.addstr(9, 15, "is this colored?", curses.color_pair(1)) # Set the color_pair that you've set with init_pair
  stdscr.addstr(10,15, "is this colored?", MAGENTA_AND_YELLOW)

  # You can combine color with a markup via the | sign; so NOT add another attribute
    
  stdscr.addstr(11,16, "is this colored, and underlined!?", BLUE_AND_YELLOW | curses.A_UNDERLINE)

  
  for number in range(100):
    stdscr.addstr(10,16,str(number))
    time.sleep(.01)     
    stdscr.refresh()

  #for number in range(0, 10, 1):
  #  stdscr.addstr(number, 10, str(number))
  stdscr.refresh() # You have to refresh the screen in order to output how it looks

  # When noting is done, the user will be taken immediately taken back by the prompt.
  stdscr.getch() # chr = Character # Get the character that the user typed in. # Also wait for the user.

wrapper(main) # Let the wrapper take over / take control over the main program.

colors = """
COLOR_BLACK = Black
COLOR_BLUE = Blue
COLOR_CYAN = Cyan (light greenish blue)
COLOR_GREEN = Green
COLOR_MAGENTA = Magenta (purplish red)
COLOR_RED = Red
COLOR_WHITE = White
COLOR_YELLOW = Yellow
"""
