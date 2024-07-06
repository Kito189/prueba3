def registrar_prestamo(prestamos):
    # Solicitar al usuario que ingrese los datos
    nombre = input("Ingrese nombre y apellido del usuario: ")
    id_libro = input("Ingrese ID del libro: ")
    fecha_prestamo = input("Ingrese fecha de préstamo (dd-mm-yyyy): ")
    fecha_devolucion = input("Ingrese fecha de devolución (dd-mm-yyyy): ")
    
    # Validar datos ingresados
    if not nombre or not id_libro or not fecha_prestamo or not fecha_devolucion:
        print("Error: Todos los campos son obligatorios")
        return  # Salir de la función si algún campo está vacío
    
    # Crear un diccionario de préstamo
    prestamo = {
        "nombre": nombre,
        "id_libro": id_libro,
        "fecha_prestamo": fecha_prestamo,
        "fecha_devolucion": fecha_devolucion
    }
    
    # Agregar el diccionario a la lista de préstamos
    prestamos.append(prestamo)
    print("Préstamo registrado con éxito")

def listar_prestamos(prestamos):
    # Ver si hay préstamos registrados
    if not prestamos:
        print("No hay préstamos registrados")
    else:
        for prestamo in prestamos:
            print(f"Préstamo: {prestamo['nombre']}, ID Libro: {prestamo['id_libro']}, "
                  f"Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion']}")

def imprimir_recibo(prestamos):
    if not prestamos:
        print("No hay préstamos registrados")
    else:
        print("Seleccione un préstamo para imprimir recibo:")
        i = 1
        # Mostrar una lista de todos los préstamos
        for prestamo in prestamos:
            print(f"{i}. {prestamo['nombre']}, ID Libro: {prestamo['id_libro']}")
            i += 1
        
        # Solicitar al usuario que ingrese el número del préstamo a imprimir
        seleccion = int(input("Ingrese el número del préstamo: "))
        
        if seleccion > 0 and seleccion <= len(prestamos):
            # Obtener el préstamo seleccionado
            prestamo_seleccionado = prestamos[seleccion - 1]
            
            # Imprimir el recibo en la consola
            print("Recibo de préstamo:")
            print(f"Nombre: {prestamo_seleccionado['nombre']}")
            print(f"ID Libro: {prestamo_seleccionado['id_libro']}")
            print(f"Fecha de préstamo: {prestamo_seleccionado['fecha_prestamo']}")
            print(f"Fecha de devolución: {prestamo_seleccionado['fecha_devolucion']}")
            print("Recibo de préstamo generado con éxito")
            
            # Crear un archivo de texto con el recibo
            nombre_archivo = f"recibo_{prestamo_seleccionado['nombre'].replace(' ', '_')}.txt"
            with open(nombre_archivo, 'w') as archivo:
                archivo.write("Recibo de préstamo:\n")
                archivo.write(f"Nombre: {prestamo_seleccionado['nombre']}\n")
                archivo.write(f"ID Libro: {prestamo_seleccionado['id_libro']}\n")
                archivo.write(f"Fecha de préstamo: {prestamo_seleccionado['fecha_prestamo']}\n")
                archivo.write(f"Fecha de devolución: {prestamo_seleccionado['fecha_devolucion']}\n")
            print(f"Recibo guardado en {nombre_archivo}")
            
        else:
            print("Error: Selección inválida")


def Salir():
    print("Saliendo del programa. ¡Hasta luego!")

