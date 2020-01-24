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
    #curses.cbreak()

    #abstracts keyboard input
    #stdscr.keypad(True)

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
    yMax = curses.LINES
    xMax = curses.COLS
    cells = [[False] * xMax for i in range(yMax)]
    y = 0
    x = 0
    while(True):
        userInput = stdscr.getch()
        #left on h
        if userInput == 104:
            x -= 1
            if x < 0:
                x = 0
        #down on j
        if userInput == 106:
            y += 1
            if y >= yMax:
                y = yMax - 1
        #up on k
        if userInput == 107:
            y -= 1
            if y < 0:
                y = 0
        #right on l
        if userInput == 108:
            x += 1
            if x >= xMax:
                x = xMax - 1
        #toggle cell on space
        if userInput == 32:
            if cells[y][x]:
                stdscr.addstr(y,x,' ')
                cells[y][x] = False
            else:
                stdscr.addstr(y,x,'#')
                cells[y][x] = True
        stdscr.move(y,x)



#restore terminal to original state when main exits
curses.wrapper(main)

#TODO
#fix toggle bug
#fix bug in bottom right cell
#allow for file input with preselected cells?
#user input to run program
#user input to end program other than ctr-c?
