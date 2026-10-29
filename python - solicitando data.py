meses = ['' , 'janeiro' , 'fevereiro', 'março', 'abril', 'maio', 'junho','julho','agosto','setembro','outubro','novembro','dezembro']
data = input('data de nascimento dd/mm/aaaa:')
if len(data) == 10:
  dia= data[0:2]
  mes= data[3:5]
  print(dia,'de',meses[int(mes)])
else:
    print('por favor , escreve direito')
