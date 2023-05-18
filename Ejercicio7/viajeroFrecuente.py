class ViajeroFrecuente:
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
    def __gt__ (self, otroViajero):
        if(self.__millas_acum > otroViajero.getTotalMillas()):
            milla_mayor = self.__millas_acum
        else:
            milla_mayor = otroViajero.getTotalMillas()
        return (milla_mayor)
    def __add__(self,millas):
        return (self.__millas_acum + millas)
    def __sub__(self,millas):
        return (self.__millas_acum - millas)
    def __eq__(self,millas):
        return self.__millas_acum == millas
    def getNumViajero(self):
        return self.__num_viajero 
    def getTotalMillas(self):
        return self.__millas_acum