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