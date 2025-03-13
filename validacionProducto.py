#Entrada de la información por el usuario de línea 3 hasta la 10

nombre = input("Ingrese el nombre del producto -> ")

#Utilizamos la función float para convertir la información str a número decimal
valor_producto = float(input('Ingrese el valor del producto -> '))

#Utilizamos la función int para convertir la información str a números enteros
cantidad = int(input("Ingrese la cantidad del producto -> "))
descuento = int(input("Ingrese el porcentaje del descuento -> "))


#Procesamiento de la línea 14 hasta la 40

#Validación de que sí sea un número float y mayor que 0 para que el usuario no pueda ingresar un valor negativo, 
# por lo tanto cada vez que ingrese un valor negativo se le repetira que ingrese un valor positivo hasta que se cumpla.
#Así será para las demás validaciones y estaremos valindado que los números si sean enteros y mayor a 0.

while not (type(valor_producto).__name__ == "float" and valor_producto > 0):
  print("-------------------------------------------------------------")
  print("El valor ingresado no es flotante o positivo" )
  valor_producto = float(input("Ingresa un valor positivo para el producto -> "))
print("-------")
print("Valor correcto!")


while not (type(cantidad).__name__ == "int" and cantidad > 0):
   print("--------------------------------------------------")
   print("La cantidad ingresada no es un número entero o positivo")
   cantidad = int(input("Ingresa una cantidad positiva para el producto -> "))
print("-------")
print("Valor correcto!")


#Acá validamos si el descuento esta dentro del rango de 0 a 100 y positivo
while not 0 < descuento or descuento> 100:
  print("-------------------------------------------------------")
  print("Ingresa un número positivo para el porcentaje")
  descuento = int(input("Ingrese el porcentaje del descuento -> "))
print("Puedes continuar")


#Hacemos las respectivas operaciones para saber el costo con y sin descuento y la cantidad total a pagar.
costo_sin_descuento = (valor_producto * cantidad)
costo_a_descontar = (costo_sin_descuento * descuento)/100
costo_total = (costo_sin_descuento - costo_a_descontar)

    
#Salida de la información
print("------------------------------------------------------------")
print(f"El costo sin descuento es ${costo_sin_descuento:,.0f}")
print(f"Valor descontado ${costo_a_descontar:,.0f}")
print(f"El costo total es ${costo_total:,.0f}")

print("")
print("------------------------------")
print(f"Nombre del producto:    {nombre}")
print(f"Valor unitario:         ${valor_producto:,.0f}")
print(f"Cantidad de productos:  {cantidad}")
print(f"Descuento aplicado:     {descuento}%")
print(f"Valor sin descuento:    ${costo_sin_descuento:,.0f}")
print("----------------")
print(f"Costo total:            ${costo_total:,.0f}")
