#Ejercicio 4. Conversor de temperatura
#Solicita una temperatura en grados Celsius y conviértela a Fahrenheit.

#Fórmula:
#F = C × 9 / 5 + 32

grados = float(input("Ingrese el numero de grados Celsius ºC: "))

formula_fahrenheit = grados * 9 / 5 + 32

print(f"La temperatura en Fahrenheit es: {formula_fahrenheit} ºF")
