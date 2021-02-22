import sys

def main():
    try:
        elementos = sys.argv[1]
        lista = []
        a = 1
        while a <= int(elementos):
            valor = input('Ingrese registro {}: '.format(a))
            lista.append(valor)
            a = a+1
        salida = ''
        for a in lista:
            salida = salida + str(a)
        print(salida)
    except IndexError as e:
        print('Error: Debe ingresar un parámetro')
    except ValueError as e:
        print('Error: Debe ingresar un entero')
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()