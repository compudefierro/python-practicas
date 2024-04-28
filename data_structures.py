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

# Tuples and Sequences
tuple_nested = ([1,2,3],[3,2,1])
print(tuple_nested, type(tuple_nested))
tuple_nested[0].append(4)
tuple_nested[1].insert(0,4)
print(tuple_nested, type(tuple_nested))

# Sets
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)

# Demonstrate set operations on unique letters from two words
set_a = set('abracadabra')
set_b = set('alacazam')
print(f'letters in a but not in b: \t{set_a - set_b} \nletters in a or b or both: \t{set_a | set_b}\nletters in both a and b: \t{set_a & set_b}\nletters in a or b but not both: {set_a ^ set_b}')

# Set: list comprehensions:
set_comp_a = {x for x in 'abracadabra' if x not in 'abc'}
print(set_comp_a)
