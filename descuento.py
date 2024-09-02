class Fabrica:
    def __init__(self, llantas, color, precio):
        self.llantas = llantas
        self.color = color
        self.precio = precio

    def mostrar_atributos(self):
        return f"Llantas: {self.llantas}, Color: {self.color}, Precio: ${self.precio:,.2f}"

    def aplicar_descuento(self):
        if self.precio > 100000:
            self.precio *= 0.90  # Aplica un descuento del 10%

class Moto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=2, color=color, precio=precio)

class auto(Fabrica):
    def __init__(self, color, precio):
        super().__init__(llantas=4, color=color, precio=precio)

# Crear objetos de cada clase
moto = Moto(color="Rojo", precio=95000)
auto = auto(color="Azul", precio=120000)

# Aplicar descuentos si es necesario
moto.aplicar_descuento()
auto.aplicar_descuento()

# Mostrar atributos de cada objeto
print("Moto:")
print(moto.mostrar_atributos())

print("\auto:")
print(auto.mostrar_atributos())  