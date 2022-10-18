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
    base_datos =[]
    descuentos_otorg = []
    total_cancelado = []
    paciente_U = []
    paciente_T = []
    paciente_R = []
    pago_U = []
    pago_T = []
    pago_R = []
    while True:
        #Bienvenida y obtencion de datos
        print('**** Bienvenid@ a la Unidad de Radiologia ****')
        for key,value in estudios.items():
            for key_interno, value_interno in value.items():
                print(f'{key} - {value_interno}', end="")
                print(" ")
        paciente = {
        "tipo_estudio" : input('Ingrese el tipo de estudio: \nU Ultrasonido\nT Tomografia\nR Resonancia\n -->').upper(),
        "cedula" : input('Por favor ingrese su cedula: '),
        "edad" : int(input('Por favor ingrese su edad: ')),
        "sexo" : input('Ingrese:\nF Femenino\nM Masculino\n--> ')
        }
        #Descuentos
        descuento = 0
        if paciente.get("sexo") == "F" and paciente.get("edad") > 55:
            descuento += estudios.get(paciente.get("tipo_estudio")).get("Precio") * 0.25
        if paciente.get("sexo") == "M" and paciente.get("edad") > 65:
            descuento += estudios.get(paciente.get("tipo_estudio")).get("Precio") * 0.25
        if len(base_datos)+1 % 2 != 0:
            descuento += estudios.get(paciente.get("tipo_estudio")).get("Precio") * 0.02
        descuentos_otorg.append(descuento)
    

        paciente["precio"] = estudios[paciente["tipo_estudio"]]["Precio"] - descuento
        
        #total
        total = estudios.get(paciente.get("tipo_estudio")).get("Precio") - descuento
        total_cancelado.append(total)

        #Factura
        print('***** FACTURA *****')
        print("Cedula", paciente.get("cedula"))
        print("Edad", paciente.get("edad"))
        print("Sexo", paciente.get("sexo"))
        print("Tipo de Estudio", paciente.get("tipo_estudio"))
        print("Monto", total)

        base_datos.append(paciente)
        #Datos del dia
        print('***** REPORTE DIARIO *****')
        #Cantidad de clientes por estudio
        if paciente.get("tipo_estudio") == "U":
            paciente_U.append(paciente)
            print("Cantidad de pacientes de Ultrasonido: ", len(paciente_U))
        if paciente.get("tipo_estudio") == "T":
            paciente_T.append(paciente)
            print("Cantidad de pacientes de Tomografia: ",len(paciente_T))
        if paciente.get("tipo_estudio") == "R":
            paciente_R.append(paciente)
            print("Cantidad de pacientes de Resonancia: ",len(paciente_R))
        #Descuentos otorgados
        print("Total descuentos otorgados", sum(descuentos_otorg))
        #Promedio de pago de los clientes
        print("Cobro total del dia", sum(total_cancelado)/len(total_cancelado))
        #Promedio de pago tipo de estudio
        if paciente.get("tipo_estudio") == "U":
            pago_U.append(paciente.get("precio"))
            print("Cantidad de pacientes de Ultrasonido: ", len(paciente_U))
        if paciente.get("tipo_estudio") == "T":
            paciente_T.append(paciente)
            print("Cantidad de pacientes de Tomografia: ",len(paciente_T))
        if paciente.get("tipo_estudio") == "R":
            paciente_R.append(paciente)
            print("Cantidad de pacientes de Resonancia: ",len(paciente_R))
        

        
            
            
        if input("Desea continuar comprando? \nS Si\nN No\n--> ") == "N":
            break

main()