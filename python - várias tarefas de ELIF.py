def exercicio1():
    n1 = float(input("coloque o primeiro numero: "))
    n2 = float(input("coloque o segundo numero: "))

    if n1 > n2:
        print(f"O maior numero é {n1}")
    elif n2 > n1:
        print(f"O maior numero é {n2}")
    else:
        print("Mesmo numero")


def exercicio2():
    nota = float(input("digite a nota do aluno: "))

    if nota >= 6:
        print("aprovado.")
    else:
        print("reprovado.")

def exercicio3():
    n1 = float(input(" coloque o primeiro numero:"))
    n2 = float(input(" coloque o segundo numero:"))
    operacao = input(" digite a operação (+,-,/,*):")

    if operacao == "+":
        resultado = n1 + n2
        print(f"Resultado:{resultado}")
    elif operacao == "-":
        resultado = n1-n2
        print(f"Resultado:{resultado}")
    elif operacao == "*":
        resultado = n1*n2
        print(f"Resultado:{resultado}")
    elif operacao == "/":
        if n2 != 0:
            resultado = n1 / n2
            print(f"Resultado:{resultado}")
        else:
            print("Erro: Divisão por zero.")
    else:
        print("Operação inválida.")
                  
def exercicio4():
    numero = float(input("coloque um numero:"))
    if numero > 0:
         print("Numero positivo")
    elif numero < 0:
          print("Numero negativo")
    else:
          print("zero")

def exercicio5():
    usuario = input("coloque o nome de usuario:")
    senha = input("coloque a senha:")
    if usuario=='admin' and senha=='1234':
     print("Login bem sucedido")
    else:
        print("Acesso negado ")

def exercicio6():
    n = int(input("digite um numero inteiro:"))
    if n % 2==0:
        print("numero é par")
    else:
        print("numero é ímpar")
    
def exercicio7():
    idade=int(input("digite a idade:"))
    if idade <=12:
        print("Isso é criança")
    elif idade <=17:
        print("Isso é Adolescente")
    elif idade <=59:
        print("Isso é Adulto")
    else:
        print("Isso é idoso")

def exercicio8():
    # Solicita a nota do aluno
 nota = float(input("Digite a nota (0 a 10): "))
 
 # Classifica a nota de acordo com as faixas fornecidas
 if 9.0 <= nota <= 10.0:
    print("Saída: Nota A")
 elif 7.0 <= nota < 9.0:
    print("Saída: Nota B")
 elif 5.0 <= nota < 7.0:
    print("Saída: Nota C")
 elif 3.0 <= nota < 5.0:
    print("Saída: Nota D")
 elif 0.0 <= nota < 3.0:
    print("Saída: Nota F")
 else:
    print("Nota inválida. Digite um valor entre 0 e 10.")

 
opcao = int(input("Escolha um exercicio (1,2,3,4,5,6,7,8): "))

if opcao == 1:
    exercicio1()
elif opcao == 2:
    exercicio2()
elif opcao == 3:
    exercicio3()
elif opcao == 4:
    exercicio4()
elif opcao == 5:
    exercicio5()
elif opcao == 6:
    exercicio6()
elif opcao == 7:
    exercicio7()
elif opcao ==8:
    exercicio8()
else:
    print("Opção invalida")
