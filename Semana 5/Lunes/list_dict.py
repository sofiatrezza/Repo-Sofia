notas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Quimica": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Logica": [1.5, 4.0, 4.5]
}

#Calcula la nota final de cada materia (30%, 30% y 40%), 
# y agregue el valor a los datos

#Para llamar a los keys de una diccionario (calculo, quimica, deporte, logica):
'''for key in notas.keys():
    print(key)'''

#Para llamar a los valores de cada key (notas):
'''for value in notas.values():
    print(value)'''

#Para llamar tanto a los keys como a los values, se utiliza el .items():
'''for key, value in notas.items():
    print(key, value)'''