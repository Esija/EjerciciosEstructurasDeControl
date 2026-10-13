#Ejercicio 5. Precio final
#Solicita:

#Precio de un producto.
#Porcentaje de IVA.
#Calcula:

#Importe del IVA.
#Precio final.
#Ejemplo:

#Precio: 100
#IVA: 21

#IVA: 21 €
#Precio final: 121 €

precio = float(input("Ingrese el precio del Producto: "))

IVA = 0.21

iva_del_producto = IVA * precio
precio_final = precio + iva_del_producto

print("El precio del producto es: ", precio_final)
print("El iva del producto es: ", IVA)
