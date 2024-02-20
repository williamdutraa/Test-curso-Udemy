minha_lista2 = [1,2,3,4,5,6]
minha_lista = ["abacaxi", "abacate","laranja", "mamao"]
lista = [2.00, 8.00, 10.00, 5.00]

for nome, numero, valor in zip(minha_lista,minha_lista2, lista):
    print (numero, nome, valor)