class produc:
    def __init__(self, nombre,precio):
        self.nombre= nombre
        self.precio= precio

productos=[
    produc("macbook",23000),
    produc("telefono samsung", 1000),
    produc("tablet",3500),
    produc("smarwatch",2000),
    produc("mouse",200)
]
productos.sort(key=lambda x: x.precio)
for produc in productos:
    print(f"nombre: {produc.nombre} , precio: {produc.precio}")
            