import curses
stdscr = curses.initscr()
#curses.noecho()
curses.cbreak()
stdscr.keypad(True)

stdscr.addstr(0,0, "Lines :" + str(curses.LINES) + ", Columns : " + str(curses.COLS))
stdscr.refresh()

c = stdscr.getch()

curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
