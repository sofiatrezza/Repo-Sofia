'''Lo han contratado para gestionar el sistema del “Circo de Halloween” que visita la 
ciudad por la fecha que se aproxima, deberá desarrollar un programa en Python para ayudar 
al circo a vender sus paquetes de entradas, existen 2 tipos de paquetes: Atracciones: 
que incluye todo los pases a todas las atracciones del circo; y shows: que incluye todos los 
espectáculos que se realicen en el circo. Los paquetes se cobran por cantidad de personas:

Se desea que realice un programa en Python que pueda realizar las siguientes acciones:
Parte A:
Para cada comprador solicitarle:
1. Nombre completo.
2. Cédula
3. Usuario de Instagram (para un concurso que desea hacer el circo).
4. Paquete a seleccionar.
5. Número de personas que se desea en el paquete seleccionado.
Se debe tomar en cuenta:
● La cédula solo puede tener números.
● Un usuario de Instagram puede tener un maximo de 30 caracteres, pueden incluir letra,
números, puntos ( . ) y guiones bajos ( _ ), no puede contener espacios ni otro tipo de
carácter, y @ se le debe concatenar automáticamente el sistema, luego de recibir el
dato.
● Si el número de personas es par, entonces se le otorgara un descuento del 10%.
● Luego de recibir la información se le deberá mostrar el monto total según el número de
personas y el descuento si aplica, y preguntar al cliente si desea proceder, de ser así, se
mostrará un mensaje de pago exitoso!.
● Si el cliente selecciona combo, se le regalara una camisa y 2 llaveros del circo a cada
persona involucrada en el combo, se le deberá mostrar un mensaje al finalizar la compra sobre el regalo, indicando cuantas camisas y llaveros son en total.
Parte B:
Al final del día para el circo se debe mostrar:
1. La cantidad total de compradores.
2. La cantidad total de compradores por tipo de paquete.
3. La cantidad de clientes que se le otorgó el descuento.
4. El promedio de facturación por tipo de paquete.
5. Deberá hacer una función que escoja un usuario al azar y diga que usuario de
Instagram se llevará el premio.'''

def opciones(paquetes):
    for key, value in paquetes.items():
        for key_i, value_i in value.items():
            print(f'{key} - {value_i}', end="")
            print(" ")
    return input("Seleccione la opcion que desee: \nA Atraccciones\nS Shows\nC Combo\n--> ")

def data_cliente(opciones, paquetes):
    cliente = {
        "nombre_completo": input("Ingrese su nombre completo: "),
        "cedula": input("Ingrese su numero de cedula: "),
        "usuario_ig" : "@" + input("Ingrese su usuario de Instagram: "),
        "paquete": opciones,
        "num_personas": int(input("Ingrese el numero de personas que se desea en el paquete seleccionado: "))
    }
    cliente["total"] = paquetes.get(cliente.get("paquete")).get("precio")
    return cliente

def usuario(cliente):
    usuario_ig : input("Ingrese su usuario de Instagram: ")
    while True:
            if len(usuario_ig) > 30:
                print('Debe tener maximo 30 caracteres')
            

def descuentos(cliente):
    descuento = 0
    if int(cliente.get("num_personas")) % 2 == 0:
        descuento += cliente.get("total") * 0.10
        cliente["total_final"] = cliente.get("total") - descuento

def obsequio(cliente):
    llavero = 0
    camisa = 0
    if cliente.get("paquete") == "C":
        print("Gracias por preferirnos! Le regalamos 2 llaveros de circo y una camisa por cada persona del paquete")
        camisa += cliente.get("num_personas")
        llavero += cliente.get("num_personas")
        cliente["obsequio"] = [camisa, 2* llavero]
        print(f'Nro. Camisas {camisa}/ Nro. Llaveros {2* llavero}')

def total_pago(cliente):
    print('***** FACTURA *****')
    for key, value in cliente.items():
        print(f'{key}- {value}', end="")
        print(" ")

def main():
    paquetes ={
       "A": {"paquete": "atracciones",
        "precio": 10},
        "S": {"paquete": "shows",
        "precio": 15},
        "C": {"paquete": "combo: atracciones+shows",
        "precio": 23}
    }
    compradores = []
    compra_A = []
    compra_S = []
    compra_C = []
    descuentos_otorg = []
    usuarios_ig = []
    while True:
        print('**** Bienvenidos al Circo de Halloween ****')
        opcion = opciones(paquetes)
        cliente = data_cliente(opcion, paquetes)
        compradores.append(cliente)
        usuarios_ig.append(cliente.get("usuario_ig"))
        descuento = descuentos(cliente)
        descuentos_otorg.append(descuento)
        print(descuentos_otorg)
        obsequio_circo = obsequio(cliente)
        total = total_pago(cliente)
        programa = input("Desea proceder al pago: \n1 Si\n2 No\n3 Continuar comprando\n-->")
        if programa == "1":
            print("Pago Exitoso!")
            break
        elif programa == "3":
            continue
        else:
            break

    #Final day report
        #Nro de comprador
    print("***** Reporte del Dia *****")
    print("El numero de compradores:", len(compradores))
    
        #Nro de comprador por paquete
    if cliente.get("paquete") == 'A':
        compra_A.append(cliente)
        print('Nro de compradores del paquete de Atracciones: ', len(compra_A))
    if cliente.get("paquete") == 'S':
        compra_S.append(cliente)
        print('Nro de compradores del paquete de Shows: ', len(compra_S))
    if cliente.get("paquete") == 'C':
        compra_C.append(cliente)
        print('Nro de compradores del paquete de Combo: ', len(compra_C))

        #Nro de clientes que se les otorgo descuento
    #print('Nro de compradores con descuento: ', len(descuento))

main()