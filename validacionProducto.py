#Entrada de la información

nombre = input("Ingrese el nombre del producto -> ")

#Procesamiento de la línea 11 hasta la 38

#Validación de que sí sea un número float y mayor que 0 para que el usuario no pueda ingresar un valor negativo, 
# por lo tanto cada vez que ingrese un valor negativo se le repetira que ingrese un valor positivo hasta que se cumpla.
#Así será para las demás validaciones y estaremos valindado que los números si sean enteros y mayor a 0.

while True: 
  try:
    valor_producto = float(input('Ingrese el valor del producto -> '))
    if (type(valor_producto).__name__ == "float" and valor_producto > 0):
      break
  except ValueError:
    print("-------")
    print("El valor que ingresaste no es valido")
   

while True: 
  try:
    cantidad = int(input("Ingrese la cantidad del producto -> "))
    if (type(cantidad).__name__ == "int" and cantidad > 0):
      break
  except ValueError:
    print("-------")
    print("El valor que ingresaste no es valido")


while True: 
  try:
    descuento = int(input("Ingrese el porcentaje del descuento -> "))
    #Acá validamos si el descuento esta dentro del rango de 0 a 100 y positivo
    if type(descuento).__name__ == "int" or type(descuento).__name__ == "int" > 100:
      break
  except ValueError:
    print("-------")
    print("El valor que ingresaste no es valido")


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
