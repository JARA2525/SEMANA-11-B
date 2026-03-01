import json
from MODELOS.producto import Producto

class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}

    # Añadir producto
    def agregar_producto(self, producto):
        self.productos[producto.get_id()] = producto

    # Eliminar producto
    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    # Actualizar producto
    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    # Buscar por nombre
    def buscar_producto(self, nombre):
        encontrados = []
        for producto in self.productos.values():
            if nombre.lower() in producto.get_nombre().lower():
                encontrados.append(producto)
        return encontrados

    # Mostrar todos
    def mostrar_productos(self):
        for producto in self.productos.values():
            print(producto.to_dict())

    # Guardar en archivo JSON
    def guardar_archivo(self, ruta):
        with open(ruta, "w") as archivo:
            json.dump(
                {id: prod.to_dict() for id, prod in self.productos.items()},
                archivo,
                indent=4
            )

    # Cargar desde archivo JSON
    def cargar_archivo(self, ruta):
        try:
            with open(ruta, "r") as archivo:
                datos = json.load(archivo)
                for id, info in datos.items():
                    producto = Producto(
                        info["id"],
                        info["nombre"],
                        info["cantidad"],
                        info["precio"]
                    )
                    self.productos[id] = producto
        except FileNotFoundError:
            print("Archivo no encontrado, se creará uno nuevo.")