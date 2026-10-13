#Ejercicio 6. Tiempo
#Solicita una cantidad de segundos y conviértela a:

#Horas.
#Minutos.
#Segundos.
#Ejemplo:

#Segundos: 3672

#1 hora
#1 minuto
#12 segundos

segundos = float(input("Ingrese el valor de los segundos: "))

segundos_finales = segundos

minutos = segundos / 60

horas = segundos / 3600

print(f"Tienes un total de {horas} horas, {minutos} minutos y {segundos_finales} segundos")
