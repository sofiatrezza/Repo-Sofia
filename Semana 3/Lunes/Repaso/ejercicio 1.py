frase = input("Por favor ingrese una frase: ")
letra = input("Por favor ingrese una letra: ")
cont = 0
for i in frase:
    if i == letra:
        cont += 1
    print("La letra '%s' aparece %2i veces en la frase '%s'." % (letra, cont, frase))