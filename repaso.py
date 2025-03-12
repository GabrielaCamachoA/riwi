""" nombre = input("Cuál es tu nombre? ")
apellido = input("Cuál es tu apellido? ")
edad = int(input("Cuántos años tienes? "))
altura =  float(input("Ingresa tu altura -> "))
respirar_bajo_el_agua = input("Puedes respirar bajo el agua? ")

print(f"Hola yo soy {nombre} {apellido}, tengo {edad} años y mido {altura}")
print(f"Puede respirar bajo el agua? {respirar_bajo_el_agua}") """

#Ejercicio 1
""" nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingres tu edad: "))

print(f"Hola {nombre}, tienea {edad} años") """

#Ejercicio 2
""" num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa otro numero: "))
suma = num1 + num2
print(f"La suma de {num1} y {num2} es de: {suma} ") """


#Ejercicio 3
""" num1 = float(input("Ingresa un número: "))
num2 = float(input("Ingresta otro numero: "))
ope = float(num1 * num2)
print(f"El resultado de la multiplicación es: {ope}") """


#Ejercicio 4
""" numero = int(input("Ingresa un número: "))
doble = numero * numero
triple = numero * 3
print(f"El doble de {numero} es {doble} y el triple de {numero} es {triple}") """


#Ejercicio 5
""" palabra = input("Ingresa una palabra: ")
veces_repetida = int(input("Ingresa el numero de veces que quieres que se repita: "))
print(palabra * veces_repetida) """


#Ejercicio 6
""" num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa el segundo número: "))
div = num1 / num2
print(f"El resultado de la división es: {div}") """


#Ejercicio 7
""" name = input("Ingresa tu nombre: ")
letras = len(name)
print(f"Tu nombre tiene {letras} letras") """


#Ejercicio 8
""" num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
div = num1 // num2
mod = num1 % num2
print(f"El resultado de la división es: {div} y el módulo entre ellos es {mod}") """


#Ejercicio 9
""" print("Ingresa dos números para realizr 4 operaciones matemáticas")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
suma = num1 + num2
resta = num2 - num1
ope = num1 * num2
div = num1 / num2
print(f" El resultado de la suma es: {suma}, de la resta: {resta}, de la multiplicación: {ope} y de la división: {div}") """


#Ejercicio 10
""" num = int(input("Ingresa un número: "))
print(f"El cuadrado de {num} es {num ** 2} y el cubo es {num ** 3}") """


#Ejercicio 11
""" num = float(input("Ingresa un número decimal: "))
print(int(num)) """


#Ejercicio 12
""" edad = int(input("Cuántos años tienes? "))
mayor = edad >= 18
menor = edad < 18
print(f"Tu edad es mayor que 18? {mayor}")
print(f"Tu edad es menor que 18? {menor}") """


#Ejercicio 13
""" num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
twins = num1 == num2
print(f"Los números son iguales? {twins}") """

#Ejercicio 14
""" num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
mayor = num1 > num2
print(f"El primer número es el mayor? {mayor}") """


#Ejercicio 15
""" num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
menor_o_igual = num1 <= num2
print(f"El primer número es menor o igual? {menor_o_igual}")  """


#EJERCICIO 16
""" num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
mayor_que_diez = num1 > 10 and num2 > 10
print(f"Los números son mayores que 10? {mayor_que_diez}") """


#Ejercicio 17
""" num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
mayor_que_diez = num1 > 10 or num2 > 10
print(f"Alguno de los dos números es mayor que 10? {mayor_que_diez}")  """


#Ejercicio 18
""" num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))
validacion = num1 != num2
print(f"El primer número no es igual al segundo? {validacion}") """


#Ejercicio 19
""" print("Ingresa tres calificaciones para calcular el promedio ---------")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
promedio = (num1 + num2 + num3)/ 3
print(f"El promedio fue: {promedio}") """


#Ejercicio 20
numero = int(input("Ingresa un número: "))
divisible_entre_5 = numero % 5 == 0 
print(f"El número es divisible entre 5? {divisible_entre_5}")