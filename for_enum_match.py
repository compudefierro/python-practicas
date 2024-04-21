# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        
for indice, user in enumerate(users.items()):
    print(indice, user)
    
nombres = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(nombres)):
    print(i, nombres[i])
    
for indice, nombre in enumerate(nombres):
    print(indice, nombre)
    
    
opcion = 2
match opcion:
    case 1:
        print('opcion 1')
    case 2:
        print('opcion 2')
    case _:
        print('opcion incorrecta')
        
opcion_tupla = (1, 2)
match opcion_tupla:
    case (1, 1):
        print('opcion 1,1')
    case (1, 2):
        print('opcion 1,2')
    case _:
        print('tupla erronea')
        
# point is an (x, y) tuple
opcion_tupla = (2,0)
match opcion_tupla:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
    
from enum import Enum
class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    
color = Color('red')
print(color)
match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
        
