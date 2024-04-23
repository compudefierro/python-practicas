lista = ['jorge', 'osvaldo', 'dri']
lista2 = lista.copy()
lista_frutas = ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
print(id(lista), id(lista2))
print(lista, lista2)
print(lista_frutas.count('banana'))

lista_frutas = ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']

filtro = [x for x in lista_frutas if x == 'pear']

print(filtro)
from random import randint
matris = [[ x for x in range(randint(0,10))],[ x for x in range(randint(0,6))],[ x for x in range(randint(0,6))],[ x for x in range(randint(0,6))]]
print(matris)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
print([[fila[i] for fila in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
    
print(transposed)

transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)

transposed = []
transposed = list(zip(*matrix))
print(transposed)