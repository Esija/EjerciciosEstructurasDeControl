#Ejercicio 7. Mayor de edad
#Solicita la edad de una persona.

#Muestra:

#Eres mayor de edad
#o:

#Eres menor de edad

edad = int(input("Escribe tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")

elif edad <= 17:
    print("Eres menor de edad")