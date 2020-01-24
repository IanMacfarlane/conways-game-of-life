import curses
import time

#initialize curses and returns window object representing entire screen
stdscr = curses.initscr()

#terminate curses manually
#curses.nocbreak()
#stdscr.keypad(False)
#curses.echo()
#restore terminal to original operation mode
#curses.endwin()

def main(stdscr):
    #turn off automatic echoing of keys to the screen
    curses.noecho()

    #allows keyboard input without requiring the enter key to be pressed
    curses.cbreak()

    #abstracts keyboard input
    stdscr.keypad(True)

    #make cursor invisible
    #curs_set(False)

    #curses.LINES
    #curses.COLS
    #stdscr.addstr('hello world')
    #stdscr.refresh()

    #time.sleep(5)
    
    #refresh screen then wait for keyboard input returns key. getch() returns keycode. getstr()
    userInput = stdscr.getkey()
    #addstr(y,x,str)
    stdscr.addstr(str(userInput))
    stdscr.getch()


#restore terminal to original state when main exits
curses.wrapper(main)
