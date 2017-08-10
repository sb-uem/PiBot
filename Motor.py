import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

Enable1=22 #Enable Motor 1
Enable2=25 #Enable Motor 2

#Set Enable High
GPIO.output(Enable1,1)
GPIO.output(Enable2,1)

class Motor(object):
	
	def __init__(self,md1,md2,me1,me2):
		self.md1=md1 #MotorDireitoEntrada1
		self.md2=md1 #MotorDireitoEntrada2
		self.me1=me1 #MotorEsquerdoEntrada1
		self.me2=me2 #MotorEsquerdoEntrada2
		self.parar()

	def frente(self):
		GPIO.output(self.md1,1)
		GPIO.output(self.md2,0)
		GPIO.output(self.me1,1)	
		GPIO.output(self.me2,0)

	def re(self):
		GPIO.output(self.md1,0)
		GPIO.output(self.md2,1)
		GPIO.output(self.me1,0)
		GPIO.output(self.me2,1)

	def direita(self):
		GPIO.output(self.md1,0)
		GPIO.output(self.md2,1)
		GPIO.output(self.me1,1)
		GPIO.output(self.me2,0)

	def esquerda(self):
		GPIO.output(self.md1,1)
		GPIO.output(self.md2,0)
		GPIO.output(self.me1,0)
		GPIO.output(self.me2,1)		

	def parar(self):
		GPIO.output(self.md1,1)
		GPIO.output(self.md2,1)
		GPIO.output(self.me1,1)
		GPIO.output(self.me2,1)
