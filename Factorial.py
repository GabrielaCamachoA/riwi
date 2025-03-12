numero_del_usuario = int(input("Ingresa un número positivo:  "))
factorial = 1

for i in range(1, numero_del_usuario+1):
   factorial *= i 
   print(factorial)