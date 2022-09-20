precio = 3.49
descuento = 0.60
barras = int(input("Ingrese el numero de barras de pan vendidas que no son del día: "))
costo = barras * precio - (1 - descuento)
print(f"El costo de una barra de pan fresca de {precio}")
print(f"El descuento sobre una barra de pan no fresca es {descuento}")
print(f"El costo final a pagar es {costo}")