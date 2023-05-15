class perro:
    def __init__(self, temperatura, presion, humedad):
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
    def __str__(self) -> str:
        return f"{self.temperatura, self.presion, self.humedad}"
    def __repr__(self) -> str:
        return f"{self.temperatura, self.presion, self.humedad}"

if __name__=='__main__': 
    registros = []
    for dia in range(1, 32):
        filas = []
        for hora in range(24):
            registro = perro(0, 0, 0)  # valores por defecto para temperatura, presion y humedad
            print(registro)
            filas.append(registro)
        registros.append(filas)

    print(registros)