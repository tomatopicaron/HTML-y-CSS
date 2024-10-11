

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
    

#git sistema de control de versiones distrubuido
#permiten trabajar sin coneccion y de forma remota
#es un clon
#un sistema de controles sentralizado es un computador o servidor master al que hay que ir a descargar su inf
#una rama es indendiente a la rama principal y funciona para probar todo antes de moverlo a la principal
#el merch ya es unir el trabajo
#el comit se encargada de almacenar la informacion del proyecto
#github es una plataforma de almacenamiento de codigo


Tiempo = int(input("Ingrese el tiempo de uso en horas. ejmpo: 2"))

1 == 900
2 == 1000
4 == 1500


if Tiempo == 1:
    print ("debe pagar"(1))

elif Tiempo == 2:
    print ("debe pagar"(2))

elif Tiempo == 3:
    print ("debe pagar"(1+2))

elif Tiempo == 4:
    print ("debe pagar"(4))

else:
    print ("valor invalido")
    
    #1 ACTIVIDAD IF

def calcular_precio(horas): 

    if horas == 1: 

        precio = 900 

     

    elif horas == 2: 

        precio =1000 

     

    elif horas == 4: 

        precio = 1500 

     

    else: 

        precio = horas*400 #aqui calcule un precio justo para las cantidades no especificadsa 

     

    return precio 

horas = int(input("ingrese numero de horas. ejm: 2")) 

 

precio = calcular_precio(horas) 

print(f"precio por{horas} horas es: {precio}") 

 