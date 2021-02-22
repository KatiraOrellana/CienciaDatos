import sys

def main():
    try:
        Nolistas = sys.argv[1]
        Nolistas = int(Nolistas)
        print(Nolistas)
        glista = []
        for a in range(Nolistas):
            glista.append([])
            b = 1
            valor = input('Ingrese elemento {} de la lista {}, si desea terminar la lista, ingrese 0: '.format(b,a))
            print(valor)
            while int(valor) != 0:
                glista[a].append(valor)
                print(glista)
                b = b+1
                valor = input('Ingrese elemento {} de la lista {}, si desea terminar la lista, ingrese 0: '.format(b,a))
        print(len(glista))
        promedio = []
        for x in range(Nolistas):
            print('Esta es la lista ',glista[x])
            suma = 0
            for y in range(2):
                suma = suma + glista[x][y]
                print(str(suma))
    except IndexError as e:
        print(e)
    except ValueError as e:
        print('Error: Debe ingresar un entero')
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()