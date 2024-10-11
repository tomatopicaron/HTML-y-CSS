def f(x):
    # Definir aquí la función cuya raíz se desea encontrar
    return x**3 - 2*x - 5  # Ejemplo: f(x) = x^3 - 2x - 5

def bolzano(a, b, E):
    if f(a) * f(b) > 0:
        print("Error: La función tiene el mismo signo en los extremos.")
        return None

    while (b - a) / 2 > E:
        c = (a + b) / 2  # Punto medio
        if f(c) == 0:
            return c  # Si c es la raíz exacta
        elif f(a) * f(c) < 0:
            b = c  # La raíz está en el intervalo [a, c]
        else:
            a = c  # La raíz está en el intervalo [c, b]

    c = (a + b) / 2  # Valor aproximado de la raíz
    return c

# Entradas del usuario
a = float(input("Ingrese el extremo inferior del intervalo (a): "))
b = float(input("Ingrese el extremo superior del intervalo (b): "))
E = float(input("Ingrese el error máximo permitido (E): "))

# Calcular y mostrar la raíz
raiz = bolzano(a, b, E)
if raiz is not None:
    print(f"El valor C que está a menos de {E} del valor c es: {raiz:.5f}")
    
#tablero

def bolzano(f, a, b, E):
    # Verificar si la función tiene el mismo signo en los extremos
    if f(a) * f(b) > 0:
        raise ValueError("La función tiene el mismo signo en los extremos")

    # Inicializar el intervalo
    a_n = a
    b_n = b

    # Iterar hasta alcanzar el error máximo permitido
    while True:
        # Calcular el punto medio
        c_n = (a_n + b_n) / 2

        # Verificar si el punto medio es el cero
        if abs(f(c_n)) < E:
            return c_n

        # Actualizar el intervalo
        if f(a_n) * f(c_n) < 0:
            b_n = c_n
        else:
            a_n = c_n

# Definir la función
def f(x):
    return x**2 - 2

# Datos de entrada
a = 0
b = 2
E = 0.001

try:
    c = bolzano(f, a, b, E)
    print(f"El cero de la función está en x = {c:.4f}")
except ValueError as e:
    print(e)