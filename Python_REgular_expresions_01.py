import re

string = """
Jornada financiera: las acciones argentinas subieron hasta 12% en Wall
Street y los bonos llegaron a un precio récord desde 2020 El S&P Merval ganó
5,2%, a 1.124.136 puntos. Medido en dólares llegó al nivel de agosto de 2018.
Los bonos Globales subieron 1,1% en promedio y el riesgo país cedió a 1.581 puntos.
El dólar libre quedó a $1.025 y el BCRA compró USD 67000 millones en el mercado
"""


p = re.compile(r"\d{4}")

text = re.findall(p, string)

print(text)


result = re.search(fr"\d{{3}}", string)
print(result)

# Buscar todos los números en la cadena
numeros_encontrados = re.findall(r'\d+', string)

print(numeros_encontrados)

# Buscar todos los números en la cadena junto con su posición
numeros_encontrados = re.finditer(r'\d+', string)
numeros_encontrados_2 = re.finditer(r'\d+', string)

for match2 in numeros_encontrados_2:
    print(match2)

# Mostrar los números encontrados con sus posiciones
for match in numeros_encontrados:
    numero = match.group()
    inicio = match.start()
    fin = match.end()
    print(f"Número: {numero}, Posición inicio: {inicio}, Posición fin: {fin}")

string_corta = "Jornada financiera: las acciones argentinas subieron hasta "

print(re.match(r"\w{2}", string_corta))

string2 = "abc123"
print("Cadena de entrada:", string2)

resultado = re.match(r"\w{3}", string2)
print("Resultado:", resultado)

print(re.findall(r".{12}", string))

