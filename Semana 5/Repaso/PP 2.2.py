'''La Unidad de Radiología de una Clínica en Caracas, ofrece varios Estudios a sus clientes. Los Estudios
son de tres tipos:
Cuando el Cliente, solicita un Estudio en la Unidad de Radiología, se le solicitan los siguientes datos:
Cedula de Identidad, Edad, Sexo (F=Femenino; M=Masculino, y el Tipo de Estudio (uno solo por
cliente) que se le va a efectuar. Cuando el cliente es Femenino y mayor de 55 años, o Masculino
mayor de 65 años (Tercera Edad), el Sistema les otorga un descuento de 25%. A todos los clientes
impares se les otorga un 2% adicional de descuento.
A Para cada Cliente, el Programa deberá Desplegar la Información del Recibo con los
siguientes datos:
1 El número de su cédula de identidad
2 Su Edad
3 El Código del Sexo
4 El Tipo de Estudio
5 El Monto Neto a Pagar, habiéndole aplicado el descuento para los casos que aplique.
B Al final del Día.
1 La cantidad de Clientes por tipo de Estudio.
2 El Monto Total de Descuentos Otorgados
3 El Monto Total Neto Facturado
4 El Promedio de Pago de todos los Clientes
5 El promedio de pago por tipo de estudio'''

paciente_U = []
paciente_T = []
paciente_R = []
descuentos_otorg = []
def tipo_estudio(estudios):
    for key,value in estudios.items():
        for key_interno, value_interno in value.items():
            print(f'{key} - {value_interno}', end="")
            print(" ")
    return input('Seleccione una opcion: \nU Ultrasonido\nT Tomografia\nR Resonancia\n-->')

def datos_cliente(opcion):
    paciente ={
        "Cedula": input("Ingrese su numero de cedula: "),
        "Edad": input("Ingrese su edad: "),
        "Sexo": input("Ingrese su sexo--> M - Masculino o F - Femenino: "),
        "Estudio": opcion
    }
    return paciente

def descuentos_pacientes(estudios, paciente, base_datos):
    descuento = 0
    if paciente.get("Sexo") == "F" and int(paciente.get("Edad"))> 55:
        descuento += estudios.get(paciente.get("Estudio")).get("Precio") *0.25
    if paciente.get("Sexo") == "M" and int(paciente.get("Edad")) > 65:
        descuento += estudios.get(paciente.get("Estudio")).get("Precio") *0.25
    if base_datos % 2 != 0:
        descuento += estudios.get(paciente.get("Estudio")).get("Precio") *0.02
    descuentos_otorg.append(descuento)
    print(descuentos_otorg)
    return descuento

def facturacion(estudios, paciente):
    print("**** RECEIPT ****")
    print("Cedula", paciente.get("Cedula"))
    print("Edad", paciente.get("Edad"))
    print("Sexo", paciente.get("Sexo"))
    print("Estudio", estudios.get(paciente.get("Estudio")).get("Descripcion"))

def pago(estudios, paciente, descuento):
    return estudios.get(paciente.get('Estudio')).get('Precio') - descuento

def cliente_estudio(paciente):
    if paciente.get("Estudio") == 'Ultrasonido':
        paciente_U.append(paciente)
        print(len(paciente_U))
    if paciente.get("Estudio") == 'Resonancia':
        paciente_R.append(paciente)
        print(len(paciente_R))
    if paciente.get("Estudio") == 'Tomografia':
        paciente_T.append(paciente)
        print(len(paciente_T))

def monto_neto(paciente):
    facturado = 0


def main():
    estudios = {
        "U":{"Descripcion":"Ultrasonido",
            "Precio": 8900},
        "T":{"Descripcion":"Tomografia",
            "Precio": 12640},
        "R":{"Descripcion":"Resonancia",
            "Precio": 15600}
        }

    base_datos =  []
    print("Bienvenido al Hospital de Clinicas Caracas")
    while True:
        opcion = tipo_estudio(estudios)
        cliente = datos_cliente(opcion)
        base_datos.append(cliente)
        descuentos = descuentos_pacientes(estudios, cliente, len(base_datos))
        print(descuentos)
        total = pago(estudios, opcion, descuentos)
        facturacion(estudios, cliente, total)
        print("**** REPORTE DIARIO ****")
        cliente_estudios = cliente_estudio(opcion)
        

main()

