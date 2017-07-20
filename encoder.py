class Encoder(object):
  
  def __init__(self,estadoanterior):
        self.estadoanterior = LOW
      
  def encoder_confere(self,estadoatual,i,alfa):
   if ((self.estadoatual) != (self.estadoanterior)):
      self.i = self.i+1
      self.alfa = self.i*18
      self.estadoanterior = self.estadoatual
      self.estadoatual = self.leitura
   
  def encoder_zera(self,i,alfa):  
   self.i = 0
   self.alfa = 0
  
encoderdir=classEncoder()
encoderesq=classEncoder()

 

def encoder_confere(estadoatual,i,alfa):
  if ((estadoatual) != (estadoanterior)):
    i =i+1
    alfa = i*18
    estadoanterior = estadoatual
    estadoatual = leitura
 
def encoder_zera(i,alfa):  
  i = 0
  alfa = 0
  
def encoder_conferedir(estadoatual,i,alfa):
  if ((estadoatual) != (estadoanterior)):
    i =i+1
    alfa = i*18
    estadoanterior = estadoatual
    estadoatual = leitura

def encoder_zeradir(i,alfa):  
  i = 0
  alfa = 0    
    
def encoder_confereesq(estadoatual,i,alfa):
  if ((estadoatual) != (estadoanterior)):
    i =i+1
    alfa = i*18
    estadoanterior = estadoatual
    estadoatual = leitura
    
def encoder_zeraesq(i,alfa):  
  i = 0
  alfa = 0
