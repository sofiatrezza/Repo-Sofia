def es_primo(rif):
    numero = int(rif[len(-1)])
    aux = numero -1
    while aux > 1:
        if numero % aux == 0:
            return False

def main():
    productos = {
        "F": {"descripcion": "Farmaceutico",
            "precio":2500},
        "Q": {"descripcion": "Quimico",
            "precio":1000},
        "B": {"descripcion": "Biologico",
        "precio":4000}
    }

    #contadores para la data del dia
    cliente_f = 0
    cliente_q = 0
    cliente_b = 0
    descuento_f = 0
    descuento_q = 0
    descuento_b = 0
    compra_max = 0
    rif_compra_max = 0
    total_dia = 0
    while True:
            #Variables
        rif= input('Por favor ingrese su rif: ')
        linea_producto = input('Ingrese la linea del product: \nF Farmaceutico\nQ Quimico\nB Biologico\n -->')
        forma_pago = input('Ingrese la forma de pago:\nC One time\nR Credito\n -->')
        monto = productos.get(linea_producto).get("precio")
        recargo = 0
        discount = 0    
        impuesto = 0
            #descuento
        if forma_pago == "C":
            discount +=  monto * 0.03
        if int(monto) % 2 == 0:
            discount +=  monto *0.02
        if es_primo(rif):
            discount += monto *0.05

        #impuesto
        if linea_producto != 'F':
            impuesto += monto * 0.12
        #totales
        total = monto + recargo - discount + impuesto

        #Datos del dia
        total_dia += total
        if linea_producto == 'F':
            cliente_f += 1
            descuento_f += discount
        elif linea_producto == 'Q':
            cliente_q += 1
            descuento_q += discount
        elif linea_producto == 'B':
            cliente_b += 1
            descuento_b += discount
            
        if total > compra_max:
            rif_compra_max = rif 
            compra_max


        print('***** FACTURA *****')
        print("RIF", rif)
        print('Producto', productos.get(linea_producto).get("descripcion"))
        print("Metodo de Pago", forma_pago)
        print('Descuento', discount)
        print('Impuesto', impuesto)
        if input("Desea continuar comprando? \nS Si\nN No\n--> ") == "N":
            break

        print('***** DATA DEL DIA *****')
        print('Clientes Farmaceutico', cliente_f)
        print('Clientes Quimico', cliente_q)
        print('Clientes Biologico', cliente_b)
        print('Descuentos Farmaceuticos', descuento_f)
        print('Descuentos Quimico', descuento_q)
        print('Descuentos Biologico', descuento_b)

main()