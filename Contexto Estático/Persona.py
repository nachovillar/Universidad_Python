class Persona():
    contador_persona = 0

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_persona += 1
        return cls.contador_persona

    def __init__(self, nombre, edad):
        self._id_persona = Persona.generar_siguiente_valor()
        self._nombre = nombre
        self._edad = edad

    def __str__(self):
        return f'Persona: {self.id_persona} Nombre: {self.nombre} Edad: {self.edad}'

    @property
    def id_persona(self):
        return self._id_persona

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

if __name__ == '__main__':
    persona1 = Persona('Juan', 20)
    print(persona1)

    persona2 = Persona('Andrés', 23)
    print(persona2)
