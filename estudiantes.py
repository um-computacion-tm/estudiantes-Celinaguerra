
#ESTO ES UNA CLASE

class Persona:
    def __init__(self, param_nombre,param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0

    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def asistencia_clase(self):
        self.asistencia += 1


class Profesor(Persona):
    #contructor
    def __init__(self,param_nombre, param_email, param_numprof):      #con def se definen método
        self.numprof = param_numprof
        super().__init__(param_nombre, param_email)

class Alumno(Persona):
    def __init__(self,param_nombre, param_email, param_carrera, param_legajo):
        self.carrera = param_carrera
        self.legajo = param_legajo
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)

    def cambiar_carrera(self, nuevacarrera):
        self.carrera = nuevacarrera

    def cursando(self, materia):
        self.materias_cursando.append(materia)


class Materia:
    def __init__(self,cod_mat, param_nombre, param_carga):
        self.codmat = cod_mat
        self.nombre = param_nombre
        self.carga = param_carga



#ESTO ES UN OBJETO

profe_walter = Profesor("Walter", "walter.um", "0034")
print(profe_walter.nombre)
print(profe_walter.email)
print(profe_walter.numprof)

profe_daniel = Profesor("Daniel", "daniel.um", "0010")
print(profe_daniel.nombre)
print(profe_daniel.email)
print(profe_daniel.numprof)

alumno_celi = Alumno("Celi", "celiguerra.um", "informatica", "62157")
print(alumno_celi.nombre)
print(alumno_celi.email)
print(alumno_celi.carrera)
print(alumno_celi.legajo)

alumno_sofi = Alumno("Sofi", "sofisoler.um", "informatica", "62911")
print(alumno_sofi.nombre)
print(alumno_sofi.email)
print(alumno_sofi.carrera)
print(alumno_sofi.legajo)





print(alumno_celi.email)

print(alumno_sofi.carrera)


nuevacarrera = str(input("Elige una carrera: "))
alumno_sofi.cambiar_carrera(nuevacarrera)
print(alumno_sofi.carrera)

materia = str(input("Que materia estas cursando?: "))
alumno_celi.cursando(materia)
print(alumno_celi.cursando)


"""profesor_pepe = Profesor("Pepe")
profesor_walter = Profesor("Walter")
profesor_gabriel = Profesor("Gabriel")

print(id(profesor_pepe))
print(profesor_pepe.nombre)

print(id(profesor_walter))
print(profesor_walter.nombre)

print(id(profesor_gabriel))
print(profesor_gabriel.nombre)"""

"""profesor_pepe = Profesor("Pepe", "jopepe@um.ar")
print(id(profesor_pepe))
print(profesor_pepe.nombre)
print(profesor_pepe.email)

print("su asistencia es: ")
print(profesor_pepe.asistencia)

print("el profesor fue a clase")
profesor_pepe.asistencia_clase()        #esto suma una asistencia
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()
profesor_pepe.asistencia_clase()

print("su asistencia es: ")
print(profesor_pepe.asistencia)"""

"""profesor_pepe.cambiar_nombre("Juancito")
print(profesor_pepe.nombre)

profesor_pepe.cambiar_nombre("mario")
print(profesor_pepe.nombre)
print(profesor_pepe.email)"""

