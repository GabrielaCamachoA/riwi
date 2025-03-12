nombre = input("Ingrese el nombre del producto -> ")
valor_producto = int(input('Ingrese el valor del producto -> '))
cantidad = int(input("Ingrese la cantidad del producto -> "))
descuento = int(input("Ingrese el porcentaje del descuento -> "))
costo_sin_descuento = (valor_producto * cantidad)


if (type(valor_producto).__name__ == "int" and valor_producto > 0):
  print("-------")
  print("Valor correcto!")
else:
   print("-------")
   print("El valor ingresado no es flotante o positivo" )


if (type(cantidad).__name__ == "int" and cantidad > 0):
   print("-------")
   print("Valor correcto!")
else:
    print("-------")
    print("La cantidad ingresada no es un número entero o positivo")

while not 0 < descuento or descuento> 100:
  print("----------")
  print("Ingresa un número valido para el porcentaje")
  descuento = int(input("Ingrese el porcentaje del descuento -> "))
print("Puedes continuar")
costo_a_descontar = (costo_sin_descuento * descuento)/100
costo_total = (costo_sin_descuento - costo_a_descontar)

    

print("------------------------------------------------------------")
print(f"El costo sin descuento es ${costo_sin_descuento:,.0f}")
print(f"Valor descontado ${costo_a_descontar:,.0f}")
print(f"El costo total es ${costo_total:,.0f}")

print("------------------------------")
print(f"Nombre del producto:    {nombre}")
print(f"Valor unitario:         ${valor_producto:,.0f}")
print(f"Cantidad de productos:  {cantidad}")
print(f"Descuento aplicado:     {descuento}%")
print(f"Valor sin descuento:    ${costo_sin_descuento:,.0f}")
print("----------------")
print(f"Costo total:            ${costo_total:,.0f}")
