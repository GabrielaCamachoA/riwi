#Ejercicio 1
""" usuario = ("Gabriela", "Camacho", "90")

for edad in usuario:
        edad = int(usuario[2])
        if edad < 18:
            continue
        if edad > 60:
            print("Se encontró una persona mayor de 60 años")
            break """


#Ejercicio 2
""" numeros = [1,2,3,4,5,6,7,8,9,10]

while True:
    for i in range (10):
        par = numeros[i]
        if par % 2 == 0: 
            print(par)
    break """


#Ejercicio 3
""" numero = [30,-2,100,20,200,60]
while True:
    for j in range(6):
        num = numero[j]
        if num < 0:
            print("Se encontro un numero negativo")
        if num > 100:
            continue
        if num > 50:
            print(f"Estos fueron los numeros mayores a 50: {num}")
    break """


#Ejercicio 4
""" for i in range (1,200):
    if i % 4 == 0:
        continue
    elif i > 150:
        break
    print(i) """


#Ejercicio 5
""" numeros_ingresados = 0
while True: 
    try:
        numero = int(input("Ingresa un numero entero: "))
        numeros_ingresados+=1
        if type(numero).__name__ != "int":
          numero = int(input("Ingresa un numero entero: "))
        elif numero < 0:
          print("Se encontro un numero negativo")
          continue
        elif numero == 0:
          print(f"Hiciste {numeros_ingresados} intentos")
          break
    except ValueError:
       print("Error!!!") """


#Ejercicio 6
""" texto = "HolaAchicOs, saludos"
iteracion = 0
for vocal in texto:
    if vocal == "a" or vocal == "A" or vocal == "e" or vocal == "E" or vocal == "i" or vocal == "I" or vocal== "o" or vocal == "O" or vocal== "u" or vocal == "U":
        print("Vocal")
        iteracion += 1
        continue
    if vocal == " ":
        break
print(f"El total de vocales encontradas fueron: {iteracion}") """