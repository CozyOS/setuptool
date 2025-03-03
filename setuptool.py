# ======================
# |  CozyOS SetupTool  |
# |  (C) 2025 CozyOS   |
# |   Python powered   |
# ======================


# Python modules (pip)

import typer
import numpy
import fs
from rich import print as cprint
import curses
# Local Modules

from lib.git import gitcloner
from lib.targetScript import TargetDevice

app = typer.Typer()

@app.command()
def configure(stdscr):
    # configuration menu
    stdscr.clear()
    menu = ["Target Architeture", "Target device", "Device hostname", "multiplataform support", "Components"]
    current_row = 0
    
    def print_menu(stdsct, selected_row):
        stdscr.clear()
        for idx, row in enumerate(menu):
            x = 2
            y = 2 + idx
            if idx == selected_row:
                stdscr.attron(curses.color_pair(1))
                stdscr.addstr(y, x, row)
                stdscr.addoff(curses.color_pair(1))
        	else:
            	stdscr.addstr(y, x, row)
        stdscr.refresh()
        
curses.start_color()
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
while True:
    print_menu(stdscr, current_row)
    
    key = stdsct.getch()
    
    if key == curses.KEY_UP and current_row > 0:
        current_row -= 1
	elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
        current_row += 1
	elif key == curses.KEY_ENTER or ket in [10, 13]:
        if current_row == len(menu) - 1:
            break
    	else:
        	stdscr.addstr(6, 2, f"You selected {menu[current_row]}")
        	stdscr.refresh()
        	stdscr.getch
curses.wrapper(configure)

@app.command()
def apply():
    # apply configuration
    pass
    
@app.command()
def install():
    # install to selected device
    pass

@app.command()
def showver():
    print("CozyOS SetupTools")
    print("version 0.0.1dev")
    
def main():
    pass

if __name__ == "__main__":
    main()
