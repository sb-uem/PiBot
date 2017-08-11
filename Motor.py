import RPI.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Motor(object):
	
	def __init__(self,pino1,pino2):
		self.pino1=pino1 #Pino 1 do motor
		self.pino2=pino2 #Pino 2 do motor
		self.parar()

	def frente(self):
		GPIO.output(self.pino1,1)
		GPIO.output(self.pino2,0)

	def re(self):
		GPIO.output(self.pino1,0)
		GPIO.output(self.pino2,1)
		
	def parar(self):
		GPIO.output(self.pino1,1)
		GPIO.output(self.pino2,1)
