def opciones(tarifas):
    for key, value in tarifas.items():
            print(f"{key} -BsS/hora {value}", end= "")
            print('')
    opcion = input("Ingrese una opcion: ")
    if tarifas[opcion] is not None:
        return tarifas[opcion]
    
def descuentos(usuario, tarifas):
    descuento = 0
    if usuario.get('horas') > 3:
        descuento += tarifas * 0.15
    return descuento

def datos_cliente(tarifas): 
    usuario = {
        "cedula":input('Ingrese su numero de cedula: '),
        "tipo": input('Ingrese el tipo de vehiculo A (Automatico) o S (Sincronico): '),
        "horas": int(input('Ingrese la cantidad de horas que va a tomar: '))
        }
    usuario['precio'] = descuentos(usuario, tarifas)
    return usuario

tarifas = {
    "A": 2500,
    "S":3500
}

clientes =[] 
print("***** Bienvenid@s a 'La Rapida' *****")
while True:
    opcion = opciones(tarifas)
    cliente = datos_cliente(opcion)
    clientes.append(cliente)
    print(clientes)
    programa = input('Elija una opcion \n1 Nueva inscripcion\n2 Salir\n-->')
    if programa == "1":
        continue
    elif programa == "2":
        break
    

