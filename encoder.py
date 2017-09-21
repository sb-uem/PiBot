import RPi.GPIO as GPIO

class Encoder(object):
  
  def __init__(self,pino):
        self.estadoanterior = False
        self.pino = pino
		  GPIO.setup(pino, GPIO.IN, pull_up_down=GPIO.PUD_UP)
		  self.encoder_zera()
      
  def encoder_confere(self):
    self.estadoatual = GPIO.input(self.pino);  
    if ((self.estadoatual) != (self.estadoanterior)):
      self.i = self.i+1
      self.alfa = self.i*18
      self.estadoanterior = self.estadoatual
   
  def encoder_zera(self):  
   self.i = 0
   self.alfa = 0
  
 
