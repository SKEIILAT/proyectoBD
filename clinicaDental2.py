import pymysql

miConexion= pymysql.connect(host="localhost",user="root",passwd="",db="ClinicaDentalDB")
cur=miConexion.cursor()

def mostrarMenu():
    print("Bienvenid@")
    print("Menú de opciones")
    print("1. PACIENTES")
    print("2. DENTISTAS")
    print("3. ASISTENTE")
    print("4. CITA")
    print("5. TRATAMIENTO")
    print("6. HISTORIA CLÍNICA")


def mostrarOpciones_Pacientes():
    print("1. Añadir Paciente")
    print("2. Consultar la información de un Paciente")
    print("3. Editar la información de un Paciente")
    print("4. Eliminar registro de un Paciente")
    print("5. Regresar al menú principal")

def mostrarOpciones_Dentistas():
    print("1. Añadir Dentista")
    print("2. Consultar la información de un Dentista")
    print("3. Editar la información de un Dentista")
    print("4. Eliminar registro de un Dentista")
    print("5. Regresar al menú principal")

def mostrarOpciones_Asistentes():
    print("1. Añadir Asistente")
    print("2. Consultar la información de un Asistente")
    print("3. Editar la información de un Asistente")
    print("4. Eliminar registro de un Asistente")
    print("5. Regresar al menú principal")

def mostrarOpciones_HC():
    print("1. Añadir Historia Clínica")
    print("2. Consultar la información de una Historia Clínica")
    print("3. Editar la información de una Historia Clínica")
    print("4. Eliminar registro de una Historia Clínica")
    print("5. Regresar al menú principal")

def mostrarOpciones_Citas():
    print("1. Añadir Cita")
    print("2. Consultar la información de una Cita")
    print("3. Editar la información de una Cita")
    print("4. Eliminar registro de una Cita")
    print("5. Regresar al menú principal")

def mostrarOpciones_Tratamientos():
    print("1. Añadir Tratamiento")
    print("2. Consultar la información de un Tratamiento")
    print("3. Editar la información de un Tratamiento")
    print("4. Eliminar registro de un Tratamiento")
    print("5. Regresar al menú principal")

def mostrarTablaPacientes():
     cur.execute("select id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion from paciente ")
     print('-'*65+"TABLA DE PACIENTES"+'-'*65)
     print(F"|    id_paciente   |     nombre    |     apellido     |     telefono   |           email          |   fecha_nacimiento  |         direccion        |")
     for id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion in cur.fetchall():
            print("|%17d | %12s  | %15s  | %14s | %24s | %19s | %24s |" % (id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion))

