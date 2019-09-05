class Agenda():
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
     
Dato = Agenda('Reinaldo', 'Python', '0418-5554411')

print(Dato.nombre, Dato.apellido, Dato.telefono, sep = ' ')
