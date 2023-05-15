class Registro:
    def __init__(self, temperatura: float, presion: float, humedad: float):
        self.__temperatura = temperatura
        self.__presion = presion
        self.__humedad = humedad
    def __str__(self):
        return {self.__temperatura, self.__presion, self.__humedad}
    def __repr__(self):
        return f"{self.__temperatura, self.__presion, self.__humedad}"
    def mostrar_menor_mayor(self):
        return 0
    def getTemperatura(self):
        return self.__temperatura
    def getPresion(self):
        return self.__presion
    def getHumedad(self):
        return self.__humedad
    def temperatura_promedio(datos):
        temperatura_promedio = datos.groupby(["hora"])["temperatura"].mean()
        print("Temperatura promedio mensual por cada hora:")
        print(temperatura_promedio)
    def listar_valores_por_hora(datos, num_dia):
        datos_dia = datos[datos["dia"] == num_dia]
        datos_dia = datos_dia.set_index("hora")
        print("Valores para el día", num_dia)
        print(datos_dia[["temperatura", "humedad", "presion"]])
