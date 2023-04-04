class Persona:
    contador=0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador +=1
    def __init__(self,nombre,edad):

        self.id_persona=Persona.generar_siguiente_valor()
        self.nombre=nombre
        self.edad=edad

    def __str__(self):
        return f"Persona [{self.id_persona}][{self.nombre}][{self.edad}]"

persona1 = Persona("Andres",23)
print(persona1)
persona2 = Persona("Raul",15)
print(persona2)
persona3 = Persona("Mario",19)
print(persona3)
print(f"Valor contador{Persona.contador}")
