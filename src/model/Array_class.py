class Array:
    def vector(self, valor):
        lista = []
        self.valor = None
        i = 1
        for i in range(6):
            lista.append(self.valor)
            i += 1
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

    def suma_filas(self, matriz: list):
        suma_filas = []
        for fila in matriz:
            total = sum(fila)
            suma_filas.append(total)
        return suma_filas

    def suma_columnas(self, matriz: list):
        filas = len(matriz)
        columnas = len(matriz[0])
        suma_columnas = []
        for j in range(columnas):
            total = 0
            for i in range(filas):
                total += matriz[i][j]
            suma_columnas.append(total)
        return suma_columnas
