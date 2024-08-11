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
    print("7. CONSULTAS")
    print("8. Regresar al menú principal")

def mostrarOpciones():
    print("Menú de opciones")
    print("1. Pacientes con el mayor número de citas")
    print("2. Dentistas con el mayor número de citas asignadas")
    print("3. Asistentes que trabajan con más dentistas")
    print("4. Tratamientos con el costo promedio más alto")
    print("5. Detalles de citas por estado")
    print("6. Número total de citas por paciente")
    print("7. Regresar al menú principal")

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

def mostrarTablaDentistas():
    print('-'*69+"TABLA DE DENTISTAS"+'-'*69)
    print(F"|    id_dentista   |     nombre    |    apellido      |     telefono   |           email          |      especialidad     |  hora_inicio   |    hora_fin   |")
    cur.execute("select id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin from dentista ")
    for id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin in cur.fetchall():
            print("|%17d | %12s  | %15s  | %14s | %24s | %21s | %14s |%14s |" % (id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin))

def mostrarTablaTratamiento():
    print('-'*69+"TABLA DE TRATAMIENTO"+'-'*69)
    print(F"|   id_tratamiento |    id_paciente    |           nombre          |                                 descripcion                             |    duracion_dias   |")
    cur.execute("select id_tratamiento, id_paciente, nombre, descripcion, duracion_dias FROM tratamiento")
    for id_tratamiento,id_paciente, nombre, descripcion, duracion_dias in cur.fetchall():
            print("|%17d | %17d |%25s  | %70s  | %18d |" %  (id_tratamiento, id_paciente,nombre, descripcion, duracion_dias))      

def mostrarTablaAsistentes():
    cur.execute("select id_asistente, id_dentista, nombre, apellido, email, telefono from asistente ")
    print('-' * 69 + "TABLA DE ASISTENTES" + '-' * 69)
    print(F"|    id_asistente   |    id_dentista    |     nombre     |    apellido      |            email          |    telefono     |")
    for id_asistente, id_dentista, nombre, apellido, email, telefono in cur.fetchall():
        print("|%18d | %17d | %13s  | %15s  | %25s | %15s |" % (id_asistente, id_dentista, nombre, apellido, email, telefono))


def mostrarTablaCitas():
    cur.execute(
        "select id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo FROM cita")
    print('-' * 69 + "TABLA DE CITAS" + '-' * 69)
    print(
        F"|  id_cita   |   id_paciente   |   id_historia   |   id_dentista   |   id_asistente   |   id_tratamiento    |      cita_fecha     |     estado     |    costo   |")
    cur.execute(
        "select id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo FROM cita")
    for id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo in cur.fetchall():
        print("|%11d | %15d | %15d | %15d | %16d | %19d | %15s | %14s | %10.2f |" % (
        id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo))


def mostrarTablaHC():
    print('-'*69 + "TABLA DE HISTORIAS CLÍNICAS" + '-'*69)
    print(F"| id_historia | id_paciente |                                                                             observaciones                                                              |")
    cur.execute("SELECT id_historia, id_paciente, observaciones FROM historia_clinica")
    for id_historia, id_paciente, observaciones in cur.fetchall():
            print("|%12d | %11d | %150s |" % (id_historia, id_paciente, observaciones))


