def menu():
servicios = cargar()

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
        mostrar(servicios)
    elif op == "2":
        agregar(servicios)
    elif op == "3":
        editar(servicios)
    elif op == "4":
        eliminar(servicios)
    elif op == "5":
        print("...Estas Saliendo del sistema...")
    break
else:
print("Opción inválida")

menu()
