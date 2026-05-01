ARCHIVO = "servicios.json"

def cargar():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except:
        return []

def guardar(servicios):
    with open(ARCHIVO, "w") as f:
        json.dump(servicios, f, indent=4)



def menu():
servicios = cargar()

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

def editar(servicios):
    nombre = input("Nombre del servicio a editar: ")

    for s in servicios:
        if s["nombre"] == nombre:
            print("\n✏️ Editando servicio")

    s["nombre"] = input("Nuevo nombre: ")
    s["precio"] = input("Nuevo precio: ")
    s["tipo_evento"] = input("Nuevo tipo: ")
    s["duracion"] = input("Nueva duración: ")

    guardar(servicios)
    print("¡Servicio actualizado!")
    return

    print("-Servicio no encontrado-")