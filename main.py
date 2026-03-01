from SERVICIOS.inventario import Inventario
from MODELOS.producto import Producto

def menu():
    inventario = Inventario()
    inventario.cargar_archivo("DATA/inventario.json")

    while True:
        print("\n===== SISTEMA DE INVENTARIO =====")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))

            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID a actualizar: ")
            cantidad = int(input("Nueva cantidad: "))
            precio = float(input("Nuevo precio: "))
            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            resultados = inventario.buscar_producto(nombre)
            for prod in resultados:
                print(prod.to_dict())

        elif opcion == "5":
            inventario.mostrar_productos()

        elif opcion == "6":
            inventario.guardar_archivo("DATA/inventario.json")
            print("Inventario guardado. Saliendo...")
            break

        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()