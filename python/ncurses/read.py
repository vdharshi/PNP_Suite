import curses
import os
screen = curses.initscr()
with open ("/etc/lsb-release",'r')as f:
 index=0
 for line in f:
  index=index+1
  if 'CHROMEOS_RELEASE_BOARD' in line:
   i=line[:-1]
c=os.popen("crossystem fwid").read()

screen.addstr(0, 0, f"{i}    {c}")
screen.refresh()

c = screen.getch()

curses.endwin()
