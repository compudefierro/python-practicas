"""
nombres = ['jorge', 'raul', 'mirta']
apellidos = ['dri', 'dri', 'picolini']
nombre_completo=zip(nombres,apellidos)
lista_nombres_completos = list(nombre_completo)
for item in lista_nombres_completos:
    for iterar in item:
        print(iterar)

nombre_unzip, apellido_unzip = zip(*lista_nombres_completos)
"""

nombres = [
    'jorge',
    'raul',
    'mirta',
    'sebastian'
    ]

nombres_enumerados = enumerate(nombres)
print(list(nombres_enumerados))
for indice, valor in nombres_enumerados:
    print(indice, valor)