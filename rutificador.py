import requests
from os import system
from htmltb_to_json import api1_conversor, api2_conversor

repetir = 1

while repetir == 1:

    print('---------------- Rutificador ------------------')
    print(' ')

    nombre = input('Ingrese el nombre: ')
    print(' ')
    
    #Intenta con el primer api
    try:
        datos = api1_conversor(nombre)

        for i in range(0,len(datos)):

            print('Nombre: %s'%datos[i]['Nombre'])
            print('RUT: %s'%datos[i]['RUT'])
            print('Género: %s'%datos[i]['Sexo'])
            print('Dirección: %s'%datos[i]['Dirección'])
            print('Comuna/Ciudad: %s'%datos[i]['Ciudad/Comuna'])
            print('----------------------------------')
            print('----------------------------------')

        print(' ')
        print('Resultados: %d' % len(datos))
        print(' ')
        x = 0
        while x == 0:
            validador = input('¿Desea consultar otro nombre? (S/N) ')
            print(validador)
            if validador == 's' or validador == 'S':
                x = 1
            elif validador == 'n' or validador == 'N':
                x = 1
                repetir = 0
            else:
                continue
        system('clear')

    #Sino funciona con el primero intenta con este
    except:
        datos = api2_conversor(nombre)

        for i in range(0,len(datos)):

            print('Nombre: %s'%datos[i]['Nombre'])
            print('RUT: %s'%datos[i]['RUT'])
            print('Género: %s'%datos[i]['Género'])
            print('Dirección: %s'%datos[i]['Dirección'])
            print('Comuna/Ciudad: %s'%datos[i]['Comuna'])
            print('----------------------------------')
            print('----------------------------------')

        print(' ')
        print('Resultados: %d' % len(datos))
        print(' ')

        x = 0
        while x == 0:
            validador = input('¿Desea consultar otro nombre? (S/N)')

            if validador == 's' or validador == 'S':
                x = 1
            elif validador == 'n' or validador == 'N':
                x = 1
                repetir = 0
            else:
                continue
        system('clear')
    

