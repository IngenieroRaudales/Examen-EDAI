'''
	Programa que crea una base de datos con personas muestra.
	Y con los datos ingresados al momento de que se crea devuelve
	el indicador de semáforo COVID que correspone al número de contagios.
'''

#Solicitar librerias para tener pantalla limpia. :)
import os
os.system("cls")

#Declarar las variables y listas a ocupar.
op ='0'
datos = []
datos2 = []
datos3 = []
while (op != '2'):
	print("\n1) Llenar\n2) Salir\n")             	#Menú
	op = input("Elige una opción: ")
	if op == '1':
		ed = int(input ("Edad: "))					#Ingreso de la edad
		ind = float(input ("Indicador: "))			#Ingreso del indicador
		if ind < 0.8:								
			cov = "Negativo"
		else:										#Indicador de caso positivo/negativo
			cov = "Positivo"
		reg = str(ed) + ',' + str(cov) + '\n'
		reg2 = ed
		reg3 = cov									#Operaciones de las listas
		datos.append(reg)
		datos2.append(reg2)
		datos3.append(reg3)
	elif op == '2':
		print("\n\nContinuemos...\n\n")
	else:
		print("Opción no válida ):")

#Cambiar el nombre del .csv cada que se quiera hacer una base de datos nueva
alm = open("bad.csv","a")
alm.writelines(datos)											#Crear base de datos y guardar
alm.close()

alm = open("bad.csv","r")							
contenido = alm.read()											#Mostrar base de datos
alm.close
print("\n\nALMACENAMIENTO DE MUESTRAS: \n")
print(contenido)

prom = sum(datos2) / len(datos3)
print("El promedio de edad de las personas muestra es: \n")		#Promedio de edad de personas
print(prom)

sem = datos3.count("Positivo")
print("\nEl número de casos positivos a COVID es: \n")			#Conteo de casos positivos
print(sem)

print("\nDado el número de contagios el semáforo COVID es:\n")
if sem == 0:
	print("Verde")
elif 1 <= sem <= 30:
	print("Amarillo")											#Indicador de color de semáforo
elif 31 <= sem <= 70:
	print("Naranja")
elif 71 <= sem <= 100:
	print("Rojo")


#Mensaje de despedida
print("\n\n\n\n\n\t\t\t\t\t\tGracias por usar el indicador de semáforo :)")
