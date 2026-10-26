sala:str = ""
iniciohora:int = 0
qtd_alunos:int = 0
tolerancia:int = 0
premio:str = ""
atrasado:str = ""
qtd_atrasado:int = 0

#Carregando os dados nas variaveis

sala:str = input("Informe a turma:")
iniciohorario:int = int(input("Inicio:"))
qtd_alunos:int = int(input("quantidade alunos:"))
tolerancia:int = int(input("Tolerancia:"))
premio:str = input("Qual o premio:")
contador:int = 1
while( contador < qtd_alunos):

  #Parte das regras
  atrasado:str = input ("Nome do aluno:")
  horario:int = int(input("Hora Chegada:"))
  if (horario> (iniciohorario+tolerancia)):
    print(f"Aluno {atrasado} atrasado chegou {horario}h")
    print(premio)
    qtd_atrasado = qtd_atrasado + 1
  else:
    print(f"Aluno {atrasado} chegou no {horario}h")
  contador = contador + 1
print(f"atrasado: {qtd_atrasado} ")
print(f"premio:{qtd_atrasado} x {premio}")
