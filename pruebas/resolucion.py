"""1. En el an ́alisis de antenas y redes de telecomunicaciones, la impedancia de una linea de
transmisi on se compone de una parte real (resistencia) y una parte imaginaria (reac-
tancia). Un ingeniero necesita calcular la impedancia total sumando los componentes
de dos tramos de la red de fibra  ́optica de la universidad."""

# A) Defina la impedancia del Tramo 1 como un numero complejo con parte real 50 y
#       parte imaginaria 30 (50 + 30j).

#tramo 1
impedancia1 = 50 + 30j

# B) Defina la impedancia del Tramo 2 de la misma forma, con parte real 40 y parte
#    imaginaria −10 (40 − 10j).

#tramo 2
impedancia2 = 40 -10j

#suma de ambos tramos
sumaimpedancias = impedancia1 + impedancia2


#d) Muestre en pantalla la impedancia total, y luego imprima por separado solo la
#    parte real (convertida a numero entero int) y la parte imaginaria (convertida a
#      int) usando los atributos .real y .imag.

print(sumaimpedancias)

impedanciareal = int(sumaimpedancias.real)
print(impedanciareal)

impedanciaimag = int(sumaimpedancias.imag)
print(impedanciaimag)

### LISTO ### 


"""2.- Al desarrollar sistemas inform ́aticos, los usuarios suelen ingresar datos con espacios
accidentales o formatos incorrectos. El sistema de la biblioteca de la ULagos recibi ́o el
RUT de un estudiante, pero viene “sucio” con espacios al inicio, al final y con puntos
intermedios: “ 19.543.872-K " """

# a) Guarde el RUT original en una variable de tipo string.
rut = " 19.543.872-k " # tiene que quedar: "19543872-k"

# b) Utilice el metodo propio de Python para eliminar los espacios en blanco de los extremos.
rut_sin_espacio = rut.strip() # strip() quita espacios

# c) Utilice un metodo propio de Python para eliminar los puntos (.)
rut_final = rut_sin_espacio.replace(".","") #remplazar

# d)Calcule el largo total del RUT ya limpio (sin espacios ni puntos) y muestre el
#       resultado por pantalla junto al RUT con su nuevo formato.

largo_de_rut = len(rut_final)

print(f"largo del rut: {largo_de_rut} | rut: {rut_final}")

"""

3. El Departamento de Admisi ́on de la Universidad requiere un script basico para registrar
correos institucionales. El programa debe solicitar al usuario que ingrese su nombre
completo por terminal. Debido a que los usuarios pueden escribir con may ́usculas y
min ́usculas desordenadas o con espacios de m ́as, el programa debe estandarizar el texto.
Escribe un programa que:
a) Solicite por terminal el nombre del estudiante. LISTA
b) Remueva los espacios sobrantes de los extremos. LISTA
c) Convierta todo el texto a minusculas. LISTA
d) Reemplace los espacios intermedios por puntos (.) para simular la estructura de
un correo electronico. LISTA
e) Muestre en pantalla el resultado final con el texto @alumnos.ulagos.cl concatenado
al final. LISTO

"""

nombre_estudiante = input("Usuario ingrese su nombre completo, separando nombres y apellidos por un espacio intermedio ")

nombre_estudiante = nombre_estudiante.strip()
nombre_estudiante = nombre_estudiante.lower()
nombre_estudiante = nombre_estudiante.replace(" ",".")


print(nombre_estudiante + "@alumnos.ulagos.cl")

"""
4. En fisica de particulas, la precisi ́on de los decimales es crıtica. Un sensor de presion

hidr ́aulica en un laboratorio de la universidad entrega una medida de 1024.7689 Pascales 
como tipo float. Escribe un programa que realice lo siguiente:

a) Defina la variable con el valor del sensor. LISTO
b) Convierta dicho valor a un n ́umero entero (int), descartando los decimales, y
almac ́enelo en una variable nueva. LISTA
c) Utilice un metodo propio de Python para redondear el valor original del sensor a
exactamente 2 decimales y guarde el resultado en otra variable. LISTA
d) Imprima un mensaje comparativo que muestre por terminal: el valor original, el
valor truncado como entero y el valor redondeado."""

valor_sensor = 1024.7689
valor_sensor_entero = int(valor_sensor)
redondeado_valor_sensor = round(valor_sensor,2)

print(f"A continuacion se mostraran los valores que ha entregado el sensor \n Valor original(inicial): {valor_sensor} \n Valor del sensor en numero entero: {valor_sensor_entero} \n Valor del sensor redondeado: {redondeado_valor_sensor}")

"""
5. Una plataforma web de la Universidad de Los Lagos mide la velocidad de respuesta
de su servidor de asignaci ́on de asignaturas. Se han tomado 3 muestras de tiempo de
respuesta (en milisegundos) de forma manual. Escribe un programa en Python que:
a) Solicite al administrador de la plataforma ingresar por terminal los 3 tiempos de
respuesta (los cuales pueden contener decimales, tipo float). LISTA
b) Almacene los 3 valores ingresados dentro de una lista de Python que debe tener
por nombre tiempos respuesta. LISTA

c) Acceda por medio de sus  ́indices ([0], [1], [2]) a los elementos de la lista para
calcular el tiempo promedio de respuesta del servidor. LISTA

d) Encuentre el tiempo m ́as r ́apido (m ́ınimo) y el tiempo m ́as lento (m ́aximo) utili-
zando las funciones propias de Python. LISTA

e) Calcule la “brecha de rendimiento”, que corresponde a la resta entre el tiempo
m ́aximo y el m ́ınimo. Lista

f ) Imprima en pantalla la lista completa de datos y el reporte con el promedio y la
brecha calculada."""

toma_tiempo1 = float(input("Administrados ingrese el tiempo de respuesta numero 1: "))
toma_tiempo2 = float(input("Administrados ingrese el tiempo de respuesta numero 2: "))
toma_tiempo3 = float(input("Administrados ingrese el tiempo de respuesta numero 3: "))

tiempos_respuestas = []
tiempos_respuestas.append(toma_tiempo1)
tiempos_respuestas.append(toma_tiempo2)
tiempos_respuestas.append(toma_tiempo3)

promedio_tiempos = (tiempos_respuestas[0] + tiempos_respuestas[1] +tiempos_respuestas[2] ) / len(tiempos_respuestas)

min_tiempo = min(tiempos_respuestas) # mas rapido
max_timepo = max(tiempos_respuestas) # mas lento

brecha_tiempo = (max_timepo - min_tiempo)

print(f" A continuacion la lista completa de los tiempos de respuesta y datos: \n Tiempos de respuesta: {tiempos_respuestas} \n Promedio: {promedio_tiempos} \n Brecha de tiempo: {brecha_tiempo}")