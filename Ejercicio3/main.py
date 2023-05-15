import csv 
from Registro import Registro

def mostrarMenu():
    print("""
        1.Mostrar mayor y menor
        2.Ver temperatura Promedio
        3.Mostrar valores por hora
    """)

if __name__=='__main__':
    registros = []
    archivo = open('variables.csv') 
    reader = csv.reader(archivo, delimiter = ';')
    for fila in reader:
        dia = int(fila[0])
        hora = int (fila[1])
        temperatura = float(fila[2])
        humedad = int(fila[3])
        presion = int(fila[4])
        registro = Registro(temperatura, humedad, presion)
        registros.append([dia, hora, temperatura, humedad, presion])
    print(registros)
       
    mostrarMenu()
    num=int(input("Ingrese la opcion deseada:"))
    while num !=0:
        match num:
            case 1:
                i=0
                while i<len(registros):
                    variables = [temperatura,humedad, presion]
                    for i in range(6):
                        minimo = min(variables)
                        # maximo = registros[var].idxmax()
                        print("Variable:", variables)
                        print(f"Mínimo valor:{minimo}")
            #print("Máximo valor:", registros[maximo])