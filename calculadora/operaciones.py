def suma(a, b):
    while b > 0:
        a = a + 1
        b = b - 1
    while b < 0:
        a = a - 1
        b = b + 1
    return a

def resta(a, b):
    while b > 0:
        a = a - 1
        b = b - 1
    while b < 0:
        a = a + 1
        b = b + 1
    return a

def multiplicacion(a, b):
    resultado = 0
    negativo = False
    if b < 0:
        b = resta(0, b)
        negativo = True
    while b > 0:
        resultado = suma(resultado, a)
        b = resta(b, 1)
    return resta(0, resultado) if negativo else resultado

def division(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    negativo = (a < 0) != (b < 0)
    a = resta(0, a) if a < 0 else a
    b = resta(0, b) if b < 0 else b
    resultado = 0
    while a >= b:
        a = resta(a, b)
        resultado = suma(resultado, 1)
    return resta(0, resultado) if negativo else resultado

def factorial(n):
    if n < 0:
        return "Error: No se puede calcular el factorial de un número negativo."
    if n == 0 or n == 1:
        return 1
    resultado = 1
    contador = n
    while contador > 1:
        resultado = multiplicacion(resultado, contador)
        contador = resta(contador, 1)
    return resultado

def raiz_cuadrada(n):
    if n < 0:
        return "Error: No se puede calcular la raíz cuadrada de un número negativo."
    resultado = 0
    contador = 1
    while n >= contador:
        n = resta(n, contador)
        contador = suma(contador, 2)
        resultado = suma(resultado, 1)
    return resultado

def potencia(a, b):
    if b < 0:
        return "Error: No se soportan exponentes negativos."
    resultado = 1
    while b > 0:
        resultado = multiplicacion(resultado, a)
        b = resta(b, 1)
    return resultado
