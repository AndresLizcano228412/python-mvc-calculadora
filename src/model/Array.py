
    def vector(self, lista):
        lista = []
        suma = 0
        i = 1
        for i in range(6):
            numero = int(input("Ingrese un número: "))
            lista.append(numero)
            suma += numero
            i += 1
            return lista, suma