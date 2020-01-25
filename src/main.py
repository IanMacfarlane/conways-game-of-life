import curses
import time
import os

#initialize curses and returns window object representing entire screen
stdscr = curses.initscr()

#basic cursor movement
yMax = curses.LINES
xMax = curses.COLS

def main(stdscr):

    #enable mouse click
    curses.mousemask(2)

    #initialize 2d list each cell as False
    cells = [[False] * xMax for i in range(yMax)]

    y = int(yMax/2)
    x = int(xMax/2)
    stdscr.move(y,x)

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
            if y == yMax-1 and x == xMax-1:
               1 
            elif cells[y][x]:
                stdscr.addstr(y,x,' ')
                cells[y][x] = False
            else:
                stdscr.addstr(y,x,'#')
                cells[y][x] = True

        #on mouse click toggle cell at mouse location
        if userInput == 409:
            curses.curs_set(False)
            mouseClick = curses.getmouse()
            yMouse = mouseClick[2]
            xMouse = mouseClick[1]

            if yMouse == yMax-1 and xMouse == xMax-1:
               1 
            elif cells[yMouse][xMouse]:
                stdscr.addstr(yMouse,xMouse,' ')
                cells[yMouse][xMouse] = False
            else:
                stdscr.addstr(yMouse,xMouse,'#')
                cells[yMouse][xMouse] = True

        #run game of life on enter
        if userInput == 10:
            runGame(stdscr, cells)

        stdscr.move(y,x)

def runGame(stdscr, cells):

    #make cursor invisible
    curses.curs_set(False)

    while(True):
        cellsCounter = [[0] * xMax for i in range(yMax)]
        cellsOut = [[True] * xMax for i in range(yMax)]

        #loop through list each live cell incraments all those around it by 1
        for i in range(0, yMax):
            for j in range(0, xMax):
                if cells[i][j]:
                    #increment all adjacent cells without going out of bounds
                    if not i-1 < 0:
                        cellsCounter[i-1][j] += 1
                    if not i+1 >= yMax:
                        cellsCounter[i+1][j] += 1
                    if not j+1 >= xMax:
                        cellsCounter[i][j+1] += 1
                    if not j-1 < 0:
                        cellsCounter[i][j-1] += 1
                    if not j+1 >= xMax and not i+1 >= yMax:
                        cellsCounter[i+1][j+1] += 1
                    if not i-1 < 0 and not j+1 >= xMax:
                        cellsCounter[i-1][j+1] += 1
                    if not i+1 >= yMax and not j-1 < 0:
                        cellsCounter[i+1][j-1] += 1
                    if not i-1 < 0 and not j-1 < 0:
                        cellsCounter[i-1][j-1] += 1

        #conways game of life rules to toggle cells between alive and dead
        for i in range(0, yMax):
            for j in range(0, xMax):

                #if cell is alive and has 2 or 3 neighbors it stays alive otherwise it dies
                if cells[i][j] and (cellsCounter[i][j] == 2 or cellsCounter[i][j] == 3):
                    cellsOut[i][j] = True
                elif cells[i][j]:
                    cellsOut[i][j] = False

                #if a cell is dead and it has 3 neighbors it comes to life otherwise it stays dead
                elif not cells[i][j] and cellsCounter[i][j] == 3:
                    cellsOut[i][j] = True
                else:
                    cellsOut[i][j] = False

        #set cells to new iteration
        cells = cellsOut

        #redraw window
        for i in range(0, yMax):
            for j in range(0, xMax):
                if i == yMax - 1 and j == xMax - 1:
                    break
                if cellsOut[i][j]:
                    stdscr.addstr(i,j,'#')
                else:
                    stdscr.addstr(i,j,' ')

        stdscr.refresh()
        time.sleep(.1)


#restore terminal to original state when main exits
curses.wrapper(main)
