#ej_7
class Persona():
     def __init__(self,nombre,edad,dni):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

     def get_nombre(self):
         return self.__nombre
     
     def get_edad(self):
         return self.__edad
     
     def get_dni(self):
         return self.__dni
     
     def set_nombre(self, nombre):
         self.__nombre = nombre

     def set_edad(self, edad):
         self.__edad = edad
     
     def set_dni(self, dni):
         self.__dni = dni   

     def mostrar(self):
         print(f"Nombre: {self.__nombre} Edad: {self.__edad} dni: {self.__dni}")
     
     def Es_mayor_de_edad(self):
         return True if self.__edad >= 18 else False
     
     def __str__(self):
        return (f"Nombre: {self.__nombre} Edad: {self.__edad} dni: {self.__dni}")   
 


class Cuenta:
    def __init__(self, titular:Persona, cantidad:float):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular
    
    def get_cantidad(self):
        return self.__cantidad
    
    def set_titular(self,titular:Persona):
        self.__titular = titular
    
    def set_cantidad(self,cantidad):
        self.__cantidad = cantidad

    def mostrar(self):
        print(f"Titular:  {self.__titular} Cantidad: {self.__cantidad}")

    def ingresar(self,cantidad):
        if cantidad < 0:
            pass
        else: 
            self.__cantidad += cantidad
    
    def retirar(self,cantidad):
        self.__cantidad -= cantidad

    

p1 = Persona("Beto",16,33000000)
p1.mostrar()

p2 = Persona("Ana",23,33000000)

c = Cuenta(p2,30000)

c.set_titular(p2)

print("Titular: ",c.get_titular())
print("Cantidad: ",c.get_cantidad())

c.set_titular(p1)

c.mostrar()
c.set_cantidad(20000)

print("Titular: ",c.get_titular(),"Cantidad:",c.get_cantidad())

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


#ej_8

class CuentaJoven(Cuenta):
    
    def __init__(self, titular:Persona, cantidad:float, bonificacion:float):
         super().__init__(titular, cantidad)
         self.__bonificacion = bonificacion

    def get_bonificacion(self):
        return self.__bonificacion
    
    def set_bonificacion(self,bonificacion):
        self.__bonificacion = bonificacion

    def es_titular_valido(self):
        if 18 <= self.get_titular().get_edad() < 25:
            return True
        else:
            return False
    def retirar(self,cantidad):
        if self.es_titular_valido():
            new_cant = self.get_cantidad()-cantidad
            self.set_cantidad(new_cant)
        else:
            return "No puede retirar dinero pq no es titular válido"
    def mostrar(self):
        return f"Cuenta Joven {self.get_bonificacion()}%"

       
p3 = Persona("Mario",23,33000000)
j = CuentaJoven(p3,100000,30)

print(j.get_titular().get_edad())
print (j.get_bonificacion())

print(j.es_titular_valido())
print(j.get_cantidad())
print(j.retirar(50000))
print(j.get_cantidad())
print(j.mostrar())