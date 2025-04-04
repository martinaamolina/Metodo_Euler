# -*- coding: utf-8 -*-
"""
Created on Thu Mar 27 18:21:11 2025

@author: Lenovo
"""

"""
Método de Euler para aproximar la solución de una EDO de primer orden.
Parámetros:
f  -> Función que define la EDO dy/dx = f(x, y)
x0 -> Valor inicial de x
y0 -> Valor inicial de y
h  -> Tamaño del paso
n  -> Número de pasos a realizar
"""
import math

def metodo_euler(f, x0, y0, h, n):
    
    x = x0  # Inicializamos x
    y = y0  # Inicializamos y
    
    for _ in range(n):  # Iteramos n veces
        y = y + h * f(x, y)  # Aplicamos la fórmula de Euler
        x = x + h  # Avanzamos en x
    
    return y  # Devuelve la aproximación final.

#-----------------------------------------------------------------------

# Definimos la ecuación diferencial para el Ejercicio 1: dy/dx = 0.2 * x * y
def edo1(x, y):
    return 0.2 * x * y

#---------------------------------------------------------------------------

# Función para la solución exacta del Ejercicio 1: y(x) = e^(-0.1) * e^(0.1 * x^2)
def solucion_exacta_edo1(x):
    return math.exp(-0.1) * math.exp(0.1 * x**2)

#---------------------------------------------------------------------------------

# Definimos la ecuación diferencial para el Ejercicio 2: dI/dt = 15 - 3 * I
def edo2(t, I):
    return 15 - 3 * I

#----------------------------------------------------------------------------------


# Función para la solución exacta del Ejercicio 2: I(t) = 5 * (1 - e^(-3 * t))
def solucion_exacta_edo2(t):
    return 5 * (1 - math.exp(-3 * t))

#--------------------------------------------------------------------

# EJERCICIO 1

print("  " + "-"*30)
print(" EJERCICIO 1: y' = 0.2 * x * y ")
print("-"*30 + "  ")


x_inicial = 1
y_inicial = 1
x_final = 1.5

# Con h = 0.1
h1 = 0.1
n1 = int((x_final - x_inicial) / h1)  # Cantidad de pasos
aprox1 = metodo_euler(edo1, x_inicial, y_inicial, h1, n1)
exacta1=solucion_exacta_edo1(x_final)
error1= abs(exacta1 - aprox1)
print("La aproximación con h=0.1 es:", aprox1)
print ("  ")

print("La solucion exacta es: ",exacta1)
print ("  ")

print("El error con h=0.1 es: ",error1)
print ("  ")

# Con h = 0.05
h2 = 0.05
n2 = int((x_final - x_inicial) / h2)  # Más pasos, mayor precisión
aprox2 = metodo_euler(edo1, x_inicial, y_inicial, h2, n2)
exacta2=solucion_exacta_edo2(x_final)
error2= abs(exacta2 - aprox2)
print("La aproximación con h=0.05 es:", aprox2)
print ("  ")

print("La solucion exacta es: ",exacta2)
print ("  ")

print("El error con h=0.05 es: ",error2)
print ("  ")



#---------------------------------------------------------------------


#EJERCICIO 2

print("  " + "-"*30)
print(" EJERCICIO 2: I' = 15 - 3I ")
print("-"*30 + "  ")



t_inicial = 0
I_inicial = 0
t_final = 0.5
h3 = 0.1
n3 = int((t_final - t_inicial) / h3)
aprox3 = metodo_euler(edo2, t_inicial, I_inicial, h3, n3)
exacta3 = solucion_exacta_edo2(t_final)  # Solución exacta en t=0.5
error3 = abs(exacta3 - aprox3)  # Cálculo del error
print("La aproximación de la corriente en t=0.5 es: ",aprox3)
print ("  ")
print("La solución exacta es: ",exacta3)
print ("  ")
print("El error en t=0.5 es: ",error3)
print ("  ")


#_----------------------------------------------------------------------------


#MÉTODO DE EULER; PARA INGRESO DEL USUARIO


print("  " + "-"*30)
print("INGRESO DEL USUARIO ")
print("-"*30 + "  ")

# Solicitar valores al usuario
x_inicial = float(input("Ingresa el valor inicial de x (por ejemplo, 1): "))
y_inicial = float(input("Ingresa el valor inicial de y (por ejemplo, 1): "))
x_final = float(input("Ingresa el valor final de x (por ejemplo, 1.5): "))
h = float(input("Ingresa el valor del paso h (por ejemplo, 0.1): "))

# Calcular el número de pasos n
n = int((x_final - x_inicial) / h)

# Aplicar el método de Euler
aproximacion = metodo_euler(edo1, x_inicial, y_inicial, h, n)
solucion_exacta = solucion_exacta_edo1(x_final)  # Solución exacta en x=1.5
error = abs(solucion_exacta - aproximacion)  # Cálculo del error

# Mostrar los resultados
print("EL resultado de aplicar método de Euler es:")
print("   ")
print("La aproximación con h= ",h," es: ",aproximacion)
print("   ")
print("La solución exacta es: ",solucion_exacta)
print("   ")
print("El error es: ",error)



