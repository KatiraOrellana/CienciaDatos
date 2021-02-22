import sys

def main():
    try:
       elementos = sys.argv[1]
       print(str(elementos))
       for x 
    except IndexError as e:
        print('Error: Debe ingresar un parámetro')
    except ValueError as e:
        print('Error: Debe ingresar un entero')
    except Exception as e:
        print(e)
    
if __name__ == '__main__':
    main()