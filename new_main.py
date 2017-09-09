import encoder
import Motor
#import servoDMA
import time
import RPi.GPIO as GPIO
import curses
import thread
from RPIO import PWM

#inicializa
GPIO.setmode(GPIO.BCM)

#cria os dois encoders
encoderDireita = encoder.Encoder(19)
encoderEsquerda = encoder.Encoder(26)

#cria os dois motores
motorDireita = Motor.Motor(27,17)
motorEsquerda = Motor.Motor(8,7)
Enable1=22 #Enable motorDireito
Enable2=25 #Enable motorEsquerdo

#cria o servo da camera
ServoCam=13 #Controle Servo da Camera

def camdireita():
	PWM.add_channel_pulse(0, ServoCam, 100, 220 )

def camesquerda():
	PWM.add_channel_pulse(0, ServoCam, 100, 5 )

def camcentro():
	PWM.add_channel_pulse(0, ServoCam, 100, 120 )

#comeca a Curses e comeca o loop
stdscr = curses.initscr() #Inicia Curses
curses.noecho()  #Desabilita Verbose Terminal - Curses
curses.cbreak()  #Habilita terminal para apenas um caractere - Curses
stdscr.keypad(1) #Habilita Uso do Teclado Numerico - Curses
stdscr.refresh() #Atualiza Tela - Curses
PWM.setup() #Inicia PWM - RPIO/PWM
PWM.init_channel(0) #Inicia Canal PWM para Servo Camera - RPIO/PWM

#---LOOP PRINCIPAL
tecla = ''
while tecla != ord('q'):
   tecla = stdscr.getch()
   if tecla == curses.KEY_UP:
      motorDireita.frente()
      motorEsquerda.frente()
      time.sleep(1)	
      motorDireita.parar()
      motorEsquerda.parar()		
   elif tecla == curses.KEY_DOWN:
      motorDireita.re()
      motorEsquerda.re()
      time.sleep(1)
      motorDireita.parar()
      motorEsquerda.parar()
   elif tecla == curses.KEY_LEFT:
      motorDireita.frente()
      motorEsquerda.re()
      time.sleep(1)	
      motorDireita.parar()
      motorEsquerda.parar()
   elif tecla == curses.KEY_RIGHT:
      motorDireita.re()
      motorEsquerda.frente()
      time.sleep(1)
      motorDireita.parar()
      motorEsquerda.parar()
   elif tecla == ord('a'):
	    camesquerda()
   elif tecla == ord('d'):
	    camdireita()
   elif tecla == ord('s'):
	    camcentro()
                     
#---FINALIZACAO
PWM.clear_channel_gpio(0, ServoCam)  #Limpa Canal 0 do Servo da Camera
PWM.cleanup() # Limpa Pinos de PWM
stdscr.keypad(0) #Desabilita Teclado Numerico
curses.nocbreak() #Desabilita Curses
curses.echo()     #Habilita Verbose Terminal
curses.endwin()   #Desliga Biblioteca Curses
GPIO.cleanup()    #Limpa Pinos GPIO


