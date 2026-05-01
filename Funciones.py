def mostrar(servicios):
    if not servicios:
        print("No hay servicios registrados")
        return

    print("\n CATÁLOGO FOTOGRÁFICO")
    for s in servicios:
        print(f"\nPaquete: {s['nombre']}")
        print(f"Precio: {s['precio']}")
        print(f"Tipo: {s['tipo_evento']}")
        print(f"Duración: {s['duracion']} horas")

def agregar(servicios):
    print("\n NUEVO SERVICIO FOTOGRÁFICO")

    nombre = input("Nombre del paquete: ")
    precio = input("Precio: ")
    tipo = input("Tipo de evento: ")
    duracion = input("Duración (horas): ")

    servicio = {
        "nombre": nombre,
        "precio": precio,
        "tipo_evento": tipo,
        "duracion": duracion
    }

    servicios.append(servicio)
    guardar(servicios)
    print("¡Servicio agregado!")