import sys

def main():
    try:
        entrada = sys.argv[1]
        entrada = int(entrada)
        segundos = int(entrada) % 60
        operador = int(entrada) // 60
        minutos = operador % 60
        hora = operador // 60
        if hora > 24:
            raise Exception("Error: El valor debe ser menor a 90000")
        print("Horas: {} Minutos: {} Segundos: {} ".format(hora,minutos,segundos))
    except IndexError as e:
        print('Error: Debe ingresar un parámetro')
    except ValueError as e:
        print('Error: Debe ingresar un entero')
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()