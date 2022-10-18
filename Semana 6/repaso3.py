command = input("Ingrese el comando que desea ejecutar: ")
command = command.replace("()", "o").replace("(al)","al")
print(command)