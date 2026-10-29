ditadura:str=input('bota alguma coisa:')
tabua:str=input('bote dnv:')

print(f'resolução:{ditadura}(tamanho:{len(ditadura)})')
print(f'resolução:{tabua}(tamanho:{len(tabua)})')

if len(ditadura) ==len(tabua):
    print('O comprimento  é igual')
else:
    print('o comprimento é diferente')


if ditadura == tabua:
    print('é conteudo igual')
else:
    print('é conteudo diferente')
