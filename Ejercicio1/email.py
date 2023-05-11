class email:                        #Item a
    __idCuenta = ""
    __dominio = ""
    __tipoDominio = ""
    __contrasena = ""
    def __init__(self, idCuenta, dominio, tipoDominio, contrasena):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contrasena = contrasena
    def retornaEmail(self):         #Item b
        return self.__idCuenta +'@'+self.__dominio+'.'+self.__tipoDominio
    def getDominio(self):           #Item c
        return self.__dominio
    def modificarContra(self, contrasena):
        self.__contrasena = contrasena
        return self.__contrasena
    

