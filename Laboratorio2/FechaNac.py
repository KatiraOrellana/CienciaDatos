import sys
from datetime import datetime
from datetime import date

def main():
    try:
        dia = input('Ingresa tu día de nacimiento: ')
        dia = int(dia)
        mes = input('Ingresa tu mes de nacimiento: ')
        mes = int(mes)
        if  mes < 1 or mes > 12:
            e = 'Error: el mes debe estar entre 1 y 12'
            raise Exception('Error:  Valor incorrecto')
        año = input('Ingresa tu año de nacimiento: ')
        año = int(año)
        hoyaño = datetime.today().year
        hoymes = datetime.today().month
        hoydia = datetime.today().day
        edad = hoyaño - año
        if mes > hoymes:
            edad = edad - 1
            edadmes = 12 - (mes - hoymes)
        else:
            edadmes = hoymes - mes
            print(str(edadmes))
        if hoydia > dia:
            edaddia = hoydia - dia
        else:
            edadmes = edadmes -1
            edaddia = 30 - (dia - hoydia)
        print('Su edad es:{} años {} meses {} días'.format(edad,edadmes,edaddia))
    except ValueError as f:
        print('Error: Debe ingresar un entero')
    except Exception as f:
        print(e)
    
if __name__ == '__main__':
    main()