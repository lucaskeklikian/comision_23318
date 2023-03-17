from ej_7_8_classes import Persona, Cuenta,CuentaJoven

#----------------Test clases ej_7-----------------------------------------------
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

#----------------Test clases ej_8-----------------------------------------------

p3 = Persona("Mario", 16, 33000000)
j = CuentaJoven(p3, 100000, 30)

print(j.titular.edad)
print(j.bonificacion)

print(j.es_titular_valido())

print(j.cantidad)

j.retirar(50000)

print(j.cantidad)
print(j.mostrar())
