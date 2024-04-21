vuelos = [ ['Origen', 'Destino', 'precio', 'asientos disponibles', 'Fecha'],
['Santiago', 'Puerto Montt', 35000, 30, '11 Enero 2023'],
['Santiago', 'Concepción', 30000, 40, '20 Febrero 2023'],
['Santiago', 'Puerto Montt', 28000, 2, '19 Enero 2023'],
['Santiago', 'Puerto Montt', 12000, 100, '20 Mayo 2023'],
['Antofagasta', 'Santiago', 27000, 14, '18 Abril 2023' ]
]

# vuelos_disponibles(vuelos, 'Santiago', 'Puerto Montt', 5)
# [
# ['Origen', 'Destino', 'precio', 'asientos disponibles', 'Fecha'],
# ['Santiago', 'Puerto Montt', 35000, 30, '11 Enero 2023'],
# ['Santiago', 'Puerto Montt', 12000, 100, '20 Mayo 2023']
# ]

def vuelos_disponibles(vuelos, origen, destino, pasajeros):
    vuelos_encontrados = [['Origen', 'Destino', 'precio', 'asientos disponibles', 'Fecha']]
    for item in vuelos:
        if item[0] == origen and item[1] == destino and item[3] >= pasajeros:
            vuelos_encontrados.append(item)
    return vuelos_encontrados
print(vuelos_disponibles(vuelos, 'Santiago', 'Puerto Montt', 5))


lista1 = [
['Nombre', 'Numero alumno', 'Correo', 'Nota final'],
['Alicia', 16848, 'amartinez@gmail.com', 5.7],
['Marco', 19845, 'marenas@gmail.com', 4.8]
]

lista2 = [
['Numero alumno', 'Nota final', 'Nombre', 'Color favorito'],
[16848, 5.7, 'Alicia', 'Rojo'],
[19845, 4.8, 'Marco', 'Verde'],
[19515, 6.2, 'Federico', 'Azul']
]

# [('Alicia', 5.7), ('Marco', 4.8) ]
# [('Alicia', 5.7), ('Marco', 4.8), ('Federico', 6.2) ]

def notas_alumnos(lista):
    # Buscamos los índices correspondientes a 'Nombre' y 'Nota final' en el header
    header = lista[0]
    nombre_index = header.index('Nombre')
    nota_index = header.index('Nota final')

    # Creamos una lista de tuplas con el nombre y la nota final de cada alumno
    notas = [(alumno[nombre_index], alumno[nota_index]) for alumno in lista[1:]]

    return notas
print(notas_alumnos(lista1))
print(notas_alumnos(lista2))

paises = [
[0, 'España', 'Madrid'],
[2, 'Alemania', 'Berlin'],
[1, 'Francia', 'Paris'],
[3, 'Italia', 'Roma']
]

belleza = [
[2, 0.57],
[1, 0.81],
[3, 0.68],
[0, 0.62]
]

def paises_bellos(paises, belleza):
    # Creamos un diccionario para mapear los ids de país con su índice de belleza
    belleza_dict = {pais[0]: indice for pais in belleza for indice in pais}

    # Creamos una lista de tuplas con el nombre del país y su índice de belleza
    paises_con_belleza = [(pais[1], belleza_dict[pais[0]]) for pais in paises]

    # Ordenamos la lista de tuplas según el índice de belleza (de mayor a menor)
    paises_con_belleza.sort(key=lambda x: x[1], reverse=True)

    return paises_con_belleza
print(paises_bellos(paises,belleza))