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

destinos = ["Cartagena", "San Andres", "Santa Marta"]
vueloOrigen = ["Cali", "Bogota", "Medellin"]
clasesVuelo = ["Economica", "Ejecutiva", "Primera Clase"]

precioVuelos = {
    "Cartagena": {"cali": 240000, "bogota": 198000, "medellin": 200000},
    "San Andres": {"cali": 280000, "bogota": 220000, "medellin": 210000},
    "Santa Marta": {"cali": 200000, "bogota": 150009, "medellin": 219323} 
}
clases = {
    "Economica": 1.0,
    "Ejecutiva": 1.5,
    "Primera Clase": 2.0
}
while True:
  print("\n ✈ -- BIENVENIDO A TOP NOTCH TRAVEL -- ✈")
  print("\n OPCIONES DEL USUARIO")
  print("1. Ingresa  Tus Datos")
  print("2. Reserva Tu Vuelo Ahora")
  print("3. Reserva Ya Tu Hotel Preferido")
  print("4. Explora Tus  Paquete De Turismo")
  print("5. Crea Tu Propio Plan De Viaje")
  print("6.salir")

  opcion = input("Por favor, digita una de las opciones: ")
##############-----------------------------------------opciones para escojer por seccion----------------------------#########
  if opcion == "1":
    

    def obtener_datos_usuario():
        # Solicitar datos al usuario
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        cedula = input("Ingrese su cedula: ")
        correo = input("Ingrese su correo electrónico: ")
        celular = (input("Ingrese su número de celular: "))
        direccion = input("Ingrese su dirección de residencia: ")

        # Imprimir los datos ingresados
        print("\nLos datos ingresados son:")
        print(f"Nombre: {nombre}")
        print(f"Apellido: {apellido}")
        print(f"cedula: {cedula}")
        print(f"Correo: {correo}")
        print(f"Celular: {celular}")
        print(f"Dirección de Residencia: {direccion}")

    # Llamar a la función
    obtener_datos_usuario()

  if opcion == "2":
   
    print("✈  Bienvenido al sistema de reserva de vuelos ᯓ ✈")

    # en este apartado nos encargamos de seleccionar el lugar de origen, usamos el sistema de bucles para no inciar el codigo cada vez que se digita mal un valor
    while True:
        print("Ingresa tu vuelo de origen. Las ubicaciones disponibles son:", vueloOrigen)
        ciudadOrigen = input("Ingresa tu ciudad de origen: ").capitalize()
        if ciudadOrigen in vueloOrigen:
            break
        print("La ciudad de origen ingresada no es válida. Inténtalo nuevamente.")

    # Seleccionamos el destino, solo estan habilitados lso 3 disponibles
    while True:
        print("¿A dónde quieres ir? Los lugares disponibles son:", destinos)
        ciudadDestino = input("Ingresa tu ciudad de destino: ").title()
        if ciudadDestino in destinos:
            break
        print("La ciudad de destino ingresada no es válida. Inténtalo nuevamente.")

    # ingresamos el total de pasajeros, en esta linea fue necesario la busqueda de una alternativa ya que al tratarse de un numero entero debemos asegurar que al ingresar texto nos arroje un tipo de error 
    while True:
        try:
            cantidadPasajeros = int(input("Ingresa la cantidad de pasajeros: "))
            if cantidadPasajeros > 0:
                break
            else:
                print("La cantidad de pasajeros debe ser un número positivo. Inténtalo nuevamente.")
        except ValueError:
            print("Entrada no válida. Debe ser un número entero. Inténtalo nuevamente.")

    # Seleccionamos la clase con la que queremos viajar
    while True:
        print("¿En qué clase deseas viajar? Las clases disponibles son:", clasesVuelo)
        clasedeViaje = input("Selecciona una clase: ").title()
        if clasedeViaje in clasesVuelo:
            break
        print("Clase no válida. Inténtalo nuevamente.")

    # Preguntar si el viaje es de ida y vuelta
    while True:
        opciondeVuelo = input("¿Es un vuelo de ida y vuelta? (Responda Si o No): ").lower()
        if opciondeVuelo in ["si", "no"]:
            idayvuelta = opciondeVuelo == "si"
            break
        print("Respuesta no válida. Debe ser 'Si' o 'No'. Inténtalo nuevamente.")

    # Calculamos el precio
    precioBase = precioVuelos[ciudadDestino][ciudadOrigen.lower()]
    precioconClase = clases[clasedeViaje]
    precioTotal = precioBase * precioconClase * cantidadPasajeros

    if idayvuelta:
        precioTotal *= 2 

    print(f"El precio total de su viaje es: ${precioTotal}")
  elif opcion == "3":
   
 #------------Cartagena-----------
    hoteldecameron = {
        "Precio de adulto en Decameron": 300000,
        "Precio de niño en Decameron": 150000,
        "Alimentacion en Decameron": "Incluye el desayuno"
    }
    hotelestrella = {
        "Precio de adulto en Estrella": 200000,
        "Precio de niño en Estrella": 100000,
        "Alimentacion en Estrella": "Incluye el desayuno y la cena"
    }
    hotellindanoche = {
        "Precio de adulto en Linda": 140000,
        "Precio de niño en Linda": 70000,
        "Alimentacion en Linda": "No incluye alimentacion"
    }

    #--------------Santa Marta----------
    hotellacascada = {
        "Precio de adulto en La Cascada": 180000,
        "Precio de niño en La Cascada": 90000,
        "Alimentacion en La Cascada": "Incluye el desayuno"
    }
    hotelbellarely = {
        "Precio de adulto en Bellarely": 150000,
        "Precio de niño en Bellarely": 75000,
        "Alimentacion en Bellarely": "No incluye alimentacion"
    }
    hotelresort = {
        "Precio de adulto en El Resort": 220000,
        "Precio de niño en El Resort": 110000,
        "Alimentacion en El Resort": "Incluye el desayuno y la cena"
    }

    #-------------San Andres-----------------
    hotelsolcaribe = {
        "Precio de adulto en Sol Caribe": 200000,
        "Precio de niño en Sol Caribe": 100000,
        "Alimentacion en Sol Caribe": "No incluye alimentacion"
    }
    hoteldorado = {
        "Precio de adulto en Dorado": 250000,
        "Precio de niño en Dorado": 125000,
        "Alimentacion en Dorado": "Incluye el desayuno"
    }
    hotelcoral = {
        "Precio de adulto en Coral": 320000,
        "Precio de niño en Coral": 160000,
        "Alimentacion en Coral": "Incluye el desayuno y la cena"
    }

    #-----------------------Modulo de reserva------------------------------------------
    print("----🛎🏠︎-----Bienvenido al módulo de reserva de hoteles-----🏠︎🛎----")
    print("--Nuestros destinos disponibles para ti son:--")
    print("--Cartagena, Santa Marta y San Andrés--")
    # se solicita la informacion al usuario necesaria para brindar la informacion correspondiente 
    Destino = input("Ingrese el destino de su reserva de hotel: ").lower()
    cantidadAdultos = int(input("Ingresa la cantidad de adultos: "))
    cantidadNiños = int(input("Ingresa la cantidad de niños: "))
    cantidadDias = int(input("Ingresa el número de días de hospedaje: "))
    if Destino == "cartagena":
    # el usuario tiene la posibilidad de elegir el hotel que mejor se acomode a su presupuesto y a su comodidad 
        hotelCartagena = input("¿En qué hotel le interesa hospedarse?: Hotel Decameron, Hotel Estrella y Hotel Linda Noche:  ").strip().lower()
        if hotelCartagena == "hotel decameron":
            print(hoteldecameron)
            totalAdultos = cantidadAdultos * hoteldecameron["Precio de adulto en Decameron"] * cantidadDias
            totalNiños = cantidadNiños * hoteldecameron["Precio de niño en Decameron"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        elif hotelCartagena == "hotel estrella":
            print(hotelestrella)
            totalAdultos = cantidadAdultos * hotelestrella["Precio de adulto en Estrella"] * cantidadDias
            totalNiños = cantidadNiños * hotelestrella["Precio de niño en Estrella"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        elif hotelCartagena == "hotel linda noche":
            print(hotellindanoche)
            totalAdultos = cantidadAdultos * hotellindanoche["Precio de adulto en Linda"] * cantidadDias
            totalNiños = cantidadNiños * hotellindanoche["Precio de niño en Linda"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        else:
            print("Hotel no válido. Por favor, seleccione un hotel correcto.")

    elif Destino == "santa marta":
        hotelSantaMarta = input("¿En qué hotel le interesa hospedarse?: Hotel La Cascada, Hotel Bellarely y Hotel Resort:  ").strip().lower()
        if hotelSantaMarta == "hotel la cascada":
            print(hotellacascada)
            totalAdultos = cantidadAdultos * hotellacascada["Precio de adulto en La Cascada"] * cantidadDias
            totalNiños = cantidadNiños * hotellacascada["Precio de niño en La Cascada"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        elif hotelSantaMarta == "hotel bellarely":
            print(hotelbellarely)
            totalAdultos = cantidadAdultos * hotelbellarely["Precio de adulto en Bellarely"] * cantidadDias
            totalNiños = cantidadNiños * hotelbellarely["Precio de niño en Bellarely"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        elif hotelSantaMarta == "hotel resort":
            print(hotelresort)
            totalAdultos = cantidadAdultos * hotelresort["Precio de adulto en El Resort"] * cantidadDias
            totalNiños = cantidadNiños * hotelresort["Precio de niño en El Resort"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        else:
            print("Hotel no válido. Por favor, seleccione un hotel correcto.")

    elif Destino == "san andres":
        hotelSanAndres = input("¿En qué hotel le interesa hospedarse?: Hotel Sol Caribe, Hotel Dorado y Hotel Coral:  ").strip().lower()
        if hotelSanAndres == "hotel sol caribe":
            print(hotelsolcaribe)
            totalAdultos = cantidadAdultos * hotelsolcaribe["Precio de adulto en Sol Caribe"] * cantidadDias
            totalNiños = cantidadNiños * hotelsolcaribe["Precio de niño en Sol Caribe"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        elif hotelSanAndres == "hotel dorado":
            print(hoteldorado)
            totalAdultos = cantidadAdultos * hoteldorado["Precio de adulto en Dorado"] * cantidadDias
            totalNiños = cantidadNiños * hoteldorado["Precio de niño en Dorado"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        elif hotelSanAndres == "hotel coral":
            print(hotelcoral)
            totalAdultos = cantidadAdultos * hotelcoral["Precio de adulto en Coral"] * cantidadDias
            totalNiños = cantidadNiños * hotelcoral["Precio de niño en Coral"] * cantidadDias
            print(f"El precio total de la reserva es: {totalAdultos + totalNiños}")
        else:
            print("Hotel no válido. Por favor, seleccione un hotel correcto.")
    else:
        print("Destino no válido. Por favor, seleccione un destino correcto.")
        
  elif opcion == "4":
      # Paquetes turísticos pre-armados con hoteles
    paquetes_turisticos = [
        {
            "destino": "Cartagena",
            "duracion": 5,  # en días
            "precio": 1200000,
            "descripcion": "Disfruta del Caribe, la ciudad amurallada y playas paradisíacas.",
            "hoteles": ["Hotel Decamerón", "Hotel Estrella", "Hotel Linda Noche"]
        },
        {
            "destino": "San Andrés",
            "duracion": 4,  # en días
            "precio": 1500000,
            "descripcion": "Un paraíso de mar de siete colores, snorkeling y playas cristalinas.",
            "hoteles": ["Hotel Sol Caribe", "Hotel Dorado", "Hotel Coral"]
        },
        {
            "destino": "Santa Marta",
            "duracion": 6,  # en días
            "precio": 1100000,
            "descripcion": "Conoce el Parque Tayrona y relájate en las playas del Caribe.",
            "hoteles": ["Hotel La Cascada", "Hotel Bellarely", "Hotel Resort"]
        }
    ]

    # Mostrar los paquetes turísticos disponibles con numeración
    print("\n ---✈︎ જ⁀➴ ⛰︎ ---Bienvenido al modulo de seleccion de paquetes --- ✈︎ જ⁀➴ ⛰︎---")
    print("Paquetes Turísticos Disponibles:")
    for i, paquete in enumerate(paquetes_turisticos, start=1):
        print(f"\n[{i}] Destino: {paquete['destino']}")
        print(f"    Duración: {paquete['duracion']} días")
        print(f"    Precio: ${paquete['precio']:,}")
        print(f"    Descripción: {paquete['descripcion']}")

    # Solicitar al usuario que elija un paquete
    while True:
        try:
            eleccion_paquete = int(input("\nIngrese el número del paquete que desea elegir: "))
            if 1 <= eleccion_paquete <= len(paquetes_turisticos):
                paquete_elegido = paquetes_turisticos[eleccion_paquete - 1]
                break
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(paquetes_turisticos)}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Mostrar los hoteles disponibles en el paquete elegido
    print(f"\nHoteles disponibles en {paquete_elegido['destino']}:")
    for j, hotel in enumerate(paquete_elegido["hoteles"], start=1):
        print(f"[{j}] {hotel}")

    # Solicitar al usuario que elija un hotel
    while True:
        try:
            eleccion_hotel = int(input("\nIngrese el número del hotel que desea elegir: "))
            if 1 <= eleccion_hotel <= len(paquete_elegido["hoteles"]):
                hotel_elegido = paquete_elegido["hoteles"][eleccion_hotel - 1]
                break
            else:
                print(f"Por favor, ingrese un número entre 1 y {len(paquete_elegido['hoteles'])}.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

    # Mostrar las características del paquete y hotel elegidos
    print("\nEl paquete elegido es el siguiente: ")
    print(f"Destino: {paquete_elegido['destino']}")
    print(f"Duración: {paquete_elegido['duracion']} días")
    print(f"Precio: ${paquete_elegido['precio']:,}")
    print(f"Descripción: {paquete_elegido['descripcion']}")
    print(f"Hotel Seleccionado: {hotel_elegido}")
        
      

      

  elif opcion == "5":
    actividades_Escogidas = []

    
    print("\n -----⛱--------Aquí podrás armar tu paquete de actividades---------🏝--------")
    print("--------------recuerda que contamos con destinos a Cartagena, Santa Marta y San Andres---------")

    dias_en_destino = int(input("por favor ingrese cauntos días va a estar en este destino: "))
    print(f"ha seleccionado esta cantidad de días: {dias_en_destino}")

    destino = input("Por favor introduce el destino al cual te gustaría armar tu paquete de actividades: ").lower()
    print(f"el destino que ha ingresado es: {destino}")


    if destino == "cartagena":
        actividades_car =["castillo de san felipe","islas del rosario","tour ciudad amurallada", "tour nocturno rumbero"]
        print("Las actividades que tenemos son:  ")
        print("\n castillo de San Felipe")
        print("\n  Islas Del Rosario")
        print("\n tour ciudad amurallada")
        print ("\n tour nocturno rumbero")
        
        i = 1
        while dias_en_destino > len(actividades_Escogidas):

            actividades_seleccionadas= input(f"por favor escoja la actividad correspondiente al día {i} : ").lower()
            if actividades_seleccionadas in actividades_car:
                actividades_Escogidas.append(actividades_seleccionadas)
                i = i + 1
            else:
             print("Esa actividad no se encuentra aquí")
        for diasfinal in range(dias_en_destino):
            print(f"estas son sus actividades escogidas en su paquete por día {diasfinal + 1} = {actividades_Escogidas[diasfinal]}")
        

    elif destino == "santa marta":
        actividades_santa =["parque tayrona","minca","tour del graffiti", "tour nocturno rumbero", "tour museos"]
        print("Las actividades que tenemos son:  ")
        print("\n parque tayrona")
        print("\n  minca")
        print("\n tour del graffiti")
        print ("\n tour nocturno rumbero")
        print ("\n tour museos")

        
        i = 1
        while dias_en_destino > len(actividades_Escogidas):

            actividades_seleccionadas = input(f"por favor escoja la actividad correspondiente al día {i} : ").lower()
            if actividades_seleccionadas in actividades_santa:
                actividades_Escogidas.append(actividades_seleccionadas)
                i = i + 1
            else:
             print("Esa actividad no se encuentra aquí")
        for diasfinal in range(dias_en_destino):
            print(f"estas son sus actividades escogidas en su paquete por día {diasfinal + 1} = {actividades_Escogidas[diasfinal]}") 
        

    elif destino == "san andres":
        actividades_sanan =["hoyo soplador","tour de los 7 colores","recorrido en jeep", "aventura parapente", "jhony cay"]
        print("Las actividades que tenemos son:  ")
        print("\n hoyo soplador")
        print("\n  tour de los 7 colores")
        print("\n recorrido en jeep")
        print ("\n aventura parapente")
        print ("\n jhony cay")

        
        i = 1
        while  dias_en_destino > len(actividades_Escogidas) :

            actividades_seleccionadas = input(f"por favor escoja la actividad correspondiente al día {i} : ").lower()
            if actividades_seleccionadas in actividades_sanan:
                actividades_Escogidas.append(actividades_seleccionadas)
                i = i + 1
            else:
             print("Esa actividad no se encuentra aquí")
        
        for diasfinal in range(dias_en_destino):
            print(f"estas son sus actividades escogidas en su paquete por día {diasfinal + 1} = {actividades_Escogidas[diasfinal]}")          
            
    else:
     print("Este destino no se encuentra en la lista de nuestros destinos, por favor verifique nuevamente")
  elif opcion == "6":
      break
            
    
        
   
  
    

    #######-----------------------------------------#####--------------------------------------------------------------------##################
