print('Practica excepciones: inicio')

while True:
    try:
        num = int(input('Entre Numerador: '))
        denom = int(input('Entre denominador: '))
        division = num / denom
        print('Division = %6.2f' % division)
        print('Adiós')
    except ValueError:
        print('Error: Debes ingresar valores enteros.')
    except ZeroDivisionError:
        print('Error: No se puede dividir entre cero.')