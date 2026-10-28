palavra:str = "estacionamento"

#e s t a c i o n a m  e  n  t  o
#0 1 2 3 4 5 6 7 8 9 10 11 12 13

contador:int = 0
while(contador < 14 ):
 if ( palavra[contador] !="a"):
     print(palavra[contador])
     contador= contador + 1   
 else:
     contador += 1
     continue
