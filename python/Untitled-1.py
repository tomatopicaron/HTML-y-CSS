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