#CODIGO MOTOR

import RPI.GPIO as GPIO
import time

Enable1=17 #Enable Motor 1
Enable2=25 #Enable Motor 2

MD1=27  #MotorDireitoEntrada1
MD2=22  #MotorDireitoEntrada2
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

def FRENTE(tempo):
	t=float(tempo)
	# MOTOR 1
	GPIO.OUTPUT(MD1 ,1) # IN1
	GPIO.OUTPUT(MD2 ,0) # IN2
	# MOTOR 2
	GPIO.OUTPUT(ME1 ,1) # IN3
	GPIO.OUTPUT(ME2 ,0) # IN4
	time.sleep(t)
	PARAR()

def RE(tempo):
	t=float(tempo)
	# MOTOR 1
	GPIO.OUTPUT(MD1 ,0) # IN1
	GPIO.OUTPUT(MD2 ,1) # IN2
	# MOTOR 2
	GPIO.OUTPUT(ME1 ,0) # IN3
	GPIO.OUTPUT(ME2 ,1) # IN4
	time.sleep(t)
	PARAR()

def ROTA(tempo,dir):
	t=float(tempo)
	d=int(dir)
	IF d == 1: #direita 
		# MOTOR 1
		GPIO.OUTPUT(MD1 ,0) # IN1
		GPIO.OUTPUT(MD2 ,1) # IN2
		# MOTOR 2
		GPIO.OUTPUT(ME1 ,1) # IN3
		GPIO.OUTPUT(ME2 ,0) # IN4
		time.sleep(t)
		PARAR()
	IF d == 0: #esquerda
		# MOTOR 1
		GPIO.OUTPUT(MD1 ,1) # IN1
		GPIO.OUTPUT(MD2 ,0) # IN2
		# MOTOR 2
		GPIO.OUTPUT(ME1 ,0) # IN3
		GPIO.OUTPUT(ME2 ,1) # IN4
		time.sleep(t)
		PARAR()

def PARAR():
	# MOTOR 1
	GPIO.OUTPUT(MD1 ,1) # IN1
	GPIO.OUTPUT(MD2 ,1) # IN2
	# MOTOR 2
	GPIO.OUTPUT(ME1 ,1) # IN3
	GPIO.OUTPUT(ME2 ,1) # IN4
