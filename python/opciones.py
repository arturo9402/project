def hola(nombre="mundo"):
    print("hola", nombre)
hola("arturo")
hola()
class animal:
    """docstring for ClassName"""
    def __init__(self,patas=4, tipo="pequeñp"):
        self.patas = patas
        self.tipo = tipo
        
class perro(animal):
    def __init__(self, nombre="oddy", raza="jack"):
        self.nombre = nombre
        self.raza = raza
    #def saludo(self):
        #return "te saluda %s" % self.nombre    

perrito = perro( nombre="botas",raza= "labrador" )
perrito_juan = perro()
print(perrito.nombre)
print(perrito.raza)
#print(perrito.tipo)
#print(perrito.patas)
#perrito.saludo
print(perrito_juan.nombre)
print(perrito_juan.raza)
#print(perrito_juan.tipo)
#print(perrito_juan.patas)
#perrito_juan.saludo

