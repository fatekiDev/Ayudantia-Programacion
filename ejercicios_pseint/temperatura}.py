""" SOLUCION PSEINT
Algoritmo celcius_a_fahrenheit
	
	definir C,F como real
	
	Escribir "Usuario ingrese la temperatura en Grados Celcius para transformarla en Fahrenheit"
	leer C
	
	F = (C * 1.8) + 32
	Escribir "La temperatura es : ", F
	
	
	
FinAlgoritmo
"""

# SOLUCION PYTOHN

temperatura_c = input("Usuario ingrese la temperatura en grados Celcius para transformarla en Fahrenheit: ") # Argumento = Todo lo que este dentro de parentesis en alguna funcion

fahrenthei = ( float(temperatura_c) * 1.8 ) +32 # Set/Formatea/Modificar el tipo de dato mediante la funcion float() | str() | bool() | int()

print(f"La temperatura es: {fahrenthei} la cual equivale a la temperatura anterior en celcius que era {temperatura_c}")