class Registro:
    def __init__(self, temperatura: float, humedad: float, presion: float):
        self .temperatura = temperatura
        self.humedad = humedad
        self .presion = presion
    def mostrar_menor_mayor(self, temperatura, humedad, presion):
        variables = [temperatura, humedad, presion]
        for var in variables:
            minimo = min(var)
           # maximo = registros[var].idxmax()
            print("Variable:", var)
            print(f"Mínimo valor:{minimo}")
            #print("Máximo valor:", registros[maximo])
        return minimo 
    def temperatura_promedio(datos):
        temperatura_promedio = datos.groupby(["hora"])["temperatura"].mean()
        print("Temperatura promedio mensual por cada hora:")
        print(temperatura_promedio)
    def listar_valores_por_hora(datos, num_dia):
        datos_dia = datos[datos["dia"] == num_dia]
        datos_dia = datos_dia.set_index("hora")
        print("Valores para el día", num_dia)
        print(datos_dia[["temperatura", "humedad", "presion"]])
