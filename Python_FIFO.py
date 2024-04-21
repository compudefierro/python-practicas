# FILO First In Last Out
# FIFO First in First Out

from collections import deque
# d.count(x)
# d.insert(i,x)
# d.reverse()
# d.rotate(n)
# d.pop()
# d.popleft()


# jugadores = ['Sandra', 'Felipe', 'Miguel', 'Julieta']
# while jugadores != []:
#     j = jugadores.pop(0)
#     opcion = input(j + ": quieres R o S? ")
#     if opcion == "S":
#         print("***Turno de ", j, "***")
#         jugadores.append(j)
#     print(jugadores)
# print("No quedan mas jugadores")

# usando collections.deque:
jugadores = ['Sandra', 'Felipe', 'Miguel', 'Julieta']
d = deque(jugadores)
while len(d) != 0:
    j = d.popleft()
    opcion = input(j + ": quieres R o S? ")
    if opcion == "S":
        print("***Turno de ", j, "***")
        d.append(j)
        print(d)
    print(d)
print("No quedan mas jugadores")
