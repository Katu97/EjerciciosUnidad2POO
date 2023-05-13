class Ventana:
    __titulo: str
    __x_vsi: 0
    __y_vsi: 0
    __x_vid: 50
    __y_vid: 50
    #Constructor
    def __init__(self, titulo: str, x_vsi: float, y_vsi: float, x_vid: float, y_vid: float):
        self.__titulo = titulo
        self.__x_vsi = x_vsi
        self.__y_vsi = y_vsi
        self.__x_vid = x_vid
        self.__y_vid = y_vid
    def __str__ (self):
        return f"({self.__titulo, self.__x_vsi, self.__y_vsi, self.__x_vid, self.__y_vid})"
    def __repr__ (self):
        return f"({self.__titulo, self.__x_vsi, self.__y_vsi, self.__x_vid, self.__y_vid})"
    def getTitulo(self):
        return self.__titulo
    def alto(self):
        return (self.__y_vid - self.__y_vsi)
    def ancho(self):
        return (self.__x_vid - self.__x_vsi)
    def mostrar(self):
        return f"(X del vertice superior izquierdo = {self.__x_vsi}; Y del vertice superior izquiero = {self.__y_vsi}; X del vertice inferior derecho = {self.__x_vid}; Y del vertice inferior derecho = {self.__y_vid})"
    def moverDerecha(self, numero):
        x = self.__x_vid + numero
        if x < 500:
            self.__x_vid = x
            self.__x_vsi = self.__x_vsi + numero            
        else:
            print(f"No se puede mover {numero} pasos a la derecha")
    def moverIzquierda(self, numero):
        x = self.__x_vsi - numero
        if x >= 0:
            self.__x_vsi = x
            self.__x_vid = self.__x_vid - numero
        else:
            print(f"No se puede mover {numero} pasos a la izquierda")
    def bajar(self, numero):
        x = self.__y_vid + numero
        if x < 500:
            self.__y_vid = x
            self.__y_vsi = self.__y_vsi + numero            
        else:
            print(f"No se puede mover {numero} pasos hacia abajo")
    def subir(self, numero):
        x = self.__y_vsi - numero
        if x >= 0:
            self.__y_vsi = x
            self.__y_vid = self.__y_vid - numero
        else:
            print(f"No se puede mover {numero} pasos hacia arriba")    
        
if __name__ ==  '__main__':
    print('==== Ventana Inicio ====')
    ventanaInicio = Ventana('Inicio')
    ventanaInicio.mostrar()
    print('Ventana: {} Alto: {} Ancho: {}'.format(ventanaInicio.getTitulo(),ventanaInicio.alto(),ventanaInicio.ancho()))
    print('==== Ventana Cargar ====')
    ventanaCargar = Ventana('Cargar',10,20)
    ventanaCargar.mostrar()
    print('*** Mueve a la derecha ***')
    ventanaCargar.moverDerecha(10)
    ventanaCargar.mostrar()
    print('*** Mueve a la izquierda ***')
    ventanaCargar.moverIzquierda(10)
    ventanaCargar.mostrar()
    print('*** Bajar ***')
    ventanaCargar.bajar(10)
    ventanaCargar.mostrar()
    print('==== Ventana Borrar ====')
    ventanaBorrar = Ventana('Borrar', 10, 20, 100, 200)
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir(5)   
    ventanaBorrar.mostrar()
    print('*** Subir ***')
    ventanaBorrar.subir()
    ventanaBorrar.mostrar()
    print('*** Bajar ***')
    ventanaBorrar.bajar()
    ventanaBorrar.mostrar()