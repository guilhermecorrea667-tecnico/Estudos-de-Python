hidrometro_anterior:float =float(input("digite o hidrometro antigo:"))
hidrometro_atual:float = float(input("digite o hidro atual:"))

if(hidrometro_anterior > hidrometro_atual):
   resultado =  hidrometro_anterior - hidrometro_atual
  
else:
     resultado = hidrometro_atual - hidrometro_anterior


print (f" Gasto de agua é {resultado}")

if ( resultado > 20 ):
    print ("O valor ultapassou o consumo")



valor_a_pagar = resultado * 5
print (f" O valor a pagar é {valor_a_pagar}")



