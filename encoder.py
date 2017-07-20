class Encoder(object):
  
  def __init__(self,pino):
        self.estadoanterior = LOW
        self.pino = pino
        self.encoder_zera()
        
      
  def encoder_confere(self):
    self.estadoatual = self.leitura #feita no GPIO de self.pino 
    if ((self.estadoatual) != (self.estadoanterior)):
      self.i = self.i+1
      self.alfa = self.i*18
      self.estadoanterior = self.estadoatual
      
   
  def encoder_zera(self):  
   self.i = 0
   self.alfa = 0
  
encoderdir=classEncoder(19)
encoderesq=classEncoder(26)

 

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
