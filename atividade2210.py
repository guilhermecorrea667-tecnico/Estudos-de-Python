nome:str = ""
cafe:str = ""
valorconsumo:float = 0.0
desconto:float = 0.0
quantidade:int = 0
resultado:float = 0.0

nome:str=input("Informe seu nome:")

print("O nome do cliente eh:",nome)

cafe:str=input("Informe o nome do produto:")
valorconsumo:float = float (input(" Informe o preço:"))
quantidade:int = int(input(" Quantidade a comprar:"))

resultado:float = valorconsumo * quantidade

print(f"Nome:{nome} \n Produto:{cafe}\n preço:{valorconsumo}\n quantidade: {quantidade}\n total:{resultado}")      
                   
if((resultado ==50.0)or(resultado > 50.0)):
    print("irei dar o desconto")
    desconto:float = resultado/10
    print(f"Desconto:{desconto}\n")
    resultado = resultado - desconto
    print(f"A pagar:{resultado}\n")
else:
    print("ahhh não terá desconto")
