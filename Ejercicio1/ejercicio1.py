import csv, re
from email import email 

def crearCuenta(correos = "" , contraseña = ""):
	datos = correos.split("@")
	dom = datos[1].split(".")
	return email(datos[0], dom[0], dom[1], contraseña)
    
if __name__ == '__main__':
    nombre = input("Ingrese su nombre: ")
    mail = input("Ingrese su email: ")
    email.__contrasena = input("Ingrese la contraseña: ")
    print(f"contraseña actual: "+email.__contrasena)
    print(f"Estimado {nombre} te enviaremos tus mensajes a la dirección {mail}")        #punto 1
    nuevaContra = input("Ingrese la nueva contraseña: ")
    print(f"Su nueva contraseña es:"+email.modificarContra(email,nuevaContra))

    #PUNTO 3
    datos = (input("Ingrese su email: ")).split("@")
    dominio = datos[1].split(".")
    mail2 = email(datos[0], dominio[0], dominio[1], "")
    print(mail2.retornaEmail())
    print(mail2.getDominio())
    email.__idCuenta = datos[0]
    email.__dominio = dominio[0]
    email.__tipoDominio = dominio[1]
    print(f"IdCuenta: "+email.__idCuenta+" - Dominio: "+email.__dominio+" - Tipo: "+email.__tipoDominio)
    
    #PUNTO 4
    archivo = open('correos.csv')
    reader = csv.reader(archivo, delimiter=';')
    correos = []
    email_regex = r'^[a-zA-Z0-9._%+-.]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'
    for fila in reader:
        if re.search(email_regex,fila[0]):
            print(f"correo electronico valido: {fila[0]}")
            correos.append(crearCuenta(fila[0]))
        else:
            print(f"cuenta no valida: {fila[0]}")
    
    archivo.close()