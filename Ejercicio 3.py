#Ejercicio 3. Conversor de euros
#Solicita una cantidad en euros y muestra su equivalente en dólares.

#Utiliza un tipo de cambio almacenado en una variable.

#Euros: 100
#Tipo de cambio: 1.08

#Resultado: 108 dólares

euros = float(input("Ingrese el valor de Euros: "))
VALOR_DOLAR = 1.08
dolar = VALOR_DOLAR * euros

print(f"Resultado: {dolar} dólares")
