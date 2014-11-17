# -*- encoding: utf-8 -*-
import urllib2
import json
import requests
import os

def GET():
	JSON = urllib2.urlopen("http://localhost:8080/SD2/webresources/movies").read()
	return JSON

seguir = 's'
while seguir == 's' or seguir == 'S':
	os.system('clear')
	JSON = GET()
	decode = json.loads(JSON)
	print 'seleccione una opción: '
	for indice in range(0,len(decode)):
		print str(indice) + ' - ' + decode[indice]['nameMovie']
	opcion1 = raw_input('ingrese una opción: ')
	os.system('clear')
	while not opcion1.isdigit():		
		print '***debe ingresar un valor numérico!!!***'
		print 'seleccione una opción: '
		for indice in range(0,len(decode)):	
			print str(indice) + ' - ' + decode[indice]['nameMovie']
		opcion1 = raw_input('ingrese una opción: ')
	if opcion1.isdigit():
		op1 = int(opcion1)
		if op1 >= 0 and op1 <len(decode):
			print 'Título: '+decode[op1]['nameMovie'].encode('utf-8')
			print 'Año: '+str(decode[op1]['yearMovie'])
			print 'Descripción: '+decode[op1]['descriptionMovie'].encode('utf-8')

			print'\n\nque desea hacer?:'
			print '1 - volver'
			print '2 - crear otra'
			print '3 - modificar'
			print '4 - eliminar'
			print '5 - salir'

			opcion2 = raw_input('ingrese una opción: ')
			while not opcion2.isdigit():
				so.system('clear')
				print '***Debe ingresar un valor numérico!!!***'
				print 'Título: '+decode[op1]['nameMovie'].encode('utf-8')
				print 'Año: '+str(decode[op1]['yearMovie'])
				print 'Descripción: '+decode[op1]['descriptionMovie'].encode('utf-8')

				print'\n\nque desea hacer?:'
				print '1 - volver'
				print '2 - crear otra'
				print '3 - modificar'
				print '4 - eliminar'
				print '5 - salir'

				opcion2 = raw_input('ingrese una opción: ')
			if opcion2.isdigit():
				op2 = int(opcion2)
				if op2 >= 1 and op2 <= 5:
					if op2 == 1:
						raw_input('presione una tecla')
					if op2 == 2:
						os.system('clear')
						nombre = raw_input('ingrese el nombre de la nueva película: ')
						year = raw_input('ingrese el año de la nueva película: ')
						while not year.isdigit():
							print 'debe ingresar un valor numérico!!!'
							year = raw_input('ingrese el año de la nueva película: ')
						year = int(year)
						descripcion = raw_input('ingrese la descripción de la nueva película: ')
						data = {'idMovie':0 , 'nameMovie':nombre, 'yearMovie':year, 'descriptionMovie':descripcion}
						url = 'http://localhost:8080/SD2/webresources/movies'
						headers = {'content-type': 'application/json'}
						data = json.dumps(data)
						response = requests.post(url, data=data,headers=headers)
						raw_input('presione una tecla')
					if op2 == 3:
						os.system('clear')
						print 'nombre anterior: %s' % (decode[op1]['nameMovie'].encode('utf-8'))
						nombre = raw_input('nuevo nombre (dejar en blanco para mantener): ')
						if nombre == "":
							nombre = decode[op1]['nameMovie'].encode('utf-8')
						print 'año anterior: %d' % (decode[op1]['yearMovie'])
						year = raw_input('nuevo año (dejar en blanco para mantener): ')
						if year != "":
							while not year.isdigit():
								print 'el año debe ser numérico!!!'
								print 'año anterior: %d' % (decode[op1]['yearMovie'])
								year = raw_input('nuevo año (dejar en blanco para mantener): ')
						if year == "":
							year = decode[op1]['yearMovie']
						print 'descripcion anterior: %s' % (decode[op1]['descriptionMovie'].encode('utf-8'))
						descripcion = raw_input('nueva descripción (dejar en blanco para mantener): ')
						if descripcion == "":
							descripcion = decode[op1]['descriptionMovie'].encode('utf-8')

						data = {'idMovie':decode[op1]['idMovie'],'nameMovie':nombre,'yearMovie':year,'descriptionMovie':descripcion}
						data = json.dumps(data)
						url = 'http://localhost:8080/SD2/webresources/movies/'+str(decode[op1]['idMovie'])
						headers = {'content-type':'application/json'}
						response = requests.put(url,data=data,headers=headers)
						raw_input('presione una tecla')
					if op2 == 4:
						print 'seguro que desea eliminar la película: %s (s / n)' % (decode[op1]['nameMovie'].encode('utf-8'))
						op3 = raw_input('')
						while op3 != 's' and op3 != 'S' and op3 != 'n' and op3 != 'N':
							print 'se ha ingresado una opción inválida!!!'
							print 'seguro que desea eliminar la película: %s (s / n)' % (decode[op1]['nameMovie'].encode('utf-8'))
							op3 = raw_input('')
						if op3 == 's' or op3 == 'S':
							url = 'http://localhost:8080/SD2/webresources/movies/'+str(decode[op1]['idMovie'])
							headers = {'content-type':'application/json'}
							data = {}
							response = requests.delete(url,data=data,headers=headers)
							raw_input('presione una tecla')
					if op2 == 5:
						seguir = 'n'
						raw_input('presione una tecla')
						os.system('clear')
		else:
			print '***ha ingresado una opción inválida!!!***'
			raw_input('')

