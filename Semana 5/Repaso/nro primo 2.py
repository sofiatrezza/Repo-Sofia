def es_primo(n):
    contador = 0
    for i in range(1, n):
        if i == 1 or i == n:
            continue
    if n % i == 0:
        contador += 1
    if contador == 0:
        nro_primos = []
        print("Si es número primo")
        nro_primos.append(n)
        print(nro_primos)
    else:
        print("No es número primo")
        es_primo(n)
    return nro_primos

numero= input("Ingrese un numero: ")
numero = int(numero)
es_primo(numero)