mostrarMenu()
opcion=int(input("\nIngrese una opcion: "))
print()
while(1<=opcion<=3):
    if opcion==1:
       mostrarTablaPacientes()
       print()
       mostrarOpciones_Pacientes()
       opcionP=int(input("\nIngrese una opcion: "))
       print()
       while(1<=opcionP<=4):
        if opcionP==1:
            id=0
            nombre=input("Ingrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            telefono=input("Ingrese el teléfono: ")
            email=input("Ingrese el email: ")
            fecha_nac=input("Ingrese la fecha de nacimiento (año-mes-dia) : ")
            direccion=input("Ingrese la dirección: ")
            consulta = "INSERT INTO Paciente (nombre, apellido, telefono, email, fecha_nacimiento, direccion) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(consulta, (nombre, apellido, telefono, email, fecha_nac, direccion))
            miConexion.commit()
            mostrarTablaPacientes()

            opcionP=int(input("\nIngrese una opcion: "))
        """ 
        elif opcion2==2:
            nombre=input("Ingrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            for paciente,lista in pacientes.items():
            if (nombre in lista) and (apellido in lista) :
                fecha_nac=input("Ingrese la fecha de nacimiento (dia/mes/año) : ")
                pacientes[paciente][2]=fecha_nac
                email=input("Ingrese el email: ")
                pacientes[paciente][3]=email
                telefono=input("Ingrese el teléfono: ")
                pacientes[paciente][4]=telefono
                direccion=input("Ingrese la dirección: ")
                pacientes[paciente][5]=direccion
                opcion2=int(input("\nIngrese una opcion: "))
                
        elif opcion2==3:
            nombre=input("\nIngrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            for paciente,lista in pacientes.items():
            if (nombre in lista) and (apellido in lista) :
                print(F"Id_paciente: {paciente}")
                print(lista)
            opcion2=int(input("\nIngrese una opcion: "))
        else:
            break
        opcion=int(input("\nIngrese una opcion: "))
        """  


    elif opcion==2:
        print('-'*69+"TABLA DE DENTISTAS"+'-'*69)
        print(F"|    id_dentista   |     nombre    |    apellido      |     telefono   |           email          |      especialidad     |  hora_inicio   |    hora_fin   |")
        cur.execute("select id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin from dentista ")
        for id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin in cur.fetchall():
            print("|%17d | %12s  | %15s  | %14s | %24s | %21s | %14s |%14s |" % (id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin))
        opcion=int(input("\nIngrese una opcion: "))
        print()
        mostrarOpciones_Dentistas()

    elif opcion==3:
        print('-'*69+"TABLA DE ASISTENTES"+'-'*69)
        print(F"|    id_asistente   |    id_dentista   |     nombre     |    apellido      |     telefono   |")
        cur.execute("select id_asistente, id_identista, nombre, apellido, telefono from asistente ")
        for id_asistente, id_dentista, nombre, apellido, telefono in cur.fetchall():
            print("|%17d | %17d | %12s  | %15s  | %14s |" % (id_asistente, id_dentista, nombre, apellido, telefono))
        opcion=int(input("\nIngrese una opcion: "))
        print()
        mostrarOpciones_Asistentes()
    
    elif opcion==4:
        print('-'*69+"TABLA DE CITAS"+'-'*69)
        print(F"|  id_cita   |   id_paciente   |   id_historia   |   id_dentista   |   id_asistente   |   id_tratamiento   |   cita_fecha   |     estado     |    costo   |")
        cur.execute("select id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo FROM cita")
        for id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo in cur.fetchall():
            print("|%8d | %12d | %12d | %11d | %12d | %15d | %15s | %14s | %7.2f |" % (id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo))
        opcion=int(input("\nIngrese una opcion: "))
        print()
        mostrarOpciones_Citas()

"""""
        mostrarOpciones()
        opcion2=int(input("\nIngrese una opcion: "))
        while(1<=opcion2<=7):
            if opcion2==1:
                cur.execute("SELECT p.nombre, p.apellido, COUNT(c.id_cita) AS numero_de_citas FROM Paciente p JOIN Cita c ON p.id_paciente = c.id_paciente GROUP BY p.id_paciente ORDER BY numero_de_citas DESC")
                print(F"|    Nombre   |       Apellido      |   Numero_de_citas  |")
                for nombre, apellido, numero_de_citas in cur.fetchall():
                    print("|%12s | %19s | %19d|" % (nombre, apellido, numero_de_citas))
                print()
                opcion2=int(input("\nIngrese una opcion: "))
            elif opcion2==2:
                cur.execute("SELECT d.nombre, d.apellido, COUNT(c.id_dentista) AS cantidad_citas FROM Dentista d JOIN Cita c ON d.id_dentista = c.id_dentista GROUP BY d.id_dentista ORDER BY cantidad_citas DESC;")
                print(F"|    Nombre   |       Apellido      |   Cantidad_de_citas  |")
                for nombre, apellido, cantidad_citas in cur.fetchall():
                    print("|%12s | %19s | %21d|" % (nombre, apellido, cantidad_citas))
                print()
                opcion2=int(input("\nIngrese una opcion: "))
            elif opcion2==3:
                cur.execute("SELECT a.nombre, a.apellido, COUNT(DISTINCT a.id_dentista) AS cantidad_dentistas FROM Asistente a GROUP BY a.id_asistente ORDER BY cantidad_dentistas DESC;")
                print(F"|    Nombre   |       Apellido      |   Cantidad_dentistas  |")
                for nombre, apellido, cantidad_dentistas in cur.fetchall():
                    print("|%12s | %19s | %22d|" % (nombre, apellido, cantidad_dentistas))
                print()
                opcion2=int(input("\nIngrese una opcion: "))
            elif opcion2==4:
                cur.execute("SELECT t.nombre AS tratamiento, round(AVG(c.costo),2) AS costo_promedio FROM Tratamiento t JOIN Cita c ON t.id_tratamiento = c.id_tratamiento GROUP BY t.id_tratamiento ORDER BY costo_promedio DESC; ")
                print(F"|           Tratamiento         |       Costo_promedio     |")
                for tratamiento, costo_promedio in cur.fetchall():
                    print("|%30s | %24.2f |" % (tratamiento, costo_promedio))
                print()
                opcion2=int(input("\nIngrese una opcion: "))
            elif opcion2==5:
                cur.execute("SELECT estado, COUNT(id_cita) AS cantidad_citas FROM Cita GROUP BY estado;")
                print(F"|           Estado          |        Cantidad_citas    |")
                for estado, cantidad_citas in cur.fetchall():
                    print("|%26s | %24d |" % (estado, cantidad_citas))
                print()
                opcion2=int(input("\nIngrese una opcion: "))
            elif opcion2==6:
                cur.execute("SELECT p.nombre, p.apellido, COUNT(c.id_cita) AS cantidad_citas FROM Paciente p JOIN Cita c ON p.id_paciente = c.id_paciente GROUP BY p.id_paciente;")
                print(F"|    Nombre   |       Apellido      |   Cantidad_dentistas  |")
                for nombre, apellido, cantidad_citas in cur.fetchall():
                    print("|%12s | %19s | %22d|" % (nombre, apellido, cantidad_citas))
                print()
                opcion2=int(input("\nIngrese una opcion: "))
            elif opcion2==7:
                opcion2=0
                

            
        mostrarMenu()
        opcion=int(input("\nIngrese una opcion: "))    
    """
    elif opcion==4:
        opcion=0
        miConexion.close()
print("Saliendo....")


