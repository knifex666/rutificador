import requests
from os import system
from htmltb_to_json import api1_conversor, api2_conversor, normalizar

repetir = True
maxResult = 150



while repetir == True:

    x = 0
    comuna = False
    

    print('---------------- Rutificador (RMax:%d) ------------------' % maxResult)
    print(' ')

    nombre = input('Ingrese el nombre: ')
    print(' ')

    while x == 0:
        validador = normalizar(input('¿Desea filtrar por comuna? (S/N): '))

        if validador == 'S':
            x = 1
            comuna = True
        elif validador == 'N':
            break
        else:
            continue

    if not comuna:
        
        print(' ')
        print('Cargando...')
        print(' ')

        #Intenta con el primer api
        try:
            datos = api1_conversor(nombre)

            for i in range(0,len(datos)):

                print('Nombre: %s'%datos[i]['Nombre'])
                print('RUT: %s'%datos[i]['RUT'])
                print('Género: %s'%datos[i]['Sexo'])
                print('Dirección: %s'% normalizar(datos[i]['Dirección']))
                print('Comuna/Ciudad: %s'% normalizar(datos[i]['Ciudad/Comuna']))
                print('----------------------------------')
                print('----------------------------------')

            print(' ')
            print('Resultados: %d/%d (API 1)' % (len(datos),maxResult))
            print(' ')

            while x == 0:
                validador = normalizar(input('¿Desea consultar otro nombre? (S/N)'))

                if validador == 'S':
                    x = 1
                elif validador == 'N':
                    x = 1
                    repetir = False
                else:
                    continue
            system('clear')

        #Si no funciona con el primero intenta con este
        except:
            datos = api2_conversor(nombre)

            for i in range(0,len(datos)):

                print('Nombre: %s'%datos[i]['Nombre'])
                print('RUT: %s'%datos[i]['RUT'])
                print('Género: %s'%datos[i]['Género'])
                print('Dirección: %s'% normalizar(datos[i]['Dirección']))
                print('Comuna/Ciudad: %s'%normalizar(datos[i]['Comuna']))
                print('----------------------------------')
                print('----------------------------------')

            print(' ')
            print('Resultados: %d/%d (API 2)' % (len(datos),maxResult))
            print(' ')

            while x == 0:
                validador = normalizar(input('¿Desea consultar otro nombre? (S/N)'))

                if validador == 'S':
                    x = 1
                elif validador == 'N':
                    x = 1
                    repetir = False
                else:
                    continue
            system('clear')

    else:
        
        print(' ')
        print('(Usar 2 nombres o 2 apellidos para mejores resultados)')
        print(' ')
        x = 0

        comuna = normalizar(input('Ingrese la comuna: '))
        print(' ')
        print('Cargando...')
        print(' ')
        #Intenta con el primer api
        try:
            datos = api1_conversor(nombre)
            cantidad = 0

            for i in range(0,len(datos)):

                if normalizar(datos[i]['Ciudad/Comuna']).find(comuna) > -1:
                    cantidad += 1
                    print('Nombre: %s'%datos[i]['Nombre'])
                    print('RUT: %s'%datos[i]['RUT'])
                    print('Género: %s'%datos[i]['Sexo'])
                    print('Dirección: %s'% normalizar(datos[i]['Dirección']))
                    print('Comuna/Ciudad: %s'% normalizar(datos[i]['Ciudad/Comuna']))
                    print('----------------------------------')
                    print('----------------------------------')

            print(' ')
            print('Resultados: %d/%d (API 1)' % (cantidad,maxResult))
            print(' ')

            while x == 0:
                validador = normalizar(input('¿Desea consultar otro nombre? (S/N)'))

                if validador == 'S':
                    x = 1
                elif validador == 'N':
                    x = 1
                    repetir = False
                else:
                    continue
            system('clear')

        #Si no funciona con el primero intenta con este
        except:
            datos = api2_conversor(nombre)
            cantidad = 0

            for i in range(0,len(datos)):

                if normalizar(datos[i]['Ciudad/Comuna']).find(comuna) > -1:
                    cantidad += 1
                    print('Nombre: %s'%datos[i]['Nombre'])
                    print('RUT: %s'%datos[i]['RUT'])
                    print('Género: %s'%datos[i]['Género'])
                    print('Dirección: %s'% normalizar(datos[i]['Dirección']))
                    print('Comuna/Ciudad: %s'% normalizar(datos[i]['Comuna']))
                    print('----------------------------------')
                    print('----------------------------------')

            print(' ')
            print('Resultados: %d/%d (API 2)' % (cantidad,maxResult))
            print(' ')

            while x == 0:
                validador = normalizar(input('¿Desea consultar otro nombre? (S/N)'))

                if validador == 'S':
                    x = 1
                elif validador == 'N':
                    x = 1
                    repetir = False
                else:
                    continue
            system('clear')




