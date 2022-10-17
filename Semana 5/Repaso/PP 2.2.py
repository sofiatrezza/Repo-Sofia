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

def main():
    estudios = {
        "U":{"Descripcion":"Ultrasonido",
        "Precio": 8900},
        "T":{"Descripcion":"Tomografia",
        "Precio": 12640},
        "R":{"Descripcion":"Resonancia",
        "Precio": 15600}
    }
    return estudios

def tipo_estudio(estudios):
    for key,value in estudios.items():
        for key_interno, value_interno in value.items():
            print(f'{key} - {value_interno}', end="")
    return input('Seleccione una opcion: \n1 Ultrasonido\n2 Tomografia\n3 Resonancia\n-->')
    


def datos_cliente(estudios):
    paciente ={
        "Cedula": input("Ingrese su numero de cedula: "),
        "Edad": input("Ingrese su edad: "),
        "Sexo": input("Ingrese su sexo--> M - Masculino o F - Femenino:"),
        "Tipo de Estudio": tipo_estudio
    }
    return paciente


base_datos =  []
print("Bienvenido al Hospital de Clinicas Caracas")
while True:
    opciones = tipo_estudio(estudios)
    pacientes = datos_cliente(estudios)


main()
