#Te han contratado ya que se desea descifrar 
# el código secreto debajo, se sabe que es una 
# matrix 9X4, segun un cientifico de la NASA para 
# poder descifrar el mensaje hay que transponer la 
# matriz (convertirla a 4X9).

codigos= [
['L', 'm', 'l', ' '], 
['o', 'o', ' ', 's'], 
['g', 's', 'm', 'e'], 
['r', 't', 'e', 'c'], 
['a', 'r', 'n', 'r'], 
['s', 'a', 's', 'e'], 
['t', 'r', 'a', 't'], 
['e', ' ', 'j', 'o'], 
[' ', 'e', 'e', '!']
]



matriz = []
for i in range(4):
    insideList = []
    for j in range(9):
        insideList.append(1)
        matriz.append(insideList)
print(matriz)



'''codigo_dado = [['m', 's','r'],['a','a','e'],['s','p','t'],['a','o','o']
lista_codigo_dado = []
for lista in codigo_dado:
    for elem in lista:
         lista_codigo_dado.append(elem)

matrix = []
for i in range(4):
    insideLists = []
    pos = 0
    for j in range(9):
        insideLists.append(lista_codigo_dado[pos])
        pos += 1
    matrix.append(insideLists)
print(matrix)'''