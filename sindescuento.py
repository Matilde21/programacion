# crear una clase fabrica que tenga los atributos llantas, color y precio; Luego crear 2 clases mas que hereden de fabrica las cuales son moto y carro.
# crear metodos que muestren la cantidad de llantas, color y precios de cada transporte. 
# Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno

class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_info(self):
        print(f"Llantas: {self.llantas}, Color: {self.color}, Precio: {self.precio}")

class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(2, color, precio)

class auto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(4, color, precio)


moto = Moto("Rojo", 1500)
auto = Auto("Azul", 20000)

print("Información de la moto:")
moto1.mostrar_info()

print("Información del carro:")
auto.mostrar_info()