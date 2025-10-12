# src/model/calculator.py
from __future__ import annotations


class DivisionPorCeroError(Exception):
    """Error al intentar dividir entre cero."""


class ExponenteInvalidoError(Exception):
    """Error cuando el exponente no es un entero válido (esperado >= 0)."""


class Calculator:
    """Implementa operaciones aritméticas enteras bajo restricciones del enunciado.

    Restricciones en este modelo:
    - No usar: pow, math.*, divmod, %, **, //, abs, round (ni equivalentes).
    - Se permiten: asignación, +, -, comparaciones, bucles y funciones propias.

    Convenciones:
    - División: cociente entero truncado hacia 0.
    - Módulo: resto con el mismo signo del dividendo.
    - Potenciación: exponente entero >= 0; 0^0 = 1 por convenio.
    """

    # ========= Helpers internos permitidos (solo +, -, comparaciones y bucles) =========

    def _valor_absoluto(self, n: int) -> int:
        """Retorna |n| sin usar built-ins."""
        if n < 0:
            return -n
        return n

    def _mismo_signo(self, a: int, b: int) -> bool:
        return (a >= 0 and b >= 0) or (a < 0 and b < 0)

    def _es_par(self, n: int) -> bool:
        """True si n es par, usando restas de 2."""
        m = n
        # Suponemos n >= 0 donde se use (exponente)
        while m >= 2:
            m = m - 2
        return m == 0

    def _mitad(self, n: int) -> int:
        """Retorna floor(n/2) por restas de 2 (n >= 0)."""
        m = n
        c = 0
        while m >= 2:
            m = m - 2
            c = c + 1
        return c

    # ============================ Operaciones públicas ============================

    def suma(self, a: int, b: int) -> int:
        return a + b

    def resta(self, a: int, b: int) -> int:
        return a - b

    def multiplicacion(self, a: int, b: int) -> int:
        """Multiplicación por sumas repetidas, minimizando iteraciones."""
        if a == 0 or b == 0:
            return 0

        sign = 1
        if not self._mismo_signo(a, b):
            sign = -1

        x = self._valor_absoluto(a)
        y = self._valor_absoluto(b)

        # Iterar por el menor para reducir pasos
        menor = x if x < y else y
        mayor = y if x < y else x

        acc = 0
        i = 0
        while i < menor:
            acc = acc + mayor
            i = i + 1

        if sign < 0:
            return -acc
        return acc

    def division(self, a: int, b: int) -> int:
        """Cociente entero truncado hacia 0 mediante restas por bloques.

        Lanza:
            DivisionPorCeroError: si b == 0.
        """
        if b == 0:
            raise DivisionPorCeroError("División por cero no definida.")

        if a == 0:
            return 0

        sign = 1
        if not self._mismo_signo(a, b):
            sign = -1

        n = self._valor_absoluto(a)
        d = self._valor_absoluto(b)

        # División por restas "aceleradas" (doblando el divisor)
        q = 0
        while n >= d:
            # Doblado exponencial
            temp = d
            mult = 1
            # Mientras reste al menos temp y además podamos doblar
            while (n - temp) >= 0 and (n - temp) >= temp:
                temp = temp + temp
                mult = mult + mult
            n = n - temp
            q = q + mult

        if sign < 0:
            return -q
        return q

    def modulo(self, a: int, b: int) -> int:
        """Resto con el mismo signo del dividendo, por restas.

        Lanza:
            DivisionPorCeroError: si b == 0.
        """
        if b == 0:
            raise DivisionPorCeroError("Módulo por cero no definido.")

        if a == 0:
            return 0

        sign_a = 1 if a >= 0 else -1
        n = self._valor_absoluto(a)
        d = self._valor_absoluto(b)

        # Usar el mismo esquema de división pero quedándonos con el sobrante n
        while n >= d:
            temp = d
            # Podemos reutilizar la lógica de doblado sin contar el múltiplo
            while (n - temp) >= 0 and (n - temp) >= temp:
                temp = temp + temp
            n = n - temp

        # n es el resto absoluto; aplicar signo del dividendo
        if sign_a < 0:
            return -n
        return n

    def factorial(self, numero: int) -> int:
        """Factorial por multiplicaciones repetidas (nnumero >= 0).

        Lanza:
            ExponenteInvalidoError: si numero < 0.
        """
        if numero < 0:
            raise ExponenteInvalidoError("Factorial no definido para n < 0.")
        if numero == 0:
            return 1

        acumulador = 1
        indice = 1
        while indice <= numero:
            acumulador = self.multiplicacion(acumulador, indice)
            indice = indice + 1
        return acumulador

    def potenciacion(self, a: int, b: int) -> int:
        """Exponenciación por cuadrados sin %, ** ni // (b >= 0).

        Lanza:
            ExponenteInvalidoError: si b < 0.
        """
        if b < 0:
            raise ExponenteInvalidoError("Exponente negativo no soportado.")
        # Casos base
        if b == 0:
            return 1
        if a == 0:
            return 0

        # Exponenciación rápida
        base = a
        exp = b
        res = 1
        while exp > 0:
            if not self._es_par(exp):
                res = self.multiplicacion(res, base)
            base = self.multiplicacion(base, base)
            exp = self._mitad(exp)
        return res

    def ex(self, x: float) -> float:
        """Calcula el valor de e^x usando la serie de Taylor."""
        termino = 1.0  # Primer término de la serie (x^0 / 0!)
        suma = termino
        n = 1

        while n < 100:  # Limitar a 100 términos para precisión
            termino = termino * x / n  # Calcular el siguiente término
            suma += termino
            n += 1

        return suma

    def seno(self, grados: float) -> float:
        """Calcula el seno de x (en radianes) usando la serie de Taylor."""
        import math
        x = grados * (math.pi / 180)  # Convertir grados a radianes
        termino = x  # Primer término de la serie (x^1 / 1!)
        suma = termino
        n = 1

        while n < 100:  # Limitar a 100 términos para precisión
            termino = -termino * x * x / ((2 * n) * (2 * n + 1))  # Calcular el siguiente término
            suma += termino
            n += 1

        return suma

    def coseno(self, grados: float) -> float:
        """Calcula el coseno de x (en radianes) usando la serie de Taylor."""
        import math
        x = grados * (math.pi / 180) 
        termino = 1.0  # Primer término de la serie (x^0 / 0!)
        suma = termino
        n = 1

        while n < 100:  # Limitar a 100 términos para precisión
            termino = -termino * x * x / ((2 * n - 1) * (2 * n))  # Calcular el siguiente término
            suma += termino
            n += 1

        return suma

    def arcotangente(self, x: float) -> float:
        """Calcula la arcotangente de x usando la serie de Taylor."""
        if x < -1 or x > 1:
            raise ValueError("El valor de x debe estar en el rango [-1, 1] para una convergencia adecuada.")

        termino = x  # Primer término de la serie (x^1 / 1)
        suma = termino
        n = 1

        while n < 100:  # Limitar a 100 términos para precisión
            termino = -termino * x * x * (2 * n - 1) / (2 * n + 1)  # Calcular el siguiente término
            suma += termino
            n += 1

        return suma

    def leibniz_pi(self, iteraciones: int = 10000000) -> float:
        """Calcula una aproximación de π usando la serie de Leibniz."""
        pi_aproximado = 0.0
        signo = 1.0
        for n in range(iteraciones):
            pi_aproximado += signo / (2 * n + 1)
            signo *= -1
        return 4 * pi_aproximado