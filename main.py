import time
import RPi.GPIO as GPIO
import curses
import thread
import time

Enable1=22 #Enable Motor 1
Enable2=25 #Enable Motor 2

MD1=27  #MotorDireitoEntrada1
MD2=17  #MotorDireitoEntrada2
ME1=8   #MotorEsquerdoEntrada1
ME2=7   #MotorEsquerdoEntrada2

GPIO.setmode(GPIO.BCM)
GPIO.setup(MD1 ,GPIO.OUT) # IN1 
GPIO.setup(MD2 ,GPIO.OUT) # IN2
GPIO.setup(ME1 ,GPIO.OUT) # IN3 
GPIO.setup(ME2 ,GPIO.OUT) # IN4


#Set Enable High
Enable1=1
Enable2=1

def acelerar(tempo,d):
   if d==1:
      t=float(tempo)
      # MOTOR 1
      GPIO.output(MD1 ,1) # IN1
      GPIO.output(MD2 ,0) # IN2
      # MOTOR 2
      GPIO.output(ME1 ,1) # IN3
      GPIO.output(ME2 ,0) # IN4
      time.sleep(t)
      PARAR()
   elif d==0:
      # MOTOR 1
      GPIO.output(MD1 ,0) # IN1
      GPIO.output(MD2 ,1) # IN2
      # MOTOR 2
      GPIO.output(ME1 ,0) # IN3
      GPIO.output(ME2 ,1) # IN4
      time.sleep(t)
      PARAR()

def rota(tempo,d):
	t=float(tempo)
	if d == 0: #direita 
		# MOTOR 1
		GPIO.output(MD1 ,0) # IN1
		GPIO.output(MD2 ,1) # IN2
		# MOTOR 2
		GPIO.output(ME1 ,1) # IN3
		GPIO.output(ME2 ,0) # IN4
		time.sleep(t)
		PARAR()

	if d == 1: #esquerda
		# MOTOR 1
		GPIO.output(MD1 ,1) # IN1
		GPIO.output(MD2 ,0) # IN2
		# MOTOR 2
		GPIO.output(ME1 ,0) # IN3
		GPIO.output(ME2 ,1) # IN4
		time.sleep(t)
		PARAR()

def PARAR():
	# MOTOR 1
	GPIO.output(MD1 ,1) # IN1
	GPIO.output(MD2 ,1) # IN2
	# MOTOR 2
	GPIO.output(ME1 ,1) # IN3
	GPIO.output(ME2 ,1) # IN4

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)
stdscr.refresh()

tecla = ''
while tecla != ord('q'):
   tecla = stdscr.getch()
   if tecla == curses.KEY_UP:
      eixox=1
      acelerar(1,eixox)
   elif tecla == curses.KEY_DOWN:
      eixox=0
      acelerar(1,eixox)
   elif tecla == curses.KEY_LEFT:
      dire=1
      rota(8,dire)
   elif tecla == curses.KEY_RIGHT:
      dire=0
      rota(8,dire)
      
stdscr.keypad(0)
curses.nocbreak()
curses.echo()
curses.endwin()
GPIO.cleanup()

