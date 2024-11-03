class Producto:
    def __init__(self, nombre, precio, categoria, talla, color, stock):
        #clase para almacenar la informacion de un producto
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.talla = talla
        self.color = color
        self.stock = stock

    def __str__(self):
        #representacion del producto en string para visualizarlo en la interfaz
        return f"{self.nombre} - {self.precio} - {self.categoria} - {self.talla} - {self.color} - {self.stock}"
