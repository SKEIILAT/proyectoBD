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
            mostrarOpciones_Pacientes()

            opcionP=int(input("\nIngrese una opcion: "))
        
        elif opcionP==2:
            id=int(input("Ingrese el id del paciente a consultar: "))
            consulta=F"SELECT id_paciente, nombre, apellido, telefono, email, fecha_nacimiento, direccion FROM Paciente WHERE id_paciente = {id};"
            cur.execute(consulta)
            """
            fila=cur.fetchone()
            print(fila)
            """
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

        mostrarMenu()
        opcion=int(input("\nIngrese una opcion: ")) 
        


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

    elif opcion==5:
        print('-'*69+"TABLA DE TRATAMIENTO"+'-'*69)
        print(F"|  id_tratamiento  |     nombre     |     descripcion    |    duracion_dias   |")
        cur.execute("select id_tratamiento, nombre, descripcion, duracion_dias FROM tratamiento")
        for id_tratamiento, nombre, descripcion, duracion_dias in cur.fetchall():
            print("|%16d | %12s  | %15s  | %14d |" %  (id_tratamiento, nombre, descripcion, duracion_dias))
        opcion=int(input("\nIngrese una opcion: "))
        print()
        mostrarOpciones_Tratamientos()

    elif opcion==6:
        print('-'*69 + "TABLA DE HISTORIAS CLÍNICAS" + '-'*69)
        print(F"| id_historia | id_paciente |   observaciones   |")
        cur.execute("SELECT id_historia, id_paciente, observaciones FROM historia_clinica")
        for id_historia, id_paciente, observaciones in cur.fetchall():
            print("|%13d | %12d | %17s |" % (id_historia, id_paciente, observaciones))
        opcion=int(input("\nIngrese una opcion: "))
        print()
        mostrarOpciones_HC()

    elif opcion==7:
        opcion=0
        miConexion.close()
print("Saliendo....")


