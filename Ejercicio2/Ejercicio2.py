import csv
from ViajeroF import ViajeroFrecuente

def mostrarMenu():
	print("""
        1.Consultar Cantidad de millas
        2.Acumular millas
        3.Canjear millas
    """) 

if __name__ == "__main__":
    listaViajeros = []
    i = 0
    archivo = open('viajeros.csv')
    reader = csv.reader(archivo, delimiter = ";")
    for fila in reader:
        viajero = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], fila[4])
        listaViajeros.append(viajero)

    print(listaViajeros)
    
    
    
    archivo.close()        