#pIDA 3 NÚMERO Y DIGA CUAL ES EL MAYOR
numero_1 = input('Ingrese numero1: ')
numero_1 = int(numero_1)

numero_2 = input('Ingrese numero:2: ')
numero_2 = int(numero_2)

numero_3 = input('Ingrese numero:3: ')
numero_3 = int(numero_3)

if numero_1 > numero_2 and numero_1 > numero_3:
    print(f'{numero_1}Es mayor: ')

elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f'{numero_2}Es mayor: ')

elif numero_3 > numero_2 and numero_1:
    print(f'{numero_3}Es mayor: ')
else: 
    print ('No es posble hacer comparación')
    
