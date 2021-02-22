import sys

def main():
    try:
        listas = sys.argv[1]
        print(listas)
        lista = []
        a = 1
        while a <= int(listas):
            lista.append([])
            b = 1
            while b != 0
                valor = input('Ingrese elemento de la lista {}, si desea terminar la lista, ingrese 0: '.format(a))
                lista[a].append(valor)
            a = a+1
        print(lista)
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