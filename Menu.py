import json
import Funciones


while True:
    print("---------------------------------------")
    print("\n ---SISTEMA FOTOGRÁFICO---")
    print("1. Ver catálogo de servicios(Paquetes)")
    print("2. Registrar nuevo servicio")
    print("3. Editar Paquete")
    print("4. Eliminar servicio")
    print("5. Salir")
    print("---------------------------------------")

    op = input("Seleccione una opción: ")

    if op == "1":
        Funciones.mostrar(servicios)
    elif op == "2":
        Funciones.nagregar(servicios)
    elif op == "3":
        Funciones.editar(servicios)
    elif op == "4":
        Funciones.eliminar(servicios)
    elif op == "5":
        print("...Estas Saliendo del sistema...")
    break
else:
    print("Opción inválida")

menu()
