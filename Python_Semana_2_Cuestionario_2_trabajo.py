lista = [-40, -1, 1, 5, 16, 72, 100]

# Deberás definir la función agregar_entero(lista, entero), la cual recibe como parámetro una lista en el formato anterior y un entero cualquiera. La función deberá agregar el entero en la posición correcta de la lista y luego retornar la lista. Por ejemplo, si se llama la función: agregar_entero(L, 13), siendo L la lista anterior, entonces deberás retornar la lista:
# [-40, -1, 1, 5, 13, 16, 72, 100]

def agregar_entero(lista, entero):
    for item in lista:
        if item <= entero:
            next
        else:
            lista.insert(lista.index(item),entero)
            return lista
        
        if len(lista) -1  == lista.index(item):
            lista.insert(lista.index(item) + 1,entero)
            return lista


print(agregar_entero(lista,13))

print(agregar_entero(lista,71))

print(agregar_entero(lista,133))

print(agregar_entero(lista,132))


# Deberás definir la función max_repetido(lista), la cual recibe como parámetro una lista en el formato anterior. La función deberá retornar el número de veces que se repite el entero que se repite más veces dentro de la lista. En el ejemplo anterior, el entero que más se repite es el 1, el cual se repite 7 veces, por lo que tu función deberá retornar 7.

lista = [1,4,6,2,4,3,1,1,3,5,6,7,3,4,5,5,5,3,3,2,1,2,1,1,1,2,6,6]

def max_repetido(lista):
    # Creamos un diccionario para contar la frecuencia de cada elemento en la lista
    frecuencias = {}
    for elemento in lista:
        if elemento in frecuencias:
            frecuencias[elemento] += 1
        else:
            frecuencias[elemento] = 1
    
    # Encontramos el elemento con la frecuencia máxima
    max_frecuencia = max(frecuencias.values())
    
    return max_frecuencia

print(max_repetido(lista))


estudiantes = [
'Mario Avedaño',
'Policarpo Avedaño',
'Juan Bodoque',
'Juanin Harry',
'Mario Hugo',
'Dylan Manguera',
'Eusebio Manguera'
]


# Deberás definir la función agregar_estudiante(lista, estudiante), la cual recibe como parámetro una lista en el formato anterior y el nombre de un nuevo estudiante. La función deberá agregar al estudiante en la posición correcta (ordenado alfabéticamente por apellido y nombre) de la lista y luego retornar la lista. Por ejemplo, si en la lista anterior se agrega el estudiante 'Eliza Manguera', entonces tu función deberá retornar:
# ['Mario Avedaño',
# 'Policarpo Avedaño',
# 'Juan Bodoque',
# 'Juanin Harry',
# 'Mario Hugo',
# 'Dylan Manguera',
# 'Eliza Manguera',
# 'Eusebio Manguera'
# ]

def agregar_estudiante(lista, estudiante):
    # Buscar la posición correcta para insertar el nuevo estudiante
    index = 0
    while index < len(lista) and lista[index] < estudiante:
        index += 1
    
    # Insertar el nuevo estudiante en la posición encontrada
    lista.insert(index, estudiante)
    
    return lista

# Ejemplo de uso
estudiantes = [
    'Mario Avedaño',
    'Policarpo Avedaño',
    'Juan Bodoque',
    'Juanin Harry',
    'Mario Hugo',
    'Dylan Manguera',
    'Eusebio Manguera'
]
nuevo_estudiante = 'Eliza Manguera'
print(agregar_estudiante(estudiantes, nuevo_estudiante))


# ordenado alfabeticamente:
def agregar_estudiante(lista, estudiante):
    # Dividir el nuevo estudiante en nombre y apellido
    nombre_estudiante = estudiante.split()[0]
    apellido_estudiante = estudiante.split()[1]
    
    # Buscar la posición correcta para insertar el nuevo estudiante
    index = 0
    while index < len(lista):
        nombre_actual = lista[index].split()[0]
        apellido_actual = lista[index].split()[1]
        
        # Comparar alfabéticamente por apellido y luego por nombre
        if (apellido_actual, nombre_actual) > (apellido_estudiante, nombre_estudiante):
            break
        index += 1
    
    # Insertar el nuevo estudiante en la posición encontrada
    lista.insert(index, estudiante)
    
    return lista

# Ejemplo de uso
estudiantes = [
    'Mario Avedaño',
    'Policarpo Avedaño',
    'Juan Bodoque',
    'Juanin Harry',
    'Mario Hugo',
    'Dylan Manguera',
    'Eusebio Manguera'
]
nuevo_estudiante = 'Eliza Manguera'
print(agregar_estudiante(estudiantes, nuevo_estudiante))
