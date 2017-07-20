import curses
import os
import thread

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
stdscr.refresh()

def direita(z,b):
	print('Direita')

def esquerda(c,d):
	print('Esquerda')

def frente(e,f):
	print('Frente')
        a =a +1
        print(a)

def tras(k,l):
	print('Para tras')


tecla = ''
while tecla != ord('q'):
    print( "Aperte Q para finalizar o programa.")
    tecla = stdscr.getch()
    os.system("clear")
    if tecla == curses.KEY_UP: 
        thread.start_new_thread(frente,('', 1)) #tread.start_new_thread(Função, (ParâmetroObrigatório1, ParâmetroObrigatório2))
    elif tecla == curses.KEY_DOWN:
    	thread.start_new_thread(tras,('', 1))
    elif tecla == curses.KEY_LEFT:
    	thread.start_new_thread(esquerda,('', 1))
    elif tecla == curses.KEY_RIGHT:
    	thread.start_new_thread(direita,('', 1))

curses.endwin()
