import csv 
from Registro import Registro

def mostrarMenu():
    print("""
        1.Ver fecha y hora del mayor y menor valor por cada variable
        2.Ver temperatura promedio mensual por cada hora
        3.Mostrar valores por hora del dia a ingresar
    """)

if __name__=='__main__':
    with open('variables.csv', 'r') as archivo:
        registros = []
        for linea in archivo:
            valores = linea.strip().split(';')
            registro = Registro(float(valores[2]), float(valores[3]), float(valores[4]))
            dia = int(valores[0])
            hora = int(valores[1])
            if len(registros) < dia:
                registros.append([])
            if len(registros[dia-1]) < hora:
                registros[dia-1].append([])
            registros[dia-1][hora-1].append(registro)
    
    print(registros)
         
    mostrarMenu()   
    num = int(input("Ingrese la opcion deseada: "))
    while num != 0:
        match num:
            case 1:
                i = 0
                while i<len(registros):
                    variables = [temperatura, humedad, presion]
                    for i in range(6):
                        minimo = min(variables)
                        # maximo = registros[var].idxmax()
                        print("Variable:", variables)
                        print(f"Mínimo valor:{minimo}")
                #print("Máximo valor:", registros[maximo])
                break
            case 2:
                
                break
            case 3:
                dia = int(input("Ingrese dia: "))
                
                break
            case default:
                break