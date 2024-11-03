# **Proyecto de Gestión de Inventario - Tienda de Ropa** 

Este proyecto es una aplicación que facilita la **gestión de inventario** para una tienda de ropa, organizada mediante un árbol binario de búsqueda que permite un acceso rápido a los productos. La interfaz gráfica hace que sea fácil de usar y ofrece funciones para **añadir, buscar y visualizar productos**.

## **Estructura del Proyecto**

- **`arbol_binario.py`**: Implementa el árbol binario de búsqueda (`ArbolBinarioBusqueda`), con funciones de inserción y búsqueda de productos.
- **`nodo.py`**: Define la estructura de cada nodo del árbol.
- **`producto.py`**: Contiene la definición de un producto, con atributos como nombre, precio, categoría, talla, color y stock.
- **`interfaz.py`**: Configura la interfaz gráfica de usuario con `tkinter` para gestionar el inventario.
- **`inventario.csv`**: Archivo CSV con datos iniciales del inventario.

## **Requisitos**

- **Python 3.x** (Asegúrate de que esté instalado en tu sistema).
- **`tkinter`** (generalmente viene incluido con Python).

## **Instrucciones para Ejecutar la Aplicación**

Abre una terminal en la carpeta donde has guardado los archivosn y ejecuta el programa interfaz.
Una vez que el programa se ejecuta, se abrirá una ventana de interfaz gráfica con las siguientes funcionalidades:
Visualización: Tabla con todos los productos en el inventario.
Búsqueda: Buscar productos por nombre.
Añadir productos: Insertar un nuevo producto con sus detalles.
Actualización de productos: Modificar datos como el stock o precio de un producto.
