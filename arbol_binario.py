from nodo import Nodo

class ArbolBinarioBusqueda:
    def __init__(self):
        #inicializa el arbol binario de busueda sin una raiz
        self.raiz = None

    #inserta un producto en el arbol, si la raiz esta vacia, crea un nodo raiz
    def insertar(self, producto):
        if self.raiz is None:
            self.raiz = Nodo(producto)
        else:
            self._insertar_recursivo(self.raiz, producto)

    def _insertar_recursivo(self, nodo_actual, producto):
        #insercion recursiva comparando nombres de productos
        if producto.nombre < nodo_actual.producto.nombre:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(producto)
            else:
                self._insertar_recursivo(nodo_actual.izquierda, producto)
        elif producto.nombre > nodo_actual.producto.nombre:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(producto)
            else:
                self._insertar_recursivo(nodo_actual.derecha, producto)
        else:
            nodo_actual.producto = producto #si el producto ya existe, actualiza su valor

    #busca un producto por nombre 
    def buscar(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre)

    #compara los nombres parea ver si ya existe
    def _buscar_recursivo(self, nodo_actual, nombre):
        if nodo_actual is None:
            return None
        if nombre == nodo_actual.producto.nombre:
            return nodo_actual.producto
        elif nombre < nodo_actual.producto.nombre:
            return self._buscar_recursivo(nodo_actual.izquierda, nombre)
        else:
            return self._buscar_recursivo(nodo_actual.derecha, nombre)

    #actualiza los datos de un producto si existe en el arbol
    def actualizar(self, nombre, nuevo_producto):
        nodo = self.buscar(nombre)
        if nodo is not None:
            nodo.precio = nuevo_producto.precio
            nodo.categoria = nuevo_producto.categoria
            nodo.talla = nuevo_producto.talla
            nodo.color = nuevo_producto.color
            nodo.stock = nuevo_producto.stock
            return True
        return False

    def eliminar(self, nombre):
        #elimina un producto por nombre del arbol
        self.raiz = self._eliminar_recursivo(self.raiz, nombre)

    def _eliminar_recursivo(self, nodo_actual, nombre):
        #elimina recursivamente un nodo con el porducto indicado
        if nodo_actual is None:
            return nodo_actual

        if nombre < nodo_actual.producto.nombre:
            nodo_actual.izquierda = self._eliminar_recursivo(nodo_actual.izquierda, nombre)
        elif nombre > nodo_actual.producto.nombre:
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, nombre)
        else:
            if nodo_actual.izquierda is None:
                return nodo_actual.derecha
            elif nodo_actual.derecha is None:
                return nodo_actual.izquierda

            #encuentra el sucesor y reemplaza el nodo actual
            sucesor = self._obtener_min(nodo_actual.derecha)
            nodo_actual.producto = sucesor.producto
            nodo_actual.derecha = self._eliminar_recursivo(nodo_actual.derecha, sucesor.producto.nombre)
        
        return nodo_actual

    def _obtener_min(self, nodo):
        #encuentra el nodo con el valor minimo en la sub-rama
        actual = nodo
        while actual.izquierda is not None:
            actual = actual.izquierda
        return actual
