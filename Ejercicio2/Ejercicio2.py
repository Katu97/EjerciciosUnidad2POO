import csv
#from ViajeroF import ViajeroFrecuente

#Clase
class ViajeroFrecuente:     
    __num_viajero: 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0
    #Constructor - Item a
    def __init__(self, num_viajero: int, dni: int , nombre: str, apellido:str , millas_acum: int):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    def __str__(self) -> str:
        return f"{self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum}"
    def __repr__(self) -> str:
        return f"{self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum}"
    def get_numero(self):
        return self.__num_viajero
    #Item b
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    #Item C
    def acumularMillas(self, millas_agregar):
        self.__millas_acum = int(self.__millas_acum) + millas_agregar
        return self.__millas_acum
    #Item d
    def canjearMillas(self, millas_Pcanjear: int) -> int | None:
        if (self.__millas_acum < millas_Pcanjear):
            print(f"Número de millas erróneas, tiene que ingresar un numero igual o menor a {self.__millas_acum}")
        else:
            self.__millas_acum = self.__millas_acum - millas_Pcanjear
            print(f"Canje exitoso, quedan {self.__millas_acum} para canjear")
            return int(self.__millas_acum)

def Menu():
	print("""
        1 - Consultar Cantidad de millas
        2 - Acumular millas
        3 - Canjear millas
    """)

if __name__ == "__main__":
    listaViajeros = []
    viajero = []
    archivo = open('listaViajeros.csv')
    reader = csv.reader(archivo, delimiter = ";")
    for fila in reader:
        viajero = ViajeroFrecuente(fila[0], fila[1], fila[2], fila[3], int(fila[4]))
        listaViajeros.append(viajero)
    archivo.close()
    
    #PUNTO 2
    num_Vfrecuente = input("Ingrese un numero de viajero frecuente: ")
    Menu()
    opc = int(input("Ingrese opcion elegida: "))
    while opc != 0:
        match opc:
            case 1:
                i = 0
                bandera = True
                while ((i < len(listaViajeros)) and bandera):
                    if listaViajeros[i].get_numero() == num_Vfrecuente:
                        bandera = False
                    i += 1
                if i >= len(listaViajeros):
                    print("No se encontró el viajero ingresado")
                else:
                    print(f"Cantidad de millas acumuladas del viajero ingresado: {listaViajeros[i-1].cantidadTotaldeMillas()}")
                break
            case 2:
                i = 0
                bandera = True
                while ((i < len(listaViajeros)) and bandera):
                    if listaViajeros[i].get_numero() == num_Vfrecuente:
                        bandera = False
                    i += 1
                if i >= len(listaViajeros):
                    print("No se encontró el viajero ingresado")
                else:
                    millasAagregar = int(input("Ingrese cantidad de millas a agregar: "))
                    listaViajeros[i-1].acumularMillas(millasAagregar)
                    print(f"Cantidad de millas actualizas: {listaViajeros[i-1].cantidadTotaldeMillas()}")                        
                break
            case 3:
                i = 0
                bandera = True
                while ((i < len(listaViajeros)) and bandera):
                    if listaViajeros[i].get_numero() == num_Vfrecuente:
                        bandera = False
                    i += 1
                if i >= len(listaViajeros):
                    print("No se encontró el viajero ingresado")
                else:
                    millasAcanjear = int(input("Ingrese cantidad de millas a canjear: "))
                    listaViajeros[i-1].canjearMillas(millasAcanjear)                        
                break
            case default:
                Menu()


