print("Sistema de calificaciones")

#Hacemos la respectiva validacion para que no deje ingresar ningun otro valor no que sea un entero
while True:
    try:
        #Entrada de datos
        nota = float(input("Ingresa una calificacion de 0 a 100: "))
        #Validacion de que este en el rango de 0 a 100 y diga si aprobo o no
        if type(nota).__name__== "float" and nota >= 0 and nota <= 100:
            if nota >= 60:
                print("Aprobaste, felicidades!!!")
            else:
                print("Sigue intentandolo, tu puedes!")
            break
        else:
             print("Error! Ingresa valores positivos y dentro del rango")
        
    except ValueError:
        print("Error! Ingresa un valor correcto")

print("------------------------------")
#Dentro de este while hacemos la entrada de datos de la lista y validamos para que no entren valores erroneos
calificaciones = []
while True:
        try:
            numero_ingresado = int(input("Cuantas calificaciones quieres ingresar? "))
            if type(numero_ingresado).__name__ == "int":
                #Con este for se recorrera la lista y se guardaran los valores en esta
                for i in range(numero_ingresado):
                    calificacion = float(input(f"Ingresa la {i+1} calificacion:"))
                    if calificacion >= 0 and calificacion <= 100:
                        #append es un método que agrega un elemento al final de una lista
                        calificaciones.append(calificacion)
                    else:
                        #Si el usuario 
                        print("Solo puedes ingresar valores en el rango de 0 a 100")
                break
        except ValueError:
            print("ERROR!! Ingresa un valor válido")

for promedio in calificaciones:
    #Utilizamos la funcion sum para sumar todos los elementos que hay en la lista y 
    # la funcion len para saber la longitud de la lista y dividirla por el resultado de la suma, con esto podemos conocer el promedio.
    promedio = sum(calificaciones) / len(calificaciones)
    
print(f"El promedio fue: {promedio}")



while True:
    try:
        valor_especifico = float(input("Ahora ingresa un valor alterno al de las las calificaciones, por favor -> "))
        if type(valor_especifico).__name__ == "float":
            break
    except ValueError:
        print("ERROR!! Ingresa un valor válido")
    

contador = 0
repeat = 0
for calificacion in calificaciones:
        if calificacion > valor_especifico :
            contador += 1
        if calificacion == valor_especifico:
            repeat += 1
    
print(f"Se encontraron {contador} calificaciones mayor a {valor_especifico}")
print(f"El valor ingresado se repite {repeat}")