mostrarMenu()
opcion=int(input("\nIngrese una opcion: "))
print()
while(1<=opcion<=8):
    if opcion==1:
       mostrarTablaPacientes()
       print()
       mostrarOpciones_Pacientes()
       opcionP=int(input("\nIngrese una opcion: "))
       print()
       while(1<=opcionP<=5):
        if opcionP==1:
        
            nombre=input("Ingrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            telefono=input("Ingrese el teléfono: ")
            email=input("Ingrese el email: ")
            fecha_nac=input("Ingrese la fecha de nacimiento (año-mes-dia) : ")
            direccion=input("Ingrese la dirección: ")
            #cur.execute(F"INSERT INTO Paciente (id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion) VALUES ({id},{nombre}, {apellido}, {telefono}, {email}, {fecha_nac}, {direccion})")
            consulta = "INSERT INTO Paciente (nombre, apellido, telefono, email, fecha_nacimiento, direccion) VALUES (%s, %s, %s, %s, %s, %s);"
            cur.execute(consulta, (nombre, apellido, telefono, email, fecha_nac, direccion))
            miConexion.commit()
            mostrarTablaPacientes()
            mostrarOpciones_Pacientes()

            opcionP=int(input("\nIngrese una opcion: "))
        
        elif opcionP==2:
            id=int(input("Ingrese el id del paciente a consultar: "))
            consulta=F"SELECT id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion FROM Paciente WHERE id_paciente = {id};"
            cur.execute(consulta)
            
            print('-'*65+"TABLA DE PACIENTES"+'-'*65)
            print(F"|    id_paciente   |     nombre    |     apellido     |     telefono   |           email          |   fecha_nacimiento  |         direccion        |")
            for id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion in cur.fetchall():
                print("|%17d | %12s  | %15s  | %14s | %24s | %19s | %24s |" % (id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion))
            
            mostrarOpciones_Pacientes()
            opcionP=int(input("\nIngrese una opcion: "))
               
        elif opcionP==3:
            id=int(input("Ingrese el id del paciente: "))
            nombre=input("Ingrese el nombre: ")
            apellido=input("Ingrese el apellido: ")
            telefono=input("Ingrese el teléfono: ")
            email=input("Ingrese el email: ")
            fecha_nac=input("Ingrese la fecha de nacimiento (año-mes-dia) : ")
            direccion=input("Ingrese la dirección: ")
            consulta=F"UPDATE Paciente SET nombre = %s, apellido = %s, telefono = %s, email = %s, fecha_nacimiento = %s, direccion = %s WHERE id_paciente = {id};"
            cur.execute(consulta,(nombre,apellido,telefono,email,fecha_nac,direccion))
            miConexion.commit()
            mostrarTablaPacientes()
            mostrarOpciones_Pacientes()
            opcionP=int(input("\nIngrese una opcion: "))
        
        elif opcionP==4:
            id=int(input("Ingrese el id del paciente a eliminar: "))
            consulta=F"DELETE FROM Paciente WHERE id_paciente = {id};"
            cur.execute(consulta)
            miConexion.commit()
            mostrarTablaPacientes()
            mostrarOpciones_Pacientes()
            opcionP=int(input("\nIngrese una opcion: "))
        
        elif opcionP==5:
            opcionP=0

            mostrarMenu()
            opcion=int(input("\nIngrese una opcion: "))    
        
        


    elif opcion==2:
        mostrarTablaDentistas()
        print()
        mostrarOpciones_Dentistas()
        opcionD=int(input("\nIngrese una opcion: "))
        print()
        while(1<=opcionD<=5):
            if opcionD==1:
                id=0
                nombre=input("Ingrese el nombre: ")
                apellido=input("Ingrese el apellido: ")
                telefono=input("Ingrese el teléfono: ")
                email=input("Ingrese el email: ")
                especialidad=input("Ingrese la especialidad : ")
                disponibilidad_inicio=input("Ingrese hora de inicio (XX:XX): ")
                disponibilidad_fin=input("Ingrese hora de final (XX:XX): ")
                consulta = "INSERT INTO Dentista (nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin) VALUES (%s, %s, %s, %s, %s, %s, %s);"
                cur.execute(consulta, (nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin))
                miConexion.commit()
                mostrarTablaDentistas()
                mostrarOpciones_Dentistas()

                opcionD=int(input("\nIngrese una opcion: "))
            
            elif opcionD==2:
                id = int(input("Ingrese el id del dentista a consultar: "))
                consulta = f"SELECT id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin FROM dentista WHERE id_dentista = {id};"
                cur.execute(consulta)
                print('-'*69+"TABLA DE DENTISTAS"+'-'*69)
                print(F"|    id_dentista   |     nombre    |    apellido      |     telefono   |           email          |      especialidad     |  hora_inicio   |    hora_fin   |")
                for id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin in cur.fetchall():
                    print("|%17d | %12s  | %15s  | %14s | %24s | %21s | %14s |%14s |" % (id_dentista, nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin))
                mostrarOpciones_Dentistas()
                opcionD = int(input("\nIngrese una opción: "))
            
            elif opcionD==3:
                id=int(input("Ingrese el id del dentista: "))
                nombre=input("Ingrese el nombre: ")
                apellido=input("Ingrese el apellido: ")
                telefono=input("Ingrese el teléfono: ")
                email=input("Ingrese el email: ")
                especialidad=input("Ingrese la especialidad : ")
                disponibilidad_inicio=input("Ingrese hora de inicio (XX:XX): ")
                disponibilidad_fin=input("Ingrese hora de final (XX:XX): ")
                consulta=F"UPDATE Dentista SET nombre = %s, apellido = %s, telefono = %s, email = %s, especialidad = %s, disponibilidad_inicio = %s, disponibilidad_fin = %s WHERE id_dentista= {id};"
                cur.execute(consulta, (nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin))
                miConexion.commit()
                mostrarTablaDentistas()
                mostrarOpciones_Dentistas()
                opcionD=int(input("\nIngrese una opcion: "))
        
            elif opcionD==4:
                id=int(input("Ingrese el id del dentista a eliminar: "))
                consulta=F"DELETE FROM Dentista WHERE id_dentista = {id};"
                cur.execute(consulta)
                miConexion.commit()
                mostrarTablaDentistas()
                mostrarOpciones_Dentistas()
                opcionD=int(input("\nIngrese una opcion: "))

            elif opcionD==5:
                opcionD=0
            
                mostrarMenu()
                opcion=int(input("\nIngrese una opcion: "))


    elif opcion==3:
        mostrarTablaAsistentes()
        print()
        mostrarOpciones_Asistentes()
        opcionA = int(input("\nIngrese una opcion: "))
        print()
        while (1 <= opcionA <= 5):
            if opcionA == 1:
                id_dentista = int(input("Ingrese el ID del dentista que tiene el asistente: "))
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                email = input("Ingrese el teléfono: ")
                telefono = input("Ingrese el email: ")
                consulta = f"INSERT INTO Asistente (id_dentista,nombre, apellido, email, telefono) VALUES ({id_dentista}, %s, %s, %s, %s);"
                cur.execute(consulta, (nombre, apellido, email, telefono))
                miConexion.commit()
                mostrarTablaAsistentes()
                mostrarOpciones_Asistentes()

                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA == 2:
                id = int(input("Ingrese el id del asistente a consultar: "))
                consulta = F"SELECT id_asistente, id_dentista, nombre, apellido, email, telefono FROM Asistente WHERE id_asistente = {id};"
                cur.execute(consulta)
                print('-' * 69 + "TABLA DE ASISTENTES" + '-' * 69)
                print(F"|    id_asistente   |    id_dentista    |     nombre     |    apellido      |    email   |    telefono   |")
                for id_asistente, id_dentista, nombre, apellido, email, telefono in cur.fetchall():
                    print("|%18d | %17d | %13s  | %15s  | %14s | %15s |" % (id_asistente, id_dentista, nombre, apellido, email,telefono))
                mostrarOpciones_Asistentes()
                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA == 3:
                id = int(input("Ingrese el id del asistente: "))
                id_dent=int(input("Ingrese el id del dentista que tiene le asistente:"))
                nombre = input("Ingrese el nombre: ")
                apellido = input("Ingrese el apellido: ")
                email = input("Ingrese el teléfono: ")
                telefono = input("Ingrese el email: ")
                consulta = F"UPDATE Asistente SET id_dentista = {id_dent},nombre = %s, apellido = %s, email = %s, telefono = %s WHERE id_asistente = {id};"
                cur.execute(consulta, (nombre, apellido, email, telefono))
                miConexion.commit()
                mostrarTablaAsistentes()
                mostrarOpciones_Asistentes()
                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA == 4:
                id = int(input("Ingrese el id del asistente a eliminar: "))
                consulta = F"DELETE FROM Asistente WHERE id_asistente = {id};"
                cur.execute(consulta)
                miConexion.commit()
                mostrarTablaAsistentes()
                mostrarOpciones_Asistentes()
                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA==5:
                opcionA=0

                mostrarMenu()
                opcion=int(input("\nIngrese una opcion: "))


    
    elif opcion==4:
        mostrarTablaCitas()
        print()
        mostrarOpciones_Citas()
        opcionA = int(input("\nIngrese una opcion: "))
        print()
        while (1 <= opcionA <= 5):
            if opcionA == 1:

                id_paciente = int(input("Ingrese el ID del paciente que tiene la cita: "))
                id_historia = int(input("Ingrese el ID de la h_clínica que tiene la cita: "))
                id_dentista = int(input("Ingrese el ID del dentista que tiene la cita: "))
                id_asistente = int(input("Ingrese el ID del asistente que tiene el dentista "))
                id_tratamiento = int(input("Ingrese el ID del tratamiento que tiene el paciente: "))
                cita_fecha = input("Ingrese la cita y fecha de la cita (año-mes-dia hora:minuto_segundo):")
                estado = input("Ingrese el estado de la cita (Pendiente,Cancelado,En curso,Finalizado): ")
                costo= float(input("Ingrese el costo: "))
                consulta = f"INSERT INTO Cita (id_paciente,id_historia,id_dentista,id_asistente,id_tratamiento,cita_fecha,estado,costo) VALUES ({id_paciente}, {id_historia}, {id_dentista}, {id_asistente}, {id_tratamiento}, %s, %s, {costo});"
                cur.execute(consulta, (cita_fecha,estado))
                miConexion.commit()
                mostrarTablaCitas()
                mostrarOpciones_Citas()

                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA == 2:
                id = int(input("Ingrese el id de la cita a consultar: "))
<<<<<<< HEAD
                consulta = F"SELECT id_cita,id_paciente,id_historia,id_dentista,id_asistente,id_tratamiento,cita_fecha,estado,costo FROM Cita WHERE id_cita = {id};"
=======
                consulta = F"SELECT id_cita, id_paciente,id_historia,id_dentista,id_asistente,id_tratamiento,cita_fecha,estado,costo FROM Cita WHERE id_cita = {id};"
>>>>>>> f4c9d74 (Final)
                cur.execute(consulta)
                print('-' * 69 + "TABLA DE CITAS" + '-' * 69)
                print(
                    F"|  id_cita   |   id_paciente   |   id_historia   |   id_dentista   |   id_asistente   |   id_tratamiento    |      cita_fecha     |     estado     |    costo   |")
                for id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo in cur.fetchall():
                    print("|%11d | %15d | %15d | %15d | %16d | %19d | %15s | %14s | %10.2f |" % (
                        id_cita, id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado,
                    costo))

                mostrarOpciones_Citas()
                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA == 3:
                id = int(input("Ingrese el id de la cita: "))
                id_paciente = int(input("Ingrese el ID del paciente que tiene la cita: "))
                id_historia = int(input("Ingrese el ID de la h_clínica que tiene la cita: "))
                id_dentista = int(input("Ingrese el ID del dentista que tiene la cita: "))
                id_asistente = int(input("Ingrese el ID del dentista que tiene el asistente: "))
                id_tratamiento = int(input("Ingrese el ID del dentista que tiene el asistente: "))
                cita_fecha = input("Ingrese la cita y fecha de la cita (año-mes-dia hora:minuto_segundo):")
                estado = input("Ingrese el estado de la cita (Pendiente,Cancelado,En curso,Finalizado): ")
                costo= float(input("Ingrese el costo: "))
                consulta = F"UPDATE Cita SET id_paciente = {id_paciente},id_historia = {id_historia},id_dentista = {id_dentista},id_asistente ={id_asistente},id_tratamiento = {id_tratamiento},cita_fecha = %s,estado = %s,costo={costo} WHERE id_cita = {id};"
                cur.execute(consulta, (cita_fecha,estado))
                miConexion.commit()
                mostrarTablaCitas()
                mostrarOpciones_Citas()
                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA == 4:
                id = int(input("Ingrese el id de la cita a eliminar: "))
                consulta = F"DELETE FROM Cita WHERE id_cita = {id};"
                cur.execute(consulta)
                miConexion.commit()
                mostrarTablaCitas()
                mostrarOpciones_Citas()
                opcionA = int(input("\nIngrese una opcion: "))

            elif opcionA==5:
                opcionA=0

                mostrarMenu()
                opcion = int(input("\nIngrese una opcion: "))




    elif opcion==5:
        mostrarTablaTratamiento()
        print()
        mostrarOpciones_Tratamientos()
        opcionT=int(input("\nIngrese una opcion: "))
        print()
        
        while(1<=opcionT<=5):
            if opcionT==1:

                id_paciente=int(input("Ingrese el id del paciente asociado a el tratamiento: "))
                nombre=input("Ingrese el nombre: ")
                descripcion=input("Ingrese una descripción: ")
                duracion=int(input("Ingrese la duración en dias del tratamiento: "))
                #cur.execute(F"INSERT INTO Paciente (id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion) VALUES ({id},{nombre}, {apellido}, {telefono}, {email}, {fecha_nac}, {direccion})")
                consulta = F"INSERT INTO Tratamiento (id_paciente, nombre, descripcion, duracion_dias) VALUES ({id_paciente}, %s, %s, {duracion});"
                cur.execute(consulta, (nombre, descripcion))
                miConexion.commit()
                mostrarTablaTratamiento()
                mostrarOpciones_Tratamientos()

                opcionT=int(input("\nIngrese una opcion: "))
            
            elif opcionT==2:
                id=int(input("Ingrese el id del tratamiento a consultar: "))
                consulta=F"SELECT id_tratamiento, id_paciente, nombre, descripcion, duracion_dias FROM Tratamiento WHERE id_tratamiento = {id};"
                cur.execute(consulta)
                
                print('-'*65+"TABLA DE TRATAMIENTOS"+'-'*65)
                print(F"|   id_tratamiento |    id_paciente    |           nombre          |                                 descripcion                             |    duracion_dias   |")
                for id_tratamiento,id_paciente, nombre, descripcion, duracion_dias in cur.fetchall():
                    print("|%17d | %17d |%25s  | %70s  | %18d |" %  (id_tratamiento, id_paciente,nombre, descripcion, duracion_dias)) 
                
                mostrarOpciones_Tratamientos()
                opcionT=int(input("\nIngrese una opcion: "))
                
            elif opcionT==3:
                id_tratamiento=int(input("Ingrese el id del tratamiento: "))
                id_paciente=int(input("Ingrese el id del paciente asociado a el tratamiento: "))
                nombre=input("Ingrese el nombre: ")
                descripcion=input("Ingrese una descripción: ")
                duracion=int(input("Ingrese la duración en dias del tratamiento: "))
                consulta=F"UPDATE Tratamiento SET id_paciente={id_paciente} ,nombre = %s, descripcion = %s, duracion_dias = {duracion} WHERE id_tratamiento = {id_tratamiento};"
                cur.execute(consulta,(nombre,descripcion))
                miConexion.commit()
                mostrarTablaTratamiento()
                mostrarOpciones_Tratamientos()
                opcionT=int(input("\nIngrese una opcion: "))
            
            elif opcionT==4:
                id_tratamiento=int(input("Ingrese el id del tratamiento a eliminar: "))
                consulta=F"DELETE FROM Tratamiento WHERE id_tratamiento = {id_tratamiento};"
                cur.execute(consulta)
                miConexion.commit()
                mostrarTablaTratamiento()
                mostrarOpciones_Tratamientos()
                opcionT=int(input("\nIngrese una opcion: "))
            
            elif opcionT==5:
                opcionT=0

                mostrarMenu()
                opcion=int(input("\nIngrese una opcion: "))  


    elif opcion==6:
        mostrarTablaHC()
        print()
        mostrarOpciones_HC()
        opcionHC=int(input("\nIngrese una opcion: "))
        print()
        while(1<=opcionHC<=5):
            if opcionHC==1:
                id_historia_clinica = 0
                id_paciente = int(input("Ingrese el ID del paciente: "))
                observaciones = input("Ingrese las observaciones: ")
                consulta = F"INSERT INTO historia_clinica (id_paciente, observaciones) VALUES ({id_paciente}, %s);"
                cur.execute(consulta, (observaciones))
                miConexion.commit()
                
                mostrarTablaHC()
                mostrarOpciones_HC()

                opcionHC=int(input("\nIngrese una opcion: "))
            
            elif opcionHC == 2:
                    id = int(input("Ingrese el ID de la historia clínica a consultar: "))
                    consulta = f"SELECT id_historia, id_paciente, observaciones FROM historia_clinica WHERE id_historia = {id};"
                    cur.execute(consulta)
                    
                    print('-'*69 + "TABLA DE HISTORIAS CLÍNICAS" + '-'*69)
                    print(F"| id_historia | id_paciente |                                                                             observaciones                                                              |")
                    for id_historia, id_paciente, observaciones in cur.fetchall():
                     print("|%12d | %11d | %150s |" % (id_historia, id_paciente, observaciones))

                    mostrarOpciones_HC()
                    opcionHC = int(input("\nIngrese una opción: "))

            elif opcionHC == 3:
                    id=int(input("Ingrese el ID de la Historia Clínica: "))
                    id_paciente = int(input("Ingrese el ID del paciente: "))
                    observaciones = input("Ingrese las observaciones: ")
                    consulta = f"UPDATE historia_clinica SET id_paciente = {id_paciente}, observaciones = %s WHERE id_historia = {id};"
                    cur.execute(consulta, (observaciones))
                    miConexion.commit()

                    mostrarTablaHC()
                    mostrarOpciones_HC()
                    opcionHC = int(input("\nIngrese una opción: "))
            
            elif opcionHC == 4:
                    id = int(input("Ingrese el ID de la historia clínica a eliminar: "))
                    consulta = f"DELETE FROM historia_clinica WHERE id_historia = {id};"
                    cur.execute(consulta)
                    miConexion.commit()
                    mostrarTablaHC()
                    mostrarOpciones_HC()
                    opcionHC = int(input("\nIngrese una opción: "))

            elif opcionHC == 5:
                opcionHC=0

                mostrarMenu()
                opcion=int(input("\nIngrese una opcion: "))
    

    elif opcion==7:
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
    elif opcion==8:
        opcion=0
        miConexion.close()
print("Saliendo....")