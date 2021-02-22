import sys

def main():
    try:
        elementos = sys.argv[1]
        lista = []
        print(elementos)
        a = 1
        while a <= elementos:
            lista = lista.append(input('Ingrese registro {} '.format.lista))
            a = a+1
    except IndexError as e:
        print('Error: Debe ingresar un parámetro')
    except ValueError as e:
        print('Error: Debe ingresar un entero')
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()