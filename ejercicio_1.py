# numero = 50
# if type(numero) == int:
#     print("Respuesta:", numero * 2)
# else:
#     print("Este dato no es numérico.")

# def mensaje(hombre):
#     print(hombre)


# mensaje("")
# mensaje("Mi primer programa. ")
# mensaje("Mi segundo programa. ")


# class Sintaxis:
#     def usoVariables(self):
#         edad, _peso = 50, 70.50
#         print("Edad: {}\nPeso: {}".format(edad, _peso))

# ejercicio1 = Sintaxis()
# ejercicio1.usoVariables()


# class Sintaxis:
#     instancia = 0
#     def __init__(self, dato = "Iniciando..."):
#         self.frase = dato

#     def usoVariables(self):
#         edad, _peso = 25, 57.8
#         nombre = "Sandy Diaz"
#         tipoSexo = "Femenino"
#         civilSoltera = False
#         print("Nombre: {}\nEdad: {}".format(nombre, edad))
#         print("Tipo de Sexo: {}\nEstado Civil Soltera: {}".format(tipoSexo, civilSoltera))
#         print("Peso: {}Kg".format(_peso))

# ejercicio1 = Sintaxis()
# print(ejercicio1.frase)
# ejercicio1.usoVariables()


class Sintaxis:
    instancia = 0
    def __init__(self, dato = "Iniciando..."):
        self.frase = dato

    def usoVariables(self):
        edad, _peso = 25, 57.8
        nombre = "Sandy Diaz"
        tipoSexo = "Femenino"
        civilSoltera = False
        # print("Nombre: {}\nEdad: {}".format(nombre, edad))
        # print("Tipo de Sexo: {}\nEstado Civil Soltera: {}".format(tipoSexo, civilSoltera))
        # print("Peso: {}Kg".format(_peso))
        
        #TUPLA
        usuario = ()
        usuario = ("Sandy1996", 5648, "sdiazo@unemi.edu.ec", False)
        
        # LISTA
        materias = []
        materias = ["Programacion Web", "PHP", "Angular"]
        materias[1] = "Python"
        materias.append("Go")

        # DICCIONARIO
        docente = {}
        docente = {"Nombre": "Esther", "Edad": 30, "Fac.": "FACI"}
        docente["Carrera"] = "CS"
        
        # FORMAT
        # print("""Mi nombre es {}, tengo {}
        #          años""".format(nombre, edad))

        print(usuario, materias, docente)
        print(usuario, usuario[0], usuario[0:2], usuario[-1])
        print(materias, materias[2:], materias[:1], materias[::], materias[-2:])
        print(docente, docente["Nombre"])
