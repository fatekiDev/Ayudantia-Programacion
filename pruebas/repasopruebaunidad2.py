# 1. Variables y Tipos de Datos ###

# String
nombre = "Benjamin"

# Int
edad = 20

# Float
altura = 1.75

# Complex
numero_complejo = 3 + 2j

print(type(nombre))
print(type(edad))
print(type(altura))
print(type(numero_complejo))



### 2. Números Complejos ###
# Tramo 1
impedancia1 = 50 + 30j

# Tramo 2
impedancia2 = 40 - 10j

# Suma
impedancia_total = impedancia1 + impedancia2

print("Impedancia total:", impedancia_total)

# Parte real
print("Parte real:", int(impedancia_total.real))

# Parte imaginaria
print("Parte imaginaria:", int(impedancia_total.imag))



### 3. Strings y Métodos ###
texto = " Hola Mundo "

# Eliminar espacios extremos
print(texto.strip())

rut = "19.543.872-K"

# Eliminar puntos
print(rut.replace(".", ""))

nombre = "BENJAMIN"

# Minúsculas
print(nombre.lower())

# Largo de texto
print(len(nombre))

### 4. Ejercicio Tipo Evaluación — RUT ###
rut = " 19.543.872-K "

# Eliminar espacios
rut = rut.strip()

# Eliminar puntos
rut = rut.replace(".", "")

# Largo
largo = len(rut)

print("RUT limpio:", rut)
print("Cantidad de caracteres:", largo)


### 5. input() y Conversión de Datos ###
nombre = input("Ingrese su nombre: ")
print("Hola", nombre)

edad = int(input("Ingrese edad: "))
print(type(edad))

altura = float(input("Ingrese altura: "))
print(type(altura))
# 6. Correos Institucionales
nombre = input("Ingrese nombre completo: ")

# Limpiar espacios
nombre = nombre.strip()

# Minúsculas
nombre = nombre.lower()

# Cambiar espacios por puntos
nombre = nombre.replace(" ", ".")

correo = nombre + "@alumnos.ulagos.cl"

print("Correo generado:", correo)
### 7. Float, int y round() ###
sensor = 1024.7689

# Convertir a entero
entero = int(sensor)

# Redondear
redondeado = round(sensor, 2)
    
print("Original:", sensor)
print("Entero:", entero)
print("Redondeado:", redondeado)

    
### 8. Listas ###
# Pedir datos
t1 = float(input("Ingrese tiempo 1: "))
t2 = float(input("Ingrese tiempo 2: "))
t3 = float(input("Ingrese tiempo 3: "))

# Lista
tiempos_respuesta = [t1, t2, t3]

# Promedio
promedio = (
    tiempos_respuesta[0] +
    tiempos_respuesta[1] +
    tiempos_respuesta[2]
) / 3

# Min y max
minimo = min(tiempos_respuesta)
maximo = max(tiempos_respuesta)

# Brecha
brecha = maximo - minimo

# Mostrar
print("Lista:", tiempos_respuesta)
print("Promedio:", promedio)
print("Mínimo:", minimo)
print("Máximo:", maximo)
print("Brecha:", brecha)
# 9. Errores Típicos
# ERROR
numero = input("Ingrese número: ")
# resultado = numero + 5

# CORRECTO
numero = int(input("Ingrese número: "))
resultado = numero + 5

lista = [10, 20, 30]

# print(lista[3])  # ERROR: índice fuera de rango
# 10. Mini Ejercicios
# Ejercicio 1
# Pedir nombre y edad e imprimir:
# Hola Benja, tienes 20 años

# Ejercicio 2
# Pedir un decimal y mostrar:
# Original, Entero y Redondeado

# Ejercicio 3
# Pedir un texto y mostrar:
# Minúsculas, largo y texto limpio
