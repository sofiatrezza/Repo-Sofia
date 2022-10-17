aspirantes = []
trimestre_A = []
trimestre_B = []

def info_estudiante():
    estudiante = {
        "cedula":input('Ingrese su numero de cedula: '),
        "promedio": input('Ingrese su promedio de notas: '),
        }
    aspirantes.append(estudiante)
    return estudiante
    
def ubicacion_trimestre(estudiante):
    if int(estudiante.get("promedio"))>= 18:
        trimestre_A.append(estudiante)
        print("Su trimestre asignado fue el 'A'")
    elif int(estudiante.get("promedio"))>= 12:
        trimestre_B.append(estudiante)
        print("Su trimestre asignado fue el 'B'")
    elif int(estudiante.get("promedio"))< 12:
        print("Su solicitud ha sido rechazada")
    
def reporte_final(estudiante):
    print("Reporte de inscripciones del dia:")
    print(f'Total de alumnos aspirantes: {len(aspirantes)}')
    print(f'Total de alumnos asignados al trimestre "A" es de {len(trimestre_A)}')
    print(f'Total de alumnos asignados al trimestre "B" es de {len(trimestre_B)}')
    promedio_A = len(trimestre_A)/len(aspirantes)
    promedio_B = len(trimestre_B)/len(aspirantes)
    print(f'El promedio de aspirantes del trimestre "A" es de {promedio_A} y el del trimestre "B" es de {promedio_B}')

def reporte_promedio(aspirantes):
    sum = 0
    for aspirante in aspirantes:
        for key, value in estudiante.items():
            sum += int(estudiante.get('promedio'))
            print(sum)
            promedio_general = sum / len(aspirantes)
            print(f'El promedio general del trimestre es de {promedio_general}')
            return promedio_general
            
print("Bienvenid@, ingrese sus datos para evaluar su solicitud")
while True:
    estudiante = info_estudiante()
    ubicacion = ubicacion_trimestre(estudiante)
    
    opcion = input('Insertar reporte final del dia: \n1 Si\n2 No\n3 Continuar inscripcion\n-->')
    if opcion == "1":
        reporte = reporte_final(estudiante)
        promedio = reporte_promedio(estudiante)
        break
    elif opcion == "2":
        break
    elif opcion == "3":
        continue 
    






