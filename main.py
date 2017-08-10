import time
import RPi.GPIO as GPIO
import curses
import thread
import time
from RPIO import PWM

Enable1=22 #Enable Motor 1
Enable2=25 #Enable Motor 2
ServoCam=13 #Controle Servo da Câmera

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
#//////////////CONTROLE DIREÇÃO CÂMERA\\\\\\\\\\\\\
def camdireita():
	PWM.add_channel_pulse(0, ServoCam, 100, 220 )

def camesquerda():
	PWM.add_channel_pulse(0, ServoCam, 100, 5 )

def camcentro():
	PWM.add_channel_pulse(0, ServoCam, 100, 120 )


#/////////////CONTROLE MOVIMENTAÇÃO\\\\\\\\\\\\\\\
def acelerar(tempo,d):
   t=float(tempo)
   if d==1:
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
	

#////////////MAIN\\\\\\\\\
#---INICIALIZAÇÃO
stdscr = curses.initscr() #Inicia Curses
curses.noecho()  #Desabilita Verbose Terminal - Curses
curses.cbreak()  #Habilita terminal para apenas um caractere - Curses
stdscr.keypad(1) #Habilita Uso do Teclado Numérico - Curses
stdscr.refresh() #Atualiza Tela - Curses
PWM.setup() #Inicia PWM - RPIO/PWM
PWM.init_channel(0) #Inicia Canal PWM para Servo Câmera - RPIO/PWM

#---LOOP PRINCIPAL
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
   elif tecla == ord('a'):
	camesquerda()
   elif tecla == ord('d'):
	camdireita()
   elif tecla == ord('s):
	camcentro()
	
#---FINALIZAÇÃO
PWM.clear_channel_gpio(0, ServoCam)  #Limpa Canal 0 do Servo da Câmera
PWM.cleanup() # Limpa Pinos de PWM
stdscr.keypad(0) #Desabilita Teclado Numérico
curses.nocbreak() #Desabilita Curses
curses.echo()     #Habilita Verbose Terminal
curses.endwin()   #Desliga Biblioteca Curses
GPIO.cleanup()    #Limpa Pinos GPIO

