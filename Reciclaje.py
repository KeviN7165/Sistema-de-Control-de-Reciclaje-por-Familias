from datetime import datetime
class MaterialesReciclados:
    def __init__(self, tipo, peso, fecha):
        self.tipo = tipo
        self.peso = peso
        self.fecha = datetime.strptime(fecha, '%Y-%m-%d')

    

       