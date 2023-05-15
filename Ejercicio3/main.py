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
            temperatura = float(valores[2])
            presion = float(valores[3])
            humedad = float(valores[4])
            # Crear una instancia de la clase Registro con los valores leídos
            registro = Registro(temperatura, presion, humedad)
            dia = int(valores[0])
            hora = int(valores[1])
            if len(registros) < dia:
                registros.append([])
            if len(registros[dia-1]) < hora:
                registros[dia-1].append([])
            registros[dia-1][hora-1].append(registro)
    
    print(registros)
    # Imprimir la cabecera de la tabla
    print("| Día | Hora | Temperatura | Presión | Humedad |")
    print("-" * 50)

    # Recorrer la lista bidimensional y agregar cada registro a la tabla
    for dia, registros_dia in enumerate(registros, start=1):
        for hora, registros_hora in enumerate(registros_dia, start=1):
            for registro in registros_hora:
                # Imprimir una fila de la tabla con los datos del registro
                print(f"   {dia}     {hora}        {registro.getTemperatura()}        {registro.getPresion()}      {registro.getHumedad()}")
         
    mostrarMenu()   
    num = int(input("Ingrese la opcion deseada: "))
    while num != 0:
        match num:
            case 1:
                # Variables auxiliares para almacenar los valores mínimos y máximos de cada variable
                temp_min = float('inf')  # Iniciamos con un valor muy alto
                temp_max = float('-inf')  # Iniciamos con un valor muy bajo
                pres_min = float('inf')
                pres_max = float('-inf')
                hum_min = float('inf')
                hum_max = float('-inf')

                # Variables para almacenar los días y horas correspondientes a los valores mínimos y máximos
                temp_min_dia = temp_max_dia = pres_min_dia = pres_max_dia = hum_min_dia = hum_max_dia = -1
                temp_min_hora = temp_max_hora = pres_min_hora = pres_max_hora = hum_min_hora = hum_max_hora = -1

                # Recorremos la lista bidimensional "registros"
                for dia, registros_dia in enumerate(registros):
                    for hora, registros_hora in enumerate(registros_dia):
                        for registro in registros_hora:
                            # Comparamos los valores de temperatura
                            if registro.getTemperatura() < temp_min:
                                temp_min = registro.getTemperatura()
                                temp_min_dia = dia + 1
                                temp_min_hora = hora + 1
                            if registro.getTemperatura() > temp_max:
                                temp_max = registro.getTemperatura()
                                temp_max_dia = dia + 1
                                temp_max_hora = hora + 1
                            # Comparamos los valores de presión
                            if registro.getPresion() < pres_min:
                                pres_min = registro.getPresion()
                                pres_min_dia = dia + 1
                                pres_min_hora = hora + 1
                            if registro.getPresion() > pres_max:
                                pres_max = registro.getPresion()
                                pres_max_dia = dia + 1
                                pres_max_hora = hora + 1
                            # Comparamos los valores de humedad
                            if registro.getHumedad() < hum_min:
                                hum_min = registro.getHumedad()
                                hum_min_dia = dia + 1
                                hum_min_hora = hora + 1
                            if registro.getHumedad() > hum_max:
                                hum_max = registro.getHumedad()
                                hum_max_dia = dia + 1
                                hum_max_hora = hora + 1

                # Imprimimos los resultados
                print("Temperatura:")
                print(f"Día y hora de mínimo valor: {temp_min_dia}/{temp_min_hora}")
                print(f"Día y hora de máximo valor: {temp_max_dia}/{temp_max_hora}")
                print("Presión:")
                print(f"Día y hora de mínimo valor: {pres_min_dia}/{pres_min_hora}")
                print(f"Día y hora de máximo valor: {pres_max_dia}/{pres_max_hora}")
                print("Humedad:")
                print(f"Día y hora de mínimo valor: {hum_min_dia}/{hum_min_hora}")
                print(f"Día y hora de máximo valor: {hum_max_dia}/{hum_max_hora}")
                break
            case 2:
                # Crear un diccionario para almacenar la suma de las temperaturas y la cantidad de registros por cada hora
                temp_por_hora = {hora: {'suma_temperatura': 0, 'cantidad_registros': 0} for hora in range(24)}

                # Recorrer la lista de registros
                for dia in registros:
                    for hora, registros_en_hora in enumerate(dia):
                        # Calcular la suma de las temperaturas y la cantidad de registros en la hora actual
                        suma_temperatura = sum([registro.getTemperatura() for registro in registros_en_hora])
                        cantidad_registros = len(registros_en_hora)
                        # Actualizar el diccionario con la suma de las temperaturas y la cantidad de registros por hora
                        temp_por_hora[hora]['suma_temperatura'] += suma_temperatura
                        temp_por_hora[hora]['cantidad_registros'] += cantidad_registros

                # Calcular el promedio de temperatura por hora
                for hora, datos_hora in temp_por_hora.items():
                    promedio_temperatura = datos_hora['suma_temperatura'] / datos_hora['cantidad_registros']
                    print(f"Temperatura promedio en la hora {hora}: {promedio_temperatura:.2f}")
                break
            case 3:
                dia = int(input("Ingrese dia: "))
                
                break
            case default:
                break