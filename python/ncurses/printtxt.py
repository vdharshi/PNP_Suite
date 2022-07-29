import curses
screen = curses.initscr()
screen.addstr(0, 0, "This string gets printed at position (0, 0)")
screen.addstr(3, 1, "Try Russian text: Привет")  
screen.addstr(4, 4, "X")
screen.addch(5, 5, "Y")
screen.refresh()
curses.napms(10000)
curses.endwin()