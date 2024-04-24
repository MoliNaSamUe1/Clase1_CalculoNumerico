class Persona:
    def __init__(self,nombre="",cedula="",edad=0):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad

    def mayorEdad(self):
        if(self.edad >= 18):
            return True
        else:
            return False
        
    def getNombre(self):
        return self.nombre 
    
    def getCedula(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def setNombre(self,name):
        self.nombre = name
        
    def setCedula(self,ide):
        self.cedula = ide

    def setEdad(self,years):
        self.edad = years        

        

def mostrar(matriz):
    for i in range(len(matriz)):
        print(matriz[i][0]," es mayor de edad: ",matriz[i][3])


filas = int(input("Ingrese el numero de personas: "))
matriz = [[None]*4 for i in range(filas)]
for j in range(filas):
    nombre = input("Ingrese el nombre: ")
    cedula = input("Ingrese la cedula: ")
    edad = int(input("Ingrese la edad: "))
    print("")
    persona = Persona(nombre,cedula,edad)
    matriz[j][0] = nombre
    matriz[j][1] = cedula
    matriz[j][2] = edad
    matriz[j][3] = persona.mayorEdad()

mostrar(matriz)