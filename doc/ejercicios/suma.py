numeros_str = input("Dame tres numeros separados por espacios").split()
lista_numeros = list(map(int,numeros_str))

suma =sum(lista_numeros)
print(suma)