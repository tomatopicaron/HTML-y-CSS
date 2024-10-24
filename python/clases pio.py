suma = 0
for i in range (1,21):
    suma += i **2
print(suma)

a, b = 0, 1
while b <1000:
    print(b)
    a,b = b, a + b
    
suma = 0

for i in range(1,51):
    suma += i 
    print(suma)
    
numero = int(input("aqui va el numero"))
while numero >=1:
    print (numero) 
    numero -= 1
    
total = 0
while total < 100:
    number = int(input("ingrese un número: "))
    total += number
print(f"Total acumulado: {total}")


for i in range(10):
    if i == 5:
        break
    print(i)
    
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    
    

puntaje = int(input("ingrese su puntaje"))

if puntaje > 100:
    print ("puntaje no valido")
    
if puntaje >= 90:
    print ("Exelente papáaaaa!")
    
if puntaje >= 75:
    print ("es bueno si")

if puntaje >= 50:
    print ("esta bien, pasas")

else: 
    print ("Perdiste, a estudiar papá!")
    

def num1():
    print("Piensa un numero entre 1 y 1000")
    minimo = 1
    maximo = 1000
    intentos = 0

    while intentos < 10:
        intentos += 1
        numero = (minimo + maximo) // 2
        print(f"¿El número es {numero}?")

        respuesta = input("Responde con <, > o =: ")

        if respuesta == "=":
            print(f"El numero es {numero}")
            print(f"Intentos: {intentos}")
            return

        elif respuesta == "<":
            if numero == minimo:
                print("estas haciendo trampa. ¿se te olvido el numero?")
                return
            maximo = numero - 1

        elif respuesta == ">":
            if numero == maximo:
                print("estas haciendo trampa. ¿se te olvido el numero?")
                return
            minimo = numero + 1

        else:
            print("caracter incorrecto, responde con <, > o =")

    print("No pude adivinar el número en 10 intentos")

num1()

def es_bisiesto(año):
    if año % 4 == 0:
        if año % 100 == 0:
            if año % 400 == 0:
                return True  # Año bisiesto
            else:
                return False  # No es un año bisiesto
        else:
            return True  # Año bisiesto
    else:
        return False  # No es un año bisiesto

# Ejemplo de uso
año = int(input("Introduce un año: "))
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
    

def calcular_resistencia(voltage, current):
    if current == 0:
        return "La corriente no puede ser cero, ya que no se puede calcular la resistencia."
    resistencia = voltage / current
    return resistencia

def main():
    print("Cálculo de Resistencia Eléctrica")
    
    try:
        voltage = float(input("Introduce el voltaje (en voltios): "))
        current = float(input("Introduce la corriente (en amperios): "))
        
        resistencia = calcular_resistencia(voltage, current)
        print(f"La resistencia eléctrica es: {resistencia:.2f} ohmios")
        
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")

if __name__ == "__main__":
    main()

# Función para calcular la raíz cuadrada
def calcular_raiz_cuadrada(numero):
    if numero < 0:
        return "No se puede calcular la raíz cuadrada de un número negativo."
    else:
        return math.sqrt(numero)

# Ejemplo de uso
numero = float(input("Introduce un número: "))
resultado = calcular_raiz_cuadrada(numero)
print(f"La raíz cuadrada de {numero} es {resultado}")

import numpy as np

# Listas de ejemplo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
y = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]

# Dividir las listas en 8 partes iguales
x_dividido = np.array_split(x, 8)
y_dividido = np.array_split(y, 8)

# Imprimir las divisiones
for i in range(8):
    print(f"Parte {i+1}:")
    print(f"x: {x_dividido[i]}")
    print(f"y: {y_dividido[i]}")