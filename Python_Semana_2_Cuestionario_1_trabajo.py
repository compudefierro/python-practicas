# Tus amigos deciden organizar una completada (una reunión para comer hot dogs). Para evitar que todos traigan ketchup y nadie traiga salchichas, decides crear un programa en Python que verifique la variedad de ingredientes. Tienes una lista de listas con los ingredientes que tiene cada uno de tus amigos.
ingredientes_amigos = [
    ['Pan', 'Salchichas', 'Mostaza', 'Ketchup'], #ingr. amigo 1
    ['Pan', 'Tomate', 'Chucrut'], #ingr. amigo 2
    ['Ketchup','Salchichas'], #ingr. amigo 3
    ['Chucrut', 'Pan'] #ingr. amigo 4
]

ingredientes_favoritos = ['Pan', 'Tomate', 'Salchichas', 'Chucrut', 'Mostaza', 'Ketchup', 'Mayonesa', 'Palta']

for amigo in ingredientes_amigos:
    for ingrediente in amigo:
        if ingrediente in ingredientes_favoritos:
            ingredientes_favoritos.remove(ingrediente)
print(ingredientes_favoritos)


# Tu jefe te acaba de mencionar que los datos deben tener como valor mínimo el 0. ¿Cuál de los siguientes códigos reemplaza todos los valores negativos en la lista por ceros?

lista = [[-1, 2, -5, 40],
         [9, 65, -6, -34],
         [0, -4, 9, 2]
        ]

fils = len(lista)
cols = len(lista[0])
for i in range( fils ):
    for k in range( cols ):
        if lista[i][k] < 0:
            lista[i][k] = 0
            
print(lista)

# Cada elemento de esta lista es una lista con 2 valores: el nombre de un candidato y la cantidad de votos que recibió. ¿Cuál de los siguientes códigos imprime correctamente el nombre del candidato que recibió la mayor cantidad de votos?

votos = [['Alicia', 35],
         ['Bob', 42],
         ['Carlos', 29],
         ['David', 33]
]

mejor = ['', 0]
for candidato in votos:
    if candidato[1] > mejor[1]:
        mejor = candidato
print(mejor[0])


# Tienes una lista con datos de una estación meteorológica, esta contiene los strings 'soleado', 'nublado' o 'lluvia'. Siempre después de lluvia viene un float con la cantidad de milímetros de agua que cayeron durante la llovizna. Un ejemplo de esta lista es:
lista = ['soleado', 'nublado', 'soleado', 'lluvia', 2.4, 'lluvia', 0.1, 'nublado', 'lluvia', 0.8]
suma = 0
for i in lista:
    if i not in ['soleado','nublado','lluvia']:
        suma += i
print(suma)


d = ['Alicia', 'Bob', 'Carlos', 'David']    # lista de dueños
m = ['Pelusa', 'Luke', 'Mickey', 'Madonna'] # lista de mascotas

# El dueño en la posición 0 tiene la mascota en la posición 0, el dueño en la posición 1 tiene la mascota en la posición 1 y así. Quieres imprimir el nombre de cada dueño seguido del nombre de su mascota. Por ejemplo, para las listas anteriores quieres imprimir:
for i in range(len(d)):
    print(d[i], m[i])
    
    
lista = ['Alicia', 'Bob', 'Carlos', 'David']

# Quieres imprimir el nombre de los clientes de atrás hacía adelante. Por ejemplo, para la lista anterior deberás imprimir:

while len(lista) > 0:
    ultimo_cliente = len(lista) - 1
    cliente = lista.pop(ultimo_cliente)
    print(cliente)
    
lista = ['Alicia', 1998, 'Bob', 1990, 'Carlos', 1986, 'David', 2001]
# Quieres imprimir el nombre de cada cliente seguido de su año de nacimiento. Por ejemplo, para la lista anterior quieres imprimir:
for i in range(0,len(lista),2):
    nombre = lista[i]
    nacimiento = str(lista[i+1])
    print(nombre, nacimiento)
