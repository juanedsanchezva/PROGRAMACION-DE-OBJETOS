


palabra = input("Escribe una palabra:  ")

a = 0
A = 0
e = 0
E = 0
i = 0
I = 0
o = 0
O = 0
u = 0
U = 0

for letra in palabra:
    if letra == 'a':
        a += 1
    elif letra == 'e':
        e += 1
    elif letra == 'i':
        i += 1
    elif letra == 'o':
        o += 1
    elif letra == 'u':
        u += 1
    elif letra == 'A':
        A += 1
    elif letra == 'E':
        E += 1
    elif letra == 'I':
        I += 1
    elif letra == 'O':
        O += 1
    elif letra == 'U':
        U += 1



print("Cantidad de vocales:")
print(f"a: {a}")
print(f"e: {e}")
print(f"i: {i}")
print(f"o: {o}")
print(f"u: {u}")
print(f"A: {A}")
print(f"E: {E}")
print(f"I: {I}")
print(f"O: {O}")
print(f"U: {U}")