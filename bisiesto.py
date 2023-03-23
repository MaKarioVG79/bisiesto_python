
a = input("Intruduce el año ")


if int(a) % 4 != 0: 
	print("No es bisiesto")
if int(a) % 4 == 0 and int(a) % 100 != 0: 
	print("Es bisiesto")
if int(a) % 4 == 0 and int(a) % 100 == 0 and int(a) % 400 != 0:
	print("No es bisiesto")
if int(a) % 4 == 0 and int(a) % 100 == 0 and int(a) % 400 == 0: 
	print("Es bisiesto")
	
