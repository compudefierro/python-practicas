# string a lista usando la coma como separador de elemento en la nueva lista
cadena = "jorge osvaldo dri, masculino, 43, monotributista"
lista_con_split = cadena.split(",")

# string a lista usando bucle for
lista_con_bucle = []
inicio = 0
for i in range(0, len(cadena)):
    if cadena[i] == ",":
        lista_con_bucle.append(cadena[inicio:i])
        inicio = i + 1
lista_con_bucle.append(cadena[inicio:])

print(lista_con_split)
print(lista_con_bucle)

lista_compras = ["pan", "huevo", "queso", "arroz", "jamon"]
lista_compras.append("maní")
lista_compras.remove("arroz")
lista_compras.insert(2,"leche")

print(lista_compras)


datos = [2, "Julio", 2017, "Final", 14.5, "Chile", 0, "Alemania", 1]
trozo = datos[2:6]
print(trozo)

datos = ["semillas", 500, "cerveza", 2, "despacho", 4100, "pago", "bitcoin", "confianza", 95.4]
trozo = datos[1:9:2]
print(trozo)

unidades = [40, 32, 49, 2, 20, 8, 55, 300, 10]
muestra = unidades[2:4] + unidades[6:8]
print(muestra)

resultados = [ ["Alfredo",20], ["Marcela",40], ["Ignacio",30], ["Loreto",10] ]
def ganadorv2(votos):
  mayor = votos[len(votos)-1]
  for cand in votos:
    if cand[1] >= mayor[1]:
      mayor = cand
  return mayor
def ganador(votos):
  mayor = votos[0]
  for cand in votos:
    if cand[1] > mayor[1]:
      mayor = cand
  return mayor
mayoria = ganador(resultados)
print(mayoria)

tablero = [ [1,2,3], [4,5,6], [7,8,9] ]
# for j in range(3):
#   for i in range(3):
#     print(tablero[j][i],end=" ")
for i in range(9):
  print(tablero[i%3][i//3],end=" ")
# for i in range(3):
#   for j in range(3):
#     print(tablero[j][i],end=" ")

elem = 2
conjunto = [2,3,4,2,2]

def cuantasv1(elem, conjunto):
  contador = 0
  for k in range(len(conjunto)):
    if conjunto[k] == elem:
      contador += 1
  return contador

def cuantas(elem, conjunto):
  contador = 0
  for e in conjunto:
    if e == elem:
      contador += 1
  return contador

print(" ")
print(cuantas(elem,conjunto))


def buscaminas(tablero, i, j):
    # Inicializamos un contador para las bombas alrededor de la posición (i, j)
    bombas_alrededor = 0
    
    # Verificamos las posiciones alrededor de (i, j) y contamos las bombas
    for delta_i in [-1, 0, 1]:
        for delta_j in [-1, 0, 1]:
            # Evitamos contar la misma posición (i, j)
            if delta_i == 0 and delta_j == 0:
                continue
            
            # Calculamos las coordenadas de la posición vecina
            vecino_i = i + delta_i
            vecino_j = j + delta_j
            
            # Verificamos si la posición vecina está dentro del tablero
            if 0 <= vecino_i < len(tablero) and 0 <= vecino_j < len(tablero[0]):
                # Incrementamos el contador si encontramos una bomba en la posición vecina
                if tablero[vecino_i][vecino_j] == 'X':
                    bombas_alrededor += 1
    
    return bombas_alrededor

# Tablero de ejemplo
tablero = [[' ', 'X', ' ', 'X'],
           ['X', ' ', ' ', ' '],
           [' ', 'X', 'X', ' '],
           ['X', ' ', ' ', 'X']]

# Ejemplos de uso
print(buscaminas(tablero, 0, 0))  # Debería imprimir 2
print(buscaminas(tablero, 1, 1))  # Debería imprimir 4


def color_frecuente(lista):
    conteo = {}
    for color in lista:
        if color in conteo:
            conteo[color] += 1
        else:
            conteo[color] = 1
    
    # Encontrar el máximo número de ocurrencias
    max_ocurrencias = max(conteo.values())
    
    # Encontrar el color más frecuente según las prioridades
    colores_prioritarios = ["azul", "rojo", "verde", "amarillo"]
    color_mas_frecuente = None
    for color in colores_prioritarios:
        if color in conteo and conteo[color] == max_ocurrencias:
            color_mas_frecuente = color
            break
    
    return color_mas_frecuente, max_ocurrencias

# Ejemplo de uso
lista_colores = ['azul', 'rojo', 'verde', 'verde', 'verde', 'rojo', 'verde', 'verde', 'azul', 'amarillo', 'azul', 'azul', 'verde', 'verde', 'verde', 'amarillo', 'amarillo']
resultado = color_frecuente(lista_colores)
print("Color más frecuente:", resultado[0])
print("Número de ocurrencias:", resultado[1])


import math

def promedio_std(lista):
    # Calcula el promedio
    promedio = sum(lista) / len(lista)
    
    # Calcula la suma de los cuadrados de las diferencias respecto al promedio
    suma_cuadrados_diff = sum((x - promedio) ** 2 for x in lista)
    
    # Calcula la desviación estándar
    desviacion_estandar = math.sqrt(suma_cuadrados_diff / len(lista))
    
    return (promedio, desviacion_estandar)

# Ejemplo de uso
numeros = [2, 4, 6, 8, 10]
resultado = promedio_std(numeros)
print("Promedio:", resultado[0])
print("Desviación estándar:", resultado[1])

import math

def promedio_std(lista):
    # Calcula el promedio
    promedio = sum(lista) / len(lista)
    
    # Calcula la suma de los cuadrados de las diferencias respecto al promedio
    suma_cuadrados_diff = sum((x - promedio) ** 2 for x in lista)
    
    # Calcula la desviación estándar
    desviacion_estandar = math.sqrt(suma_cuadrados_diff / len(lista))
    
    return promedio, desviacion_estandar

# Ejemplo de uso
numeros = [2, 4, 6, 8, 10]
promedio, std_dev = promedio_std(numeros)
print("Promedio:", promedio)
print("Desviación estándar:", std_dev)
