import RPi.GPIO as GPIO
from RPIO import PWM
import curses
import time

servo = 13
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
PWM.setup()
PWM.init_channel(0)

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.refresh()

def direita():
    PWM.add_channel_pulse(0, servo, 100, 70 )

def esquerda():
    PWM.add_channel_pulse(0, servo, 100, 180 )

def centro():
    PWM.add_channel_pulse(0, servo, 100, 120 )



#main

tecla = ''
while tecla != ord('q'):
   tecla = stdscr.getch()
   if tecla == ord('a'):
       esquerda()
   if tecla == ord('d'):
       direita()
   if tecla == ord('w'):
       centro()
   if tecla == ord('s'):
       PWM.clear_channel_gpio(0, servo)



PWM.clear_channel_gpio(0, servo)
PWM.cleanup()
stdscr.keypad(0)
curses.nocbreak()
curses.echo()
curses.endwin()
GPIO.cleanup()
