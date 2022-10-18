def prime(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    print('You got a discount!')     
    return True

client_Q =[]
client_F =[]
client_B =[]
def main():
    #Linea de productos
    products = {
        'Q':{'description': 'chemical',
            'price': 1000 },
        'F':{'description': 'pharmacist',
            'price': 2500 },
        'B':{'description': 'biological',
            'price': 4000 }
    }
    clients = []
    max_purchase = 0
    max_rif = 0
    discount_Q = 0
    discount_F = 0
    discount_B = 0
    total_purchase = []
    while True:
        #Bienvenida 
        print('***** Welcome to Saman International *****')
        for key, value in products.items():
            for key_i, value_i in value.items():
                print(f'{key} - {value_i}', end="")
                print(" ")
        #Input del cliente
        client = {
            "rif": int(input('Please enter your rif: ')),
            "product_type": input("Select the type of product you are looking for: \nQ Chemical\nF Pharmacist\nB Biological\n--> "),
            "payment_method": input("Select your payment method: \nC Counted\nR Credit\n-->  "),
        }
        
        client["total"] = products.get(client.get("product_type")).get("price")
        #Variables
        discount = 0
        tax = 0
        recharge = 0
        #Impuesto
        if client.get("product_type") == "F":
            tax += products.get(client.get("product_type")).get("price") * 0.12
        elif client.get("product_type") == "Q":
            tax += products.get(client.get("product_type")).get("price") * 0.12
        #Recargo
        if client.get("payment_method") == "R":
            recharge += products.get(client.get("product_type")).get("price") * 0.10
        #Descuentos 
        if client.get("payment_method") == "C":
            discount += products.get(client.get("product_type")).get("price") * 0.03
        if int(client.get("total")) % 2 == 0:
            discount += products.get(client.get("product_type")).get("price") * 0.02
        if prime(client.get("rif")):
            discount += products.get(client.get("product_type")).get("price") * 0.05

         #Monto a pagar
        client["final_total"] = products.get(client.get("product_type")).get("price") - discount + tax +recharge
        clients.append(client)
        
        #Factura
        print('***** RECEIPT *****')
        for key, value in client.items():
            print(f'{key}- {value}', end="")
            print(" ")
        print("tax", tax)
        print("recharge", recharge)

        if input("Do you want to exit? \nY Yes\nN No\n--> ") == "Y":
            break

    #Final day report
        #Nro de clientes por producto
    print("***** DAY REPORT *****")
    print("The number of clients for each type of product:")
    if client.get("product_type") == "Q":
        client_Q.append(client)
    print(f'-> Chemical {len(client_Q)}')
    if client.get("product_type") == "F":
        client_F.append(client)
    print(f'-> Pharmacist {len(client_F)}')
    if client.get("product_type") == "B":
        client_B.append(client)
    print(f'-> Biological {len(client_B)}')
        
        #Monto total descuento cobrado por producto
    print("The total discounts for each type of product:")
    if client.get("product_type") == "Q":
        discount_Q += discount
    print('Total discounts Chemical', discount_Q)
    if client.get("product_type") == "F":
        discount_F += discount
    print('Total discounts Pharmacist', discount_F)
    if client.get("product_type") == "B":
        discount_B += discount
    print('Total discounts Biological', discount_B)
    
        #Compra mas alta 
    if int(client.get('final_total')) > max_purchase:
        max_purchase = int(client.get('final_total'))
        max_rif = client.get('rif')
        print('The max purchase of the day: ', max_rif) 

        #Monto total Facturado
    total_purchase.append(int(client.get("final_total")))
    print("Total invoiced on the day", sum(total_purchase))
           
main()