"""
ordenando a lista de tuplas lista com base no segundo elemento de cada tupla (o preço do produto). 
Estamos usando uma lambda expression com o argumento x para acessar o segundo elemento de cada tupla e usá-lo como chave de ordenação.

"""


lista = [('produto1', 10), ('produto2', 5), ('produto3', 20)]
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(lista_ordenada)
