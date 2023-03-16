# ej_7
class Persona:
    def __init__(self, nombre=None, edad=None, dni=None):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # GETTERS
    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    @property
    def dni(self):
        return self.__dni

    # SETTERS
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @edad.setter
    def edad(self, edad):
        self.__edad = edad

    @dni.setter
    def dni(self, dni):
        self.__dni = dni

    # METODOS
    def mostrar(self):
        print(f"Nombre: {self.__nombre} Edad: {self.__edad} dni: {self.__dni}")

    def Es_mayor_de_edad(self):
        return True if self.__edad >= 18 else False

    def __str__(self):
        return f"Nombre: {self.__nombre} Edad: {self.__edad} dni: {self.__dni}"


class Cuenta:
    def __init__(self, titular=None, cantidad=None):
        self.__titular = titular
        self.__cantidad = cantidad

    # GETTERS
    @property
    def titular(self):
        return self.__titular

    @property
    def cantidad(self):
        return self.__cantidad

    # SETTERS
    @titular.setter
    def titular(self, titular):
        self.__titular = titular

    @cantidad.setter
    def cantidad(self, cantidad):
        self.__cantidad = cantidad

    # METODOS
    def mostrar(self):
        print(f"Titular:  {self.__titular} Cantidad: {self.__cantidad}")

    def ingresar(self, cantidad):
        if cantidad < 0:
            pass
        else:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


p = Persona
p1 = Persona("Beto", 16, 33000000)
p1.mostrar()

p2 = Persona("Ana", 23, 33000000)

c = Cuenta(p2, 30000)

c.titular = p2

print("Titular: ", c.titular)
print("Cantidad: ", c.cantidad)

c.titular = p1

c.mostrar()
c.cantidad = 20000

print("Titular: ", c.titular, "Cantidad:", c.cantidad)

c.ingresar(5000)
c.mostrar()

c.ingresar(25000)
c.mostrar()

c.ingresar(-25000)
c.mostrar()

c.retirar(5000)
c.mostrar()

p2.mostrar()
print(p2.Es_mayor_de_edad())


# ej_8


class CuentaJoven(Cuenta):
    def __init__(self, titular=None, cantidad=None, bonificacion=None):
        super().__init__(titular, cantidad)
        self.__bonificacion = bonificacion

    # GETTERS
    @property
    def bonificacion(self):
        return self.__bonificacion

    # SETTERS
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion = bonificacion

    # METODOS
    def es_titular_valido(self):
        if 18 <= self.titular.edad < 25:
            return True
        else:
            return False

    def retirar(self, cantidad):
        if self.es_titular_valido():
            new_cant = self.cantidad - cantidad
            self.cantidad = new_cant
        else:
            return "No puede retirar dinero pq no es titular válido"

    def mostrar(self):
        return f"Cuenta Joven {self.bonificacion}%"


p3 = Persona("Mario", 16, 33000000)
j = CuentaJoven(p3, 100000, 30)

print(j.titular.edad)
print(j.bonificacion)

print(j.es_titular_valido())

print(j.cantidad)

j.retirar(50000)

print(j.cantidad)
print(j.mostrar())
