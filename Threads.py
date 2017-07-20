
import _thread
import time

def f1(arg2, arg1):
   for i in range(10):
      print('Função1')
      time.sleep(1)

def f2(n, a):
   for j in range(5):   
      print('Função2')
      time.sleep(2)


_thread.start_new_thread(f1, ('Texto', 1))
_thread.start_new_thread(f2, ('Texto', 1))
time.sleep(11)
