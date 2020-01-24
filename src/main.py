import curses
import time

#initialize curses and returns window object representing entire screen
stdscr = curses.initscr()

#basic cursor movement
yMax = curses.LINES
xMax = curses.COLS

def main(stdscr):

    stdscr.keypad(True)
    curses.noecho()
    curses.cbreak()

    #initialize 2d list each cell as False
    cells = [[True] * xMax for i in range(yMax)]

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

    while(True):
        cellsCounter = [[0] * xMax for i in range(yMax)]

        #loop through list and track how many neighbors each cell has
        #loop through list. each time I hit a live cell I increment all the cells adjacent to it
        for i in range(0, yMax):
            for j in range(0, xMax):
                if cells[i][j]:
                    #increment all adjacent cells
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

        #print(cellsCounter)

        for i in range(0, yMax):
            for j in range(0, xMax):
                if cells[i][j] and (not cellsCounter[i][j] == 2 or not cellsCounter[i][j] == 3):
                    cells[i][j] == False
                if not cells[i][j] and cellsCounter[i][j] == 3:
                    cells[i][j] == True

        #need another list that keeps an int in each cell
        #then loop through both lists and determine which cells die and which become live

        #redraw window
        for i in range(0, yMax):
            for j in range(0, xMax):
                if i == yMax - 1 and j == xMax - 1:
                    break
                if cells[i][j]:
                    stdscr.addstr(i,j,'#')
                else:
                    stdscr.addstr(i,j,' ')
        stdscr.refresh()


#restore terminal to original state when main exits
curses.wrapper(main)

#TODO
#fix bug in bottom right cell
#get number of live neighbors for each cell
#loop through an kill cells or bring to life
#add mouse interface
