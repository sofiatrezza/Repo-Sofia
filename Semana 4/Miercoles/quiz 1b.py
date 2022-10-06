
pathologies = {
             "Respiratory system":
            [
                {
                    "id": 1,
                    "name":"Cystic Fibrosis",
                    "price": 300
                },
                {
                    "id": 2,
                    "name": "Emphysema",
                    "price": 500
                },
                {
                    "id": 3,
                    "name": "Tuberculosis",
                    "price": 450
                }
            ],
            "Nervous system":
            [
                {
                    "id": 4,
                    "name": "Parkinson",
                    "price": 800
                },
                {
                    "id": 5,
                    "name": "Epilepsy",
                    "price": 600
                }
            ],
            "Endocrine system":
            [
                {
                    "id": 6,
                    "name": "Diabetes",
                    "price": 350 },
                {
                    "id": 7,
                    "name": "Acromegaly",
                    "price": 700},
                {
                    "id": 8,
                    "name": "Hashimoto’s thyroiditis",
                    "price": 900
            }]}

'''Registrar y cobrar al paciente: debe solicitarse nombre, apellido y cédula del paciente, y el 
id de la patología que padece. Esta información debe almacenarse en la estructura de datos de su preferencia.
Debe mostrarse en pantalla la factura generada, con los datos del paciente, la patología que padece y el monto 
a pagar.
Ver pacientes: debe preguntarse por la patología a consultar y mostrar los pacientes registrados en el sistema 
que la padezcan.
Menú principal que permita seleccionar la acción que se quiera realizar.
Debe volverse al menú principal cada vez que se termine alguna operación (es decir, el código debe seguir 
ejecutándose hasta que el usuario decida salir).
Los mensajes por consola deben verse ordenados y ser intuitivos.'''

while True:
    print('Bienvenid@ a Clinicas Caracas, como podemos ayudarle:')
    opcion = int(input('Por favor ingrese una opcion valida: \n1 Servicios disponibles\n2 Reservar cita\n3 Salir\n'))
    if opcion == 1:
        categorias = {1: "Respiratory system", 2: "Nervous system", 3: "Endocrine system"}
        categoria = int(input('Seleccione una opcion valida: \n1 Respiratory system\n2 Nervous system\n3 Endocrine system\n'))
        for tipos, lista_de_patologias in pathologies.items():
            if tipos == categorias.get(categoria):
                for patologia in lista_de_patologias:
                    id = patologia.get("id")
                    name = patologia.get("name")
                    price = patologia.get("price")
                    print(f'{id}-{name}-{price}')

    elif opcion == 2:
        patologia_id = int(input('Ingrese el id de la patologia que requiere de una cita: '))
        patologia_seleccionada = None
        for tipos, lista_de_patologias in pathologies.items():
                for patologia in lista_de_patologias:
                    if patologia_id == patologia.get("id"):
                        patologia_seleccionada = patologia
                        break
        if patologia_seleccionada:
            client = { 
                    "Usuario": input('Please enter your full name: '),
                    "ID": input('Please enter your id number: '),
                    "Patologia" : patologia_id
                }
        print("***** RECEIPT *****")
        for key, value in client.items():
            print(key, value)
            for  key, value in patologia_seleccionada.items():
                    print(key, value)
                    break
   
    elif opcion == 3:
            if input("Do you want to exit?: \nY- Yes \nN - No \n").upper() == "Y": 
                break
    else:
        continue

