def f_none(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))
print(f(4))
print(f_none(1))
print(f_none(2))
print(f_none(3))
print(f_none(4))
