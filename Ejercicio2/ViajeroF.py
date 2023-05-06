##Clase
class ViajeroFrecuente:     
    __num_viajero: 0
    __dni = ""
    __nombre = ""
    __apellido = ""
    __millas_acum = 0
    #Constructor - Item a
    def __init__(self, num_viajero, dni, nombre, apellido, millas_acum):
        self.__num_viajero = num_viajero
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    #Item b
    def cantidadTotaldeMillas(self):
        return self.__millas_acum
    #Item C
    def acumularMillas(self, millas_recorridas):
        return self.__millas_acum + millas_recorridas;
    #Item d
    def canjearMillas(self, millas_Pcanjear):
        if self.__millas_acum < millas_Pcanjear:
            print("Número de millas erróneas, tiene que ingresar un numero igual o menor a {self.__millas_acum}")
        else:
            self.__millas_acum = self.__millas_acum - millas_Pcanjear
            print("Canje exitoso, quedan {self.__millas_acum} para canjear")
            return self.__millas_acum