import time
import curses
import random
from curses import wrapper
from curses.textpad import Textbox, rectangle

def start (stdscr):
    stdscr.addstr(0, 0, "Welcome To the ultimate WPM test made in python!")
    stdscr.addstr(1, 0, "Press any key to start: ")


def main (stdscr):
     
    start(stdscr)

    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_GREEN)

    # Variables to use

    getKey = stdscr.getch()
    refresh = stdscr.refresh()
    GREEN = curses.color_pair(1)
    BLACK = curses.color_pair(2)
  
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(0, 0, "Big", BLACK)
    stdscr.getch()
    stdscr.addstr(0, 0, "Balls", GREEN)
    stdscr.getch()
    wpm(stdscr)


def wpm (stdscr):
   target_text = "Some text..."
   current_text = []
   stdscr.clear()
   stdscr.addstr(0, 0, target_text)
   
   while True:
       getKey = stdscr.getkey()
       current_text.append(getKey)
       
       if (ord(getKey) == "^["):
           break

       stdscr.clear()
       stdscr.addstr(target_text)

       for char in current_text:
           stdscr.addstr(0, 0, char, curses.color_pair(1))

           stdscr.refresh()


wrapper(main)
