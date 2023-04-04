class Miclase:
    variable="Valor clase:"
    def __init__(self,variable_objecto):
        self.variable_objecto=variable_objecto

    @staticmethod
    def metodo_estatico():
        print(Miclase.variable)
    @classmethod
    def metodo_clase(cls):
        print(cls.variable)

    def metodo_objeto(self):
        self.metodo_clase()
        self.metodo_estatico()



print(Miclase.variable)
Miclase1 = Miclase("Valor variable objeto:")
MiObjeto=Miclase("Variable del objeto")
MiObjeto.metodo_clase()
MiObjeto.metodo_objeto()

