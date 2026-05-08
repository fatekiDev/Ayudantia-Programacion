# Cree un sistema en el cual el usuario debe ingresar su nota de promedio final y este sistema debe calcular si el usuario aprobo o no.

nota_usario = float(input("usuario ingrese su promedio final para informarle si paso o no de curso: "))
if nota_usario >= 4.0: # si
    print("Aprobo")
elif nota_usario < 4: # elif -- >sino si | else --> sino/de lo contrario
    print("Reprobo")