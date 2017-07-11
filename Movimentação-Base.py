import curses
import os

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.refresh()

def direita():
	print('Direita')

def esquerda():
	print('Esquerda')

def frente():
	print('Frente')
        a =a +1
        print(a)

def tras():
	print('Para tras')


tecla = ''
while tecla != ord('q'):
    print( "Aperte Q para finalizar o programa.")
    tecla = stdscr.getch()
    os.system("clear")
    if tecla == curses.KEY_UP: 
        frente()
    elif tecla == curses.KEY_DOWN:
    	tras()
    elif tecla == curses.KEY_LEFT:
    	esquerda()
    elif tecla == curses.KEY_RIGHT:
    	direita()

curses.endwin()
