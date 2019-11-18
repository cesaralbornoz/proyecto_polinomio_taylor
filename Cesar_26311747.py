#!/usr/bin/env python3
"""
Proyecto Polinomio de Taylor.

Cada participante debe completar su módulo y luego solicitar el Pull-Request.
"""
import math
def derivada(f, h = 0.01):
    """
    Retorna la función derivada de f dado un h.

    Parámetros:
    f: función de variable real f(x).
    h: tamaño del paso.
    """

    def _(x):
        return (f(x + h) - f(x))/h

    return _

def operaciones(f,x0,n,x, px, contador):
  if contador < n: 
    if contador == 0:
      px = f(x0)
      return operaciones(f, x0, n, x, px, contador+1)
    else:
      f = derivada(f)
      px += (f(x0) * pow((x-x0), contador)) / math.factorial(contador)
      return operaciones(f, x0, n, x, px, contador+1)
  else:
    return px

def polinomio_taylor(f, x0, n):
    """
    Implementa y retorna el Polinomio de Taylor de grado n centrado en x0.

    Parámetros:
    f: función de variable real f(x).
    x0: punto centro del polinomio.
    n: grado del polinomio.
    """
    def __(x):
        po = operaciones(f, x0, n, x, 0, 0)
        return po
    return __


if __name__ == '__main__':
    # Pruebe aquí el polinomio de Taylor.
    f=lambda x: math.sin(x)
    pol=polinomio_taylor(f,0,4)
    x=0.30
    print(pol(x))