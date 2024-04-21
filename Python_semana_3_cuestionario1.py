tupla = (1,2,3,5,6,7,8,9)

m1 = ('Toy Story', 1995, '01:21', ['animacion', 'comedia'])

(nombre, anno, duracion, categorias) = m1
categorias = ['animacion',  'comedia', 'infantil' ]
print(categorias)
print(m1)

tupla = (2.0, 4.7, 6.8, 5.1)

lista = []
for nota in tupla:
    lista.append(nota)
lista[0] = 3.2

print(tupla)
print(lista)

clientes = ['Alicia', 'Bob', 'Carlos', 'David']
clientes_nuevos = ('Eva', 'Fabricio', 'Gloria')

for cliente in clientes_nuevos:
    clientes.append(cliente)
    
print(clientes)

from collections import deque

deq = deque( (1,4,5,3,2) )

print(deq)

print( deq.popleft() )
print( deq.pop() )
print( deq.pop() )
print( deq.popleft() )
print( deq.count(5) * 5 )

series = deque()
series.append('You')
series.append('Community')
series.append('Breaking Bad')
series.popleft()

print(series)


fila1 = deque()
fila2 = deque()
fila3 = deque()
filas = ( fila1, fila2, fila3 )
def elegir_fila(filas, cliente):
    mejor_fila = filas[0]
    for fila in filas:
        if len(fila) < len(mejor_fila):
            mejor_fila = fila
    mejor_fila.append( cliente )
    
fila1.append('jorge')
elegir_fila(filas, 'raul' )
print(fila1,fila2,fila3)


deq = deque( (1,2,3,4,5) )

deq2 = deque()
for i in deq:
    deq2.append( i )
deq = deq2

print(deq)


pasajeros_prioritarios = deque()
pasajeros = deque()
tripulacion = deque()

pasajeros_prioritarios.append('Jorge')
pasajeros.append('raul')
tripulacion.append('marcelo')

print(pasajeros_prioritarios, pasajeros, tripulacion)
for cola in (( pasajeros_prioritarios, pasajeros, tripulacion )):
    while len(cola) > 0:
        cola.popleft()
print(pasajeros_prioritarios, pasajeros, tripulacion)



