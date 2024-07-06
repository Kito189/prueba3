from funciones  import registrar_prestamo, listar_prestamos, imprimir_recibo, Salir

#Lista vacia para tener los prestamos

prestamos = []

while True:
    #Mostrar el menu de opciones
    print("Menú:")
    print("1. Registrar préstamo")
    print("2. Listar todos los préstamos")
    print("3. Imprimir recibo de préstamo")
    print("4. Salir del programa")
    opcion = input("Ingrese una opción: ")
    #Ver la opcion ingresada por la persona
    if opcion == "1":
        registrar_prestamo(prestamos)
    elif opcion == "2":
        listar_prestamos(prestamos)
    elif opcion == "3":
        imprimir_recibo(prestamos)
    elif opcion == "4":
        Salir()
        break
    else:
        print("opcion no valida. intente de nuevo")#imprimir mensaje de error si no es valido lo elegido
