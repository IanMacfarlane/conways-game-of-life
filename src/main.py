import curses
import time

#initialize curses and returns window object representing entire screen
stdscr = curses.initscr()

#basic cursor movement
yMax = curses.LINES
xMax = curses.COLS

def main(stdscr):

    #initialize 2d list each cell as False
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

        #run game of life on enter
        if userInput == 10:
            runGame(stdscr, cells)

        stdscr.move(y,x)

def runGame(stdscr, cells):

    #make cursor invisible
    curses.curs_set(False)

    #redraw window
    for i in range(0, yMax):
        for j in range(0, xMax):
            if i == yMax - 1 and j == xMax - 1:
                break
            if cells[i][j]:
                stdscr.addstr(i,j,'#')
            else:
                stdscr.addstr(i,j,' ')


#restore terminal to original state when main exits
curses.wrapper(main)

#TODO
#fix bug in bottom right cell
#user input to run program
#user input to end program other than ctr-c?
