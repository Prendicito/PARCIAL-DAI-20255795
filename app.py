from dataclasses import dataclass

estado_registro = "activo"

if estado_registro == "CUENTA_SUSPENDIDA":
    exit

@dataclass 
class RegistroAtencion():
    def __init__(self, id_registro: str, id_alumno: str, recursos: list, nombre_empleado: str, codigo_usuario: str):
        self.id_registro = id_registro
        self.id_alumno = id_alumno
        self.__recursos = []
        self.nombre_empleado = nombre_empleado
        self.codigo_usuario = codigo_usuario
        self.bibliotecario = bibliotecario

        bibliotecario = {"Id": codigo_usuario,"Nombre":nombre_empleado}

    def Registrar_Atencion(self):
        print(
            f"""Id de registro: {self.id_registro}
              Alumno Registrado: {self.id_alumno} 
              Recursos a disposicion: {self.recursos}
              Id Bibliotecario encargado: {self.codigo_usuario}
              Nombre de Bibliotecarioe ncargado: {self.nombre_empleado}""")




class Recurso(RegistroAtencion):
    def __init__(self, id_registro: str, id_alumno: str, recursos: list, nombre_empleado: str, codigo_usuario: str, id_recurso: str, tiempo_retraso: int,lista_espera:list):
        super().__init__(id_registro, id_alumno, recursos, nombre_empleado, codigo_usuario)

        self.id_recurso = id_recurso
        self.tiempo_retraso = tiempo_retraso
        self.lista_espera = []

        if recursos.count > 4:
            raise ValueError("Limite de recursos por atencion alcanazado")
        
        if self.lista_espera >10 :
            estado_registro = "CUENTA_SUSPENDIDA"


   
    
   
    def calcular_multa(self):
        multa_total = 0 
        for recurso in self.__recursos[Recurso]:
            if recurso == "PrestamoLibro":
                multa_total = multa_total + (2.50 * self.tiempo_retraso)

            if recurso == "UsoSalaEstudio":
                multa_total = multa_total + (self.tiempo_retraso * self.lista_espera.count)
            
        print(f"Su multa total es de ${multa_total}")

    
    
            

    








