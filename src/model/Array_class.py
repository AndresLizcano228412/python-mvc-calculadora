class Array:
    def vector(self, lista):
        suma = sum(lista)
        return lista, suma

    def matriz(self, filas: int, columnas: int, datos: list):
        matriz = []
        indice = 0
        for i in range(filas):
            fila = []
            for j in range(columnas):
                fila.append(datos[indice])
                indice += 1
            matriz.append(fila)
        return matriz