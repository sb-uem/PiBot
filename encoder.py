estadoanterior = LOW

def encoder_confere(estadoatual,i,alfa):
  if ((estadoatual) != (estadoanterior)):
    i =i+1
    alfa = i*18
    estadoanterior = estadoatual
    estadoatual = leitura
 
def encoder_zera(i,alfa):  
  i = 0
  alfa = 0
