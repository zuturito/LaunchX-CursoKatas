def main():
    try:
        configuration = open('config.txt')
    except OSError as err:
        if err.errno == 2:
            print("¡Error! No se encuentra el archivo solicitado, revisa el directorio de origen")
        elif err.errno == 13:
            print("Se ha encontrado el archivo config.txt pero es un directorio, no es posible leerlo")

if __name__ == '__main__':
    main()