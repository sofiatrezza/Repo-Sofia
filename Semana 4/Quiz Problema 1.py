numero_feliz = int(input('Ingrese un numero para ver si es feliz: '))

sumas_cuadrados = []
es_feliz = True
suma_sqr = numero_feliz
while (sum(int(dig) ** 2 for dig in str(suma_sqr))) != 1:
    numbers = []
    for dig in str(suma_sqr):
        numbers.append(int(dig) ** 2)
    suma_sqr = sum(numbers)
    for num in str(suma_sqr):
        if int(num) in sumas_cuadrados:
            es_feliz = False
    if es_feliz == False:
        break
    sumas_cuadrados.append(suma_sqr)


if es_feliz == True:
    print(f"El numero {numero_feliz} es feliz")
else:
    print(f"El numero {numero_feliz} no es feliz")
