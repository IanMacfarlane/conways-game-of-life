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
    #userInput = stdscr.getkey()
    #addstr(y,x,str)
    #stdscr.addstr(str(userInput))
    #stdscr.getch()

    #basic cursor movement
    y = 0
    x = 0
    while(True):
        userInput = stdscr.getkey()
        if userInput == 'h':
            x -= 1
            if x < 0:
                x = 0
        if userInput == 'j':
            y += 1
            if y >= curses.LINES:
                y = curses.LINES - 1
        if userInput == 'k':
            y -= 1
            if y < 0:
                y = 0
        if userInput == 'l':
            x += 1
            if x >= curses.COLS:
                x = curses.COLS - 1
        stdscr.move(y,x)



#restore terminal to original state when main exits
curses.wrapper(main)

#TODO
#cursor movement
#toggle cells between alive and dead
#allow for file input with preselected cells?
#user input to run program
#user input to end program other than ctr-c?
