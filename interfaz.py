import tkinter as tk
from tkinter import ttk, messagebox
from arbol_binario import ArbolBinarioBusqueda
from producto import Producto
import csv

class Interfaz:
    def __init__(self, arbol):
        #inicializa la interfaz grafica y el arbol binario de busqueda
        self.arbol = arbol
        self.ventana = tk.Tk()
        self.ventana.title("Gestión de Inventario - Tienda de Ropa")
        self.ventana.geometry("500x400")

        #estilo para la grafica
        style = ttk.Style()
        style.theme_use('clam')  
        style.configure("TButton", font=("Helvetica", 10), padding=5)
        
        self.crear_widgets()
        self.cargar_productos_csv()

    def crear_widgets(self):
        #tabla para mostrar productos
        self.tabla_productos = ttk.Treeview(self.ventana, columns=("Nombre", "Precio", "Categoría", "Talla", "Color", "Stock"), show="headings", height=8)
        for col in self.tabla_productos["columns"]:
            self.tabla_productos.heading(col, text=col)
        self.tabla_productos.pack(pady=10, padx=10)

        #frame para botones en una fila
        frame_botones = ttk.Frame(self.ventana)
        frame_botones.pack(pady=5)

        #botones de operaciones con margen compacto
        boton_agregar = ttk.Button(frame_botones, text="Agregar Producto", command=self.agregar_producto)
        boton_buscar = ttk.Button(frame_botones, text="Buscar", command=self.buscar_producto)
        boton_actualizar = ttk.Button(frame_botones, text="Actualizar", command=self.actualizar_producto)
        boton_eliminar = ttk.Button(frame_botones, text="Eliminar", command=self.eliminar_producto)
        
        #organiza los botones 
        boton_agregar.grid(row=0, column=0, padx=5)
        boton_buscar.grid(row=0, column=1, padx=5)
        boton_actualizar.grid(row=0, column=2, padx=5)
        boton_eliminar.grid(row=0, column=3, padx=5)

    def agregar_producto(self):
        #añade un nuevo producto al arbol, la tabla y el archivo csv
        nuevo_producto = Producto("Camiseta", 19.99, "Ropa", "M", "Rojo", 10)
        self.arbol.insertar(nuevo_producto)
        self.tabla_productos.insert("", "end", values=(nuevo_producto.nombre, nuevo_producto.precio, nuevo_producto.categoria, nuevo_producto.talla, nuevo_producto.color, nuevo_producto.stock))
        self.guardar_producto_csv(nuevo_producto)

    def buscar_producto(self):
        #busca un producto en el arbol y muestra el resultado
        nombre = "Camiseta"
        producto = self.arbol.buscar(nombre)
        if producto:
            messagebox.showinfo("Buscar Producto", f"Producto encontrado: {producto}")
        else:
            messagebox.showwarning("Buscar Producto", "Producto no encontrado")

    def actualizar_producto(self):
        #actualiza un producto existente en el arbol y en la tabla
        nombre = "Camiseta"
        nuevo_producto = Producto("Camiseta", 25.99, "Ropa", "M", "Azul", 8)
        if self.arbol.actualizar(nombre, nuevo_producto):
            messagebox.showinfo("Actualizar Producto", "Producto actualizado")
            self.actualizar_tabla(nombre, nuevo_producto)
        else:
            messagebox.showwarning("Actualizar Producto", "Producto no encontrado para actualizar")

    def eliminar_producto(self):
        #elimina un porducto del arbol y de la tabla
        nombre = "Camiseta"
        self.arbol.eliminar(nombre)
        messagebox.showinfo("Eliminar Producto", "Producto eliminado")
        self.eliminar_de_tabla(nombre)

    def actualizar_tabla(self, nombre, producto):
        #actualiza visualmente en la tabla
        for item in self.tabla_productos.get_children():
            if self.tabla_productos.item(item, 'values')[0] == nombre:
                self.tabla_productos.item(item, values=(producto.nombre, producto.precio, producto.categoria, producto.talla, producto.color, producto.stock))
                break

    def eliminar_de_tabla(self, nombre):
        #elimina visualmente de la tabla
        for item in self.tabla_productos.get_children():
            if self.tabla_productos.item(item, 'values')[0] == nombre:
                self.tabla_productos.delete(item)
                break

    def guardar_producto_csv(self, producto):
        #lo guarda en el archivo csv
        with open("inventario.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([producto.nombre, producto.precio, producto.categoria, producto.talla, producto.color, producto.stock])

    def cargar_productos_csv(self):
        #carga productos del csv al arbol y a la tabla
        try:
            with open("inventario.csv", mode="r") as file:
                reader = csv.reader(file)
                for row in reader:
                    producto = Producto(row[0], float(row[1]), row[2], row[3], row[4], int(row[5]))
                    self.arbol.insertar(producto)
                    self.tabla_productos.insert("", "end", values=(producto.nombre, producto.precio, producto.categoria, producto.talla, producto.color, producto.stock))
        except FileNotFoundError:
            print("No se encontró el archivo de inventario. Se creará uno nuevo al guardar productos.")

    def iniciar(self):
        #inicia el bucle principal de la interfaz grafica
        self.ventana.mainloop()

if __name__ == "__main__":
    arbol = ArbolBinarioBusqueda()
    app = Interfaz(arbol)
    app.iniciar()
