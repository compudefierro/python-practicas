def factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * factorial_recursivo(numero - 1)


print(factorial_recursivo(10))