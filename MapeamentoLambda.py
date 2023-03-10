"""
mapeando a lista lista para elevar cada elemento ao quadrado. 
Estamos usando uma lambda expression com o argumento x para calcular o quadrado de cada elemento e retornar uma nova lista.

"""


lista = [1, 2, 3, 4, 5]
lista_mapeada = list(map(lambda x: x ** 2, lista))
print(lista_mapeada)
