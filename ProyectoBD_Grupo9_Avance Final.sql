create database ClinicaDentalDB;
use ClinicaDentalDB;

create table Paciente(
id_paciente integer auto_increment primary key,
nombre varchar(50) not null,
apellido varchar(50) not null,
telefono char(10),
email varchar(50),
fecha_nacimiento date not null,
direccion varchar(50) not null

);

create table Tratamiento(
id_tratamiento integer auto_increment primary key,
id_paciente integer,
nombre varchar(50) not null,
descripcion varchar(150), 
duracion_dias integer default 60,
foreign key (id_paciente) references Paciente(id_paciente)
);

CREATE TABLE Dentista(
  id_dentista integer auto_increment primary key,
  nombre varchar(50) not null,
  apellido varchar(50) not null,
  telefono char(10),
  email varchar(50),
  especialidad varchar(50) not null,
  disponibilidad_inicio time,
  disponibilidad_fin time
  );
  
  CREATE TABLE Asistente(
    id_asistente integer auto_increment PRIMARY KEY,
    id_dentista integer,
    nombre varchar(50) not null,
    apellido varchar(50) not null,
    email varchar(50),
    telefono char(10),
    FOREIGN KEY (id_dentista) REFERENCES Dentista(id_dentista)
  );
  
  CREATE TABLE Historia_Clinica(
	id_historia integer primary key auto_increment,
    id_paciente integer,
    observaciones varchar(150),
    foreign key (id_paciente) references Paciente(id_paciente)
);

CREATE TABLE Cita(
	id_cita integer primary key auto_increment,
    id_paciente integer,
    id_historia integer,
    id_dentista integer,
    id_asistente integer,
    id_tratamiento integer,
    cita_fecha timestamp not null,
    estado enum("Pendiente","Cancelado","En curso","Finalizado") default "En curso",
    costo decimal(5,2),
    foreign key (id_paciente) references Paciente(id_paciente),
    foreign key (id_historia) references Historia_Clinica(id_historia),
    foreign key (id_dentista) references Dentista(id_dentista),
    foreign key (id_asistente) references Asistente(id_asistente),
    foreign key (id_tratamiento) references Tratamiento(id_tratamiento)
);

-- 10 pacientes
Insert into paciente values (0,"Jair","Palaguachi",0912345652,"jpalagua@espol.edu.ec","2004-06-21","Mucho Lote 1");
Insert into paciente values (0,"Jordan","Palaguachi",0945678910,"jordan@espol.edu.ec","2007-05-11","Mucho Lote 1");
Insert into paciente values (0,"Raul","Caicedo",0975149328,"raul@gmail.com","2000-08-25","Perimetral");
Insert into paciente values (0,"Mateo","Perez",0913285656,"mateo@gmail.com","1985-07-01","Samanes");
Insert into paciente values (0,"Pedro","Paredes",0917132493,"pedro2@gmail.com","1999-12-25","24 y Chambers");
Insert into paciente values (0,"Manuel","Murillo",0942564162,"manu78@gmail.com","2002-09-26","9 de Ocubre");
Insert into paciente values (0,"Samuel","Vallejo",0987564322,"svallej@espol.edu.ec","2001-02-01","Francisco de Orellana");
Insert into paciente values (0,"Angel","Chavez",0978436652,"achave@espol.edu.ec","2003-11-11","Vergeles");
Insert into paciente values (0,"Alejandro","Malucin",0915426437,"amaluci@espol.edu.ec","2004-03-31","Portete");
Insert into paciente values (0,"Luis","Guaman",0925461822,"luis12@gmail.com","2003-12-11","Cristo del Consuelo");

-- 10 tratamientos

Insert into Tratamiento values (0,1,"Ortodonocia","Tratamiento para correcion dental",365);
Insert into Tratamiento values (0,2,"Profilaxis","Tratamiento bucal",30);
Insert into tratamiento values (0,3,"Blanqueamiento dental","Procedimiento para conseguir el blanco natural de los dientes",30);
Insert into tratamiento values (0,4,"Carillas dentales","Tratamiento dental relacionado con la estética dental",60);
Insert into tratamiento values (0,5,"Exodoncia","Tratamiento para extracciones de dientes temporales",90);
Insert into tratamiento values (0,6,"Implantes dentales","Tratamiento para sustituir piezas dentales extraídas",90);
Insert into tratamiento values (0,7,"Férula dental","Tratamiento para conseguir una adaptación entre los dientes y boca",120);
Insert into tratamiento values (0,8,"Prótesis dental removible","Tratamiento temporal para sustituir piezas dentales",60);
Insert into tratamiento values (0,9,"Tratamiento periodontal","Tratamiento para la inflamación de encías",90);
Insert into tratamiento values (0,10,"Microabrasión del esmalte","Tratamiento para eliminar las manchas blancas en los dientes",60);

-- 10 Historias clinicas

INSERT INTO Historia_Clinica
Values(0,1,"Encías levemente inflamadas en la región anterior inferior"),
(0,2,"Dolor persiste desde hace una semana, sin alivio con analgésicos"),
(0,3,"Se realizó limpieza dental profesional con eliminación de placa y sarro en ambas arcadas. Aplicación de flúor tópico"),
(0,4,"Se recomienda seguimiento en 6 meses para revisión de la corona provisional"),
(0,5,"Se solicitarán estudios complementarios (modelos y cefalometría)"),
(0,6,"Presencia de caries incipiente en el molar superior izquierdo (26)"),
(0,7,"El paciente muestra una técnica de cepillado deficiente, con acumulación de placa en los molares posteriores superiores"),
(0,8, "La corona del segundo molar superior izquierdo muestra signos de desgaste y fisuración, con bordes irregulares."),
(0,9,"El paciente reporta sensibilidad aguda en el premolar inferior derecho al contacto con alimentos fríos."),
(0,10,"El paciente menciona un trauma dental reciente en el diente incisivo central superior izquierdo, con movilidad ligera y dolor a la palpación.");

-- 10 Dentistas

INSERT INTO Dentista VALUES(0,"José","Ayora","0912345678","jayora@hotmail.com","Ortodoncia","14:30:00","19:00:00");
INSERT INTO Dentista VALUES(0,"Fernanda","Barros","0915768912","fbarros@hotmail.com","Odontología General","15:00:00","18:00:00");
INSERT INTO Dentista VALUES(0,"Alejandro","Villa","0957890623","avilla@hotmail.com","Endodoncia","16:00:00","19:00:00");
INSERT INTO Dentista VALUES(0,"Domingo","Riera","0956643232","driera@hotmail.com","Ortodoncia","14:30:00","19:00:00");
INSERT INTO Dentista VALUES(0,"Rafael","Lopez","0954432123","rlopez@hotmail.com","Endodoncia","18:00:00","19:00:00");
INSERT INTO Dentista VALUES(0,"Maria","Ceballos","0987659087","mceballos@hotmail.com","Odontología General","15:30:00","18:30:00");
INSERT INTO Dentista VALUES(0,"Isabel","Centeno","0976659123","icenteno@hotmail.com","Endodoncia","14:30:00","19:00:00");
INSERT INTO Dentista VALUES(0,"Alan","Alvarez","0922334455","aalvarez@hotmail.com","Ortodoncia","15:30:00","19:00:00");
INSERT INTO Dentista VALUES(0,"Gabriel","Rivera","0965743216","grivera@hotmail.com","Odontología General","14:30:00","17:00:00");
INSERT INTO Dentista VALUES(0,"Luis","Villa","0909685432","lvilla@hotmail.com","Ortodoncia","14:30:00","16:30:00");

-- 10 Asistentes dentales
INSERT INTO Asistente VALUES(0,1,"Rodrigo","Barros","rbarros@hotmail.com","0943819573");
INSERT INTO Asistente VALUES(0,1,"Ramona","Ramos","rramos@hotmail.com","0934567321");
INSERT INTO Asistente VALUES(0,2,"Luisa","Barrios","lbarrios@hotmail.com","0954323456");
INSERT INTO Asistente VALUES(0,2,"Sergio","Reyes","sreyes@hotmail.com","0976543876");
INSERT INTO Asistente VALUES(0,2,"Lucas","Jaramillo","ljaramillo@hotmail.com","0945675432");
INSERT INTO Asistente VALUES(0,3,"Noah","Cantos","ncantos@hotmail.com","0946785643");
INSERT INTO Asistente VALUES(0,4,"Ramiro","Prado","rprado@hotmail.com","0965879654");
INSERT INTO Asistente VALUES(0,5,"Angelica","Palma","apalma@hotmail.com","0919870654");
INSERT INTO Asistente VALUES(0,6,"Sofia","Hernandez","shernandez@hotmail.com","0943267896");
INSERT INTO Asistente VALUES(0,7,"Victor","Manuel","vmanuel@hotmail.com","0946329087");


-- 10 Citas
use ClinicaDentalDB;
insert into cita values(0,1,1,1,1,1,timestamp("2024-12-12 01:30:00"),"Pendiente",250.50);
insert into cita values(0,2,2,2,2,2,timestamp("2025-11-10 21:45:00"),"Cancelado",350.50);
insert into cita values(0,3,3,3,3,3,timestamp("2024-02-02 08:00:00"),"Finalizado",450.50);
insert into cita values(0,4,4,4,4,4,timestamp("2025-06-15 11:00:00"),"Pendiente",50.50);
insert into cita values(0,5,5,5,5,5,timestamp("2024-08-25 13:00:00"),"Finalizado",120.50);
insert into cita values(0,6,6,6,6,6,timestamp("2024-09-27 14:00:00"),"En curso",250.00);
insert into cita values(0,7,7,7,7,7,timestamp("2024-10-28 15:00:00"),"Pendiente",150.50);
insert into cita values(0,8,8,8,8,8,timestamp("2024-11-01 16:00:00"),"En curso",100.50);
insert into cita values(0,9,9,9,9,9,timestamp("2025-12-25 23:00:00"),"Cancelado",200.50);
insert into cita values(0,10,10,10,10,10,timestamp("2024-03-12 10:00:00"),"En curso",250.00);


-- CRUD para la tabla Paciente

-- Crear (Create)
INSERT INTO Paciente (nombre, apellido, telefono, email, fecha_nacimiento, direccion)
VALUES ('Carlos', 'Gomez', '0912345678', 'cgomez@example.com', '1990-04-15', 'Centro');

-- Consultar (Read)
SELECT * FROM Paciente;
SELECT * FROM Paciente WHERE id_paciente = 1;

-- Editar (Update)
UPDATE Paciente
SET nombre = 'Carlos', apellido = 'Gómez', telefono = '0987654321', email = 'carlosg@example.com', direccion = 'Centro Histórico'
WHERE id_paciente = 1;

-- Eliminar (Delete)
DELETE FROM Paciente WHERE id_paciente = 1;

-- CRUD para la tabla Tratamiento

-- Crear (Create)
INSERT INTO Tratamiento (id_paciente, nombre, descripcion, duracion_dias)
VALUES (1, 'Limpieza profunda', 'Limpieza dental profunda para eliminar sarro y placa', 30);

-- Consultar (Read)
SELECT * FROM Tratamiento;
SELECT * FROM Tratamiento WHERE id_tratamiento = 1;

-- Editar (Update)
UPDATE Tratamiento
SET nombre = 'Limpieza básica', descripcion = 'Limpieza dental básica para eliminar placa', duracion_dias = 15
WHERE id_tratamiento = 1;

-- Eliminar (Delete)
DELETE FROM Tratamiento WHERE id_tratamiento = 1;

-- CRUD para la tabla Dentista

-- Crear (Create)
INSERT INTO Dentista (nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin)
VALUES ('Mariana', 'Pérez', '0934567890', 'mperez@example.com', 'Ortodoncia', '09:00:00', '17:00:00');

-- Consultar (Read)
SELECT * FROM Dentista;
SELECT * FROM Dentista WHERE id_dentista = 1;

-- Editar (Update)
UPDATE Dentista
SET nombre = 'Mariana', apellido = 'Pérez', telefono = '0998765432', especialidad = 'Odontología General'
WHERE id_dentista = 1;

-- Eliminar (Delete)
DELETE FROM Dentista WHERE id_dentista = 1;

-- CRUD para la tabla Asistente

-- Crear (Create)
INSERT INTO Asistente (id_dentista, nombre, apellido, email, telefono)
VALUES (1, 'Juan', 'Lopez', 'jlopez@example.com', '0923456789');

-- Consultar (Read)
SELECT * FROM Asistente;
SELECT * FROM Asistente WHERE id_asistente = 1;

-- Editar (Update)
UPDATE Asistente
SET nombre = 'Juan', apellido = 'Lopez', telefono = '0912345678', email = 'jlopez2@example.com'
WHERE id_asistente = 1;

-- Eliminar (Delete)
DELETE FROM Asistente WHERE id_asistente = 1;

-- CRUD para la tabla Historia_Clinica

-- Crear (Create)
INSERT INTO Historia_Clinica (id_paciente, observaciones)
VALUES (1, 'Paciente muestra signos de mejora en la inflamación de encías.');

-- Consultar (Read)
SELECT * FROM Historia_Clinica;
SELECT * FROM Historia_Clinica WHERE id_historia = 1;

-- Editar (Update)
UPDATE Historia_Clinica
SET observaciones = 'Inflamación en la región superior derecha ha disminuido.'
WHERE id_historia = 1;

-- Eliminar (Delete)
DELETE FROM Historia_Clinica WHERE id_historia = 1;

-- CRUD para la tabla Cita

-- Crear (Create)
INSERT INTO Cita (id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo)
VALUES (1, 1, 1, 1, 1, '2024-08-20 10:00:00', 'Pendiente', 200.00);

-- Consultar (Read)
SELECT * FROM Cita;
SELECT * FROM Cita WHERE id_cita = 1;

-- Editar (Update)
UPDATE Cita
SET estado = 'Finalizado', costo = 250.00
WHERE id_cita = 1;

-- Eliminar (Delete)
DELETE FROM Cita WHERE id_cita = 1;

-- CRUD para la tabla Paciente

-- Crear (Create)
INSERT INTO Paciente (nombre, apellido, telefono, email, fecha_nacimiento, direccion)
VALUES ('Carlos', 'Gomez', '0912345678', 'cgomez@example.com', '1990-04-15', 'Centro');

-- Consultar (Read)
SELECT * FROM Paciente;
SELECT * FROM Paciente WHERE id_paciente = 1;

-- Editar (Update)
UPDATE Paciente
SET nombre = 'Carlos', apellido = 'Gómez', telefono = '0987654321', email = 'carlosg@example.com', direccion = 'Centro Histórico'
WHERE id_paciente = 1;

-- Eliminar (Delete)
DELETE FROM Paciente WHERE id_paciente = 1;

-- CRUD para la tabla Tratamiento

-- Crear (Create)
INSERT INTO Tratamiento (id_paciente, nombre, descripcion, duracion_dias)
VALUES (1, 'Limpieza profunda', 'Limpieza dental profunda para eliminar sarro y placa', 30);

-- Consultar (Read)
SELECT * FROM Tratamiento;
SELECT * FROM Tratamiento WHERE id_tratamiento = 1;

-- Editar (Update)
UPDATE Tratamiento
SET nombre = 'Limpieza básica', descripcion = 'Limpieza dental básica para eliminar placa', duracion_dias = 15
WHERE id_tratamiento = 1;

-- Eliminar (Delete)
DELETE FROM Tratamiento WHERE id_tratamiento = 1;

-- CRUD para la tabla Dentista

-- Crear (Create)
INSERT INTO Dentista (nombre, apellido, telefono, email, especialidad, disponibilidad_inicio, disponibilidad_fin)
VALUES ('Mariana', 'Pérez', '0934567890', 'mperez@example.com', 'Ortodoncia', '09:00:00', '17:00:00');

-- Consultar (Read)
SELECT * FROM Dentista;
SELECT * FROM Dentista WHERE id_dentista = 1;

-- Editar (Update)
UPDATE Dentista
SET nombre = 'Mariana', apellido = 'Pérez', telefono = '0998765432', especialidad = 'Odontología General'
WHERE id_dentista = 1;

-- Eliminar (Delete)
DELETE FROM Dentista WHERE id_dentista = 1;

-- CRUD para la tabla Asistente

-- Crear (Create)
INSERT INTO Asistente (id_dentista, nombre, apellido, email, telefono)
VALUES (1, 'Juan', 'Lopez', 'jlopez@example.com', '0923456789');

-- Consultar (Read)
SELECT * FROM Asistente;
SELECT * FROM Asistente WHERE id_asistente = 1;

-- Editar (Update)
UPDATE Asistente
SET nombre = 'Juan', apellido = 'Lopez', telefono = '0912345678', email = 'jlopez2@example.com'
WHERE id_asistente = 1;

-- Eliminar (Delete)
DELETE FROM Asistente WHERE id_asistente = 1;

-- CRUD para la tabla Historia_Clinica

-- Crear (Create)
INSERT INTO Historia_Clinica (id_paciente, observaciones)
VALUES (1, 'Paciente muestra signos de mejora en la inflamación de encías.');

-- Consultar (Read)
SELECT * FROM Historia_Clinica;
SELECT * FROM Historia_Clinica WHERE id_historia = 1;

-- Editar (Update)
UPDATE Historia_Clinica
SET observaciones = 'Inflamación en la región superior derecha ha disminuido.'
WHERE id_historia = 1;

-- Eliminar (Delete)
DELETE FROM Historia_Clinica WHERE id_historia = 1;

-- CRUD para la tabla Cita

-- Crear (Create)
INSERT INTO Cita (id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo)
VALUES (1, 1, 1, 1, 1, '2024-08-20 10:00:00', 'Pendiente', 200.00);

-- Consultar (Read)
SELECT * FROM Cita;
SELECT * FROM Cita WHERE id_cita = 1;

-- Editar (Update)
UPDATE Cita
SET estado = 'Finalizado', costo = 250.00
WHERE id_cita = 1;

-- Eliminar (Delete)
DELETE FROM Cita WHERE id_cita = 1;


use ClinicaDentalDB;


-- 2 triggers 
-- Actualizar el Estado de Cita cuando se Elimina un Tratamiento
DELIMITER //
CREATE TRIGGER antes_de_eliminar_tratamiento
BEFORE DELETE ON Tratamiento
FOR EACH ROW
BEGIN
    UPDATE Cita
    SET estado = 'Cancelado'
    WHERE id_tratamiento = OLD.id_tratamiento;
END //
DELIMITER ;

-- Evitar la Eliminación de Pacientes con Tratamientos Activos
DELIMITER //
CREATE TRIGGER antes_de_eliminar_paciente
BEFORE DELETE ON Paciente
FOR EACH ROW
BEGIN
    DECLARE tratamientos_activos INT;
    
    -- Verifica si el paciente tiene tratamientos activos
    SELECT COUNT(*) INTO tratamientos_activos
    FROM Tratamiento
    WHERE id_paciente = OLD.id_paciente;

    -- Si hay tratamientos activos, evita la eliminación del paciente
    IF tratamientos_activos > 0 THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'No se puede eliminar el paciente porque tiene tratamientos activos.';
    END IF;
END //
DELIMITER ;


-- triggers para la eliminacíon de datos referenciados

-- PACIENTE
DELIMITER //
CREATE TRIGGER trg_anteseliminarPaciente
BEFORE DELETE ON Paciente
FOR EACH ROW
BEGIN
	DELETE FROM cita where id_paciente=OLD.id_paciente;
    DELETE FROM tratamiento where id_paciente=OLD.id_paciente;
    DELETE FROM historia_clinica where id_paciente=old.id_paciente;
END //
DELIMITER ;


-- HISTORIA CLÍNICA
DELIMITER //
CREATE TRIGGER trg_anteseliminarHistoria
BEFORE DELETE ON Historia_clinica
FOR EACH ROW
BEGIN
	DELETE FROM cita where id_historia=OLD.id_historia;
END //
DELIMITER ;


-- TRATAMIENTO
DELIMITER //
CREATE TRIGGER trg_anteseliminarTratamiento
BEFORE DELETE ON Tratamiento
FOR EACH ROW
BEGIN
	DELETE FROM cita where id_tratamiento=OLD.id_tratamiento;
END //
DELIMITER ;


-- DENTISTA
DELIMITER //

CREATE TRIGGER borrar_citas_y_asistentes_al_borrar_dentista
BEFORE DELETE ON Dentista
FOR EACH ROW
BEGIN
    DELETE FROM Cita WHERE id_dentista = OLD.id_dentista;
    DELETE FROM Asistente WHERE id_dentista = OLD.id_dentista;
END //

DELIMITER ;

-- ASISTENTE
DELIMITER //

CREATE TRIGGER borrar_citas_al_borrar_asistente
BEFORE DELETE ON Asistente
FOR EACH ROW
BEGIN
    DELETE FROM Cita WHERE id_asistente = OLD.id_asistente;
END //

DELIMITER ;




-- 4 views con al menos 3 tablas

-- Pacientes con Mayor Número de Citas y Tratamientos Activos
CREATE VIEW reporte_pacientes_citas_tratamientos AS
SELECT p.id_paciente, p.nombre, p.apellido, COUNT(c.id_cita) AS numero_de_citas, count( t.id_tratamiento) AS tratamientos_activos
FROM Paciente p
LEFT JOIN Cita c ON p.id_paciente = c.id_paciente
LEFT JOIN Tratamiento t ON p.id_paciente = t.id_paciente
GROUP BY p.id_paciente, p.nombre, p.apellido
ORDER BY numero_de_citas DESC, tratamientos_activos DESC;

select * from reporte_pacientes_citas_tratamientos;

-- Ingresos Totales por Paciente, Dentista, y Tratamiento
CREATE VIEW reporte_ingresos_pacientes_dentistas_tratamientos AS
SELECT p.id_paciente, d.id_dentista, t.id_tratamiento, SUM(c.costo) AS ingresos_totales
FROM Paciente p
JOIN Cita c ON p.id_paciente = c.id_paciente
JOIN Dentista d ON c.id_dentista = d.id_dentista
JOIN Tratamiento t ON t.id_tratamiento = c.id_tratamiento
GROUP BY p.id_paciente, d.id_dentista, t.id_tratamiento
ORDER BY ingresos_totales DESC;

select * from reporte_ingresos_pacientes_dentistas_tratamientos;

-- Vista para Tratamientos Más Populares y Su Duración Promedio
CREATE VIEW reporte_tratamientos_populares AS
SELECT t.id_tratamiento, t.nombre AS nombre_tratamiento, COUNT(c.id_cita) AS numero_de_citas , AVG(t.duracion_dias) AS duracion_promedio
FROM Tratamiento t
JOIN Cita c ON t.id_tratamiento = c.id_tratamiento
JOIN Paciente p ON c.id_paciente = p.id_paciente
GROUP BY t.id_tratamiento, t.nombre
ORDER BY numero_de_citas DESC;

select * from reporte_tratamientos_populares;

-- Dentistas con Mayor Número de Citas y Asistentes Asociados
CREATE VIEW reporte_dentistas_citas_asistentes AS
SELECT d.id_dentista, d.nombre AS nombre_dentista, d.apellido AS apellido_dentista, COUNT(c.id_cita) AS numero_de_citas, COUNT(DISTINCT a.id_asistente) AS numero_de_asistentes, t.nombre AS tratamiento_comun
FROM Dentista d
LEFT JOIN Cita c ON d.id_dentista = c.id_dentista
LEFT JOIN Asistente a ON d.id_dentista = a.id_dentista
LEFT JOIN Tratamiento t ON t.id_tratamiento = c.id_tratamiento
GROUP BY d.id_dentista, d.nombre, d.apellido , t.nombre
ORDER BY numero_de_citas DESC, numero_de_asistentes DESC;

Select * from reporte_dentistas_citas_asistentes;



-- STORED PROCEDURES

-- Stored Procedure para Insertar un Asistente
DELIMITER //

CREATE PROCEDURE sp_insertar_asistente(
	IN a_id_dentista int(11),
    IN a_nombre VARCHAR(50),
    IN a_apellido VARCHAR(50),
    IN a_email VARCHAR(50),
    IN a_telefono CHAR(10)
    
)

BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar el asistente';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Inserta el nuevo paciente en la tabla
    INSERT INTO Asistente (id_dentista, nombre, apellido, email, telefono)
    VALUES (a_id_dentista, a_nombre, a_apellido, a_email, a_telefono);

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;

 call sp_insertar_asistente(9,'Pepe','Santos','pepe@gmail.com','0987412563')
 
 
 -- Stored Procedure para Actualizar un Asistente
DELIMITER //

CREATE PROCEDURE sp_actualizar_asistente(
	IN a_id_asistente int(11),
    IN a_id_dentista int(11),
    IN a_nombre VARCHAR(50),
    IN a_apellido VARCHAR(50),
    IN a_email VARCHAR(50),
    IN a_telefono CHAR(10)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar el asistente';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Actualiza los datos del paciente en la tabla
    UPDATE Asistente
    SET id_dentista=a_id_dentista, nombre = a_nombre, apellido = a_apellido, email = a_email, telefono=a_telefono 
    WHERE id_asistente = a_id_asistente;

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;

call sp_actualizar_asistente(13,5,'Manuel','Santos','manuel@gmail.com','0912378945')

-- Stored Procedure para Eliminar un Asistente
DELIMITER //

CREATE PROCEDURE sp_eliminar_asistente(
    IN a_id_asistente INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar el paciente';
    END;
        -- Inicio de la transacción
        START TRANSACTION;

        -- Elimina el paciente de la tabla
        DELETE FROM Asistente WHERE id_asistente = a_id_asistente;

        -- Si todo sale bien, se confirma la transacción
        COMMIT;
    
END //

DELIMITER ;

call sp_eliminar_asistente(13);



-- Stored Procedure para Insertar un Paciente
DELIMITER //

CREATE PROCEDURE sp_insertar_paciente(
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(50),
    IN p_telefono CHAR(10),
    IN p_email VARCHAR(50),
    IN p_fecha_nacimiento DATE,
    IN p_direccion VARCHAR(50)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar el paciente';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Inserta el nuevo paciente en la tabla
    INSERT INTO Paciente (nombre, apellido, telefono, email, fecha_nacimiento, direccion)
    VALUES (p_nombre, p_apellido, p_telefono, p_email, p_fecha_nacimiento, p_direccion);

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;


-- Stored Procedure para Actualizar un Paciente
DELIMITER //

CREATE PROCEDURE sp_actualizar_paciente(
    IN p_id_paciente INT,
    IN p_nombre VARCHAR(50),
    IN p_apellido VARCHAR(50),
    IN p_telefono CHAR(10),
    IN p_email VARCHAR(50),
    IN p_fecha_nacimiento DATE,
    IN p_direccion VARCHAR(50)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar el paciente';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Actualiza los datos del paciente en la tabla
    UPDATE Paciente
    SET nombre = p_nombre, apellido = p_apellido, telefono = p_telefono, email = p_email, fecha_nacimiento = p_fecha_nacimiento, direccion = p_direccion
    WHERE id_paciente = p_id_paciente;

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;


-- Stored Procedure para Eliminar un Paciente 
DELIMITER //

CREATE PROCEDURE sp_eliminar_paciente(
    IN p_id_paciente INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar el paciente';
    END;

        -- Inicio de la transacción
        START TRANSACTION;

        -- Elimina el paciente de la tabla
        DELETE FROM Paciente WHERE id_paciente = p_id_paciente;

        -- Si todo sale bien, se confirma la transacción
        COMMIT;
   
END //

DELIMITER ;

-- Stored Procedure para insertar un dentista
DELIMITER //

CREATE PROCEDURE sp_insertar_dentista(
    IN d_nombre VARCHAR(50),
    IN d_apellido VARCHAR(50),
    IN d_telefono CHAR(10),
    IN d_email VARCHAR(50),
    IN d_especialidad varchar(50),
    IN d_inicio time,
    IN d_fin time
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar el dentista';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Inserta el nuevo dentista en la tabla
    INSERT INTO Dentista (nombre, apellido, telefono, email, especialidad,disponibilidad_inicio,disponibilidad_fin)
    VALUES (d_nombre, d_apellido, d_telefono, d_email, d_especialidad, d_inicio,d_fin);

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;



-- Stored Procedure para Actualizar un dentista
DELIMITER //

CREATE PROCEDURE sp_actualizar_dentista(
    IN d_id_dentista INT,
    IN d_nombre VARCHAR(50),
    IN d_apellido VARCHAR(50),
    IN d_telefono CHAR(10),
    IN d_email VARCHAR(50),
    IN d_especialidad varchar(50),
    IN d_inicio time,
    IN d_fin time
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar el dentista';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Actualiza los datos del dentista en la tabla
    UPDATE Dentista
    SET nombre = d_nombre, apellido = d_apellido, telefono = d_telefono, email = d_email, especialidad=d_especialidad, disponibilidad_inicio=d_inicio,disponibilidad_fin=d_fin
    WHERE id_dentista = d_id_dentista;

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;

-- Stored Procedure para Eliminar un dentista con Validación
DELIMITER //

CREATE PROCEDURE sp_eliminar_dentista(
    IN d_id_dentista INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar el dentista';
    END;


    -- Inicio de la transacción
    START TRANSACTION;

    -- Elimina el dentista de la tabla
    DELETE FROM Dentista WHERE id_dentista = d_id_dentista;

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;

DELIMITER //

CREATE PROCEDURE sp_insertar_historia(
    IN h_observaciones varchar(150),
    IN h_id_paciente int
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar la historia clínica';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Inserta la historia clinica en la tabla
    INSERT INTO Historia_clinica (id_paciente, observaciones)
    VALUES (h_id_paciente, h_observaciones);

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;

-- Stored Procedure para Actualizar una historia clinica
DELIMITER //

CREATE PROCEDURE sp_actualizar_historia(
	IN h_id_historia int,
    IN h_observaciones varchar(150),
    IN h_id_paciente int
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar la historia clinica';
    END;

    -- Inicio de la transacción
    START TRANSACTION;

    -- Actualiza los datos de la historia en la tabla
    UPDATE Historia_clinica
    SET id_paciente = h_id_paciente, observaciones=h_observaciones
    WHERE id_historia = h_id_historia;

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;

-- Stored Procedure para Eliminar una historia clinica con Validación
DELIMITER //

CREATE PROCEDURE sp_eliminar_historia(
    IN h_id_historia INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        -- Si ocurre un error, se realiza un rollback para deshacer los cambios
        ROLLBACK;
        -- Se lanza un error personalizado
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar la historia clínica';
    END;


    -- Inicio de la transacción
    START TRANSACTION;

    -- Elimina la historia de la tabla
    DELETE FROM historia_clinica WHERE id_historia = h_id_historia;

    -- Si todo sale bien, se confirma la transacción
    COMMIT;
END //

DELIMITER ;


-- TRATAMIENTOS
DELIMITER //
CREATE PROCEDURE InsertarTratamiento(
    IN p_id_paciente INT,
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(150),
    IN p_duracion_dias INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar tratamiento';
    END;
    START TRANSACTION;
    INSERT INTO Tratamiento (id_paciente, nombre, descripcion, duracion_dias)
    VALUES (p_id_paciente, p_nombre, p_descripcion, p_duracion_dias);
    COMMIT;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarTratamiento(
    IN p_id_tratamiento INT,
    In p_id_paciente int,
    IN p_nombre VARCHAR(50),
    IN p_descripcion VARCHAR(150),
    IN p_duracion_dias INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar tratamiento';
    END;
    START TRANSACTION;
    UPDATE Tratamiento 
    SET nombre = p_nombre, descripcion = p_descripcion, duracion_dias = p_duracion_dias,id_paciente=p_id_paciente
    WHERE id_tratamiento = p_id_tratamiento;
    
    COMMIT;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE EliminarTratamiento(
    IN p_id_tratamiento INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar tratamiento';
    END;
    START TRANSACTION;
    DELETE FROM Tratamiento WHERE id_tratamiento = p_id_tratamiento; 
    COMMIT;
END //
DELIMITER ;

-- CITAS
DELIMITER //
CREATE PROCEDURE InsertarCita(
    IN p_id_paciente INT,
    IN p_id_historia INT,
    IN p_id_dentista INT,
    IN p_id_asistente INT,
    IN p_id_tratamiento INT,
    IN p_cita_fecha TIMESTAMP,
    IN p_estado ENUM('Pendiente','Cancelado','En curso','Finalizado'),
    IN p_costo DECIMAL(5,2)
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al insertar cita';
    END;
    START TRANSACTION;
    INSERT INTO Cita (id_paciente, id_historia, id_dentista, id_asistente, id_tratamiento, cita_fecha, estado, costo)
    VALUES (p_id_paciente, p_id_historia, p_id_dentista, p_id_asistente, p_id_tratamiento, p_cita_fecha, p_estado, p_costo);
    COMMIT;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE ActualizarCita(
    IN p_id_cita INT,
    IN p_estado ENUM('Pendiente','Cancelado','En curso','Finalizado'),
    IN p_costo DECIMAL(5,2),
    In p_cita_fecha timestamp,
    IN p_id_paciente int(11),
    IN p_id_historia int(11),
    IN p_id_dentista int(11),
    IN p_id_asistente int(11),
    IN p_id_tratamiento int(11)
  
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al actualizar cita';
    END;
    START TRANSACTION;
    UPDATE Cita 
    SET estado = p_estado, costo = p_costo,id_paciente=p_id_paciente, id_historia=p_id_historia,id_asistente=p_id_asistente,id_tratamiento=p_id_tratamiento,cita_fecha=p_cita_fecha,id_dentista=p_id_dentista
    WHERE id_cita = p_id_cita;
    COMMIT;
END //
DELIMITER ;

drop procedure ActualizarCita;

DELIMITER //
CREATE PROCEDURE EliminarCita(
    IN p_id_cita INT
)
BEGIN
    DECLARE EXIT HANDLER FOR SQLEXCEPTION
    BEGIN
        ROLLBACK;
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error al eliminar cita';
    END;
    START TRANSACTION;
    DELETE FROM Cita WHERE id_cita = p_id_cita;
    COMMIT;
END //
DELIMITER ;


-- Creación de usuarios de pacientes
CREATE USER 'paciente1'@'localhost' IDENTIFIED BY 'paciente1_pass';
CREATE USER 'paciente2'@'localhost' IDENTIFIED BY 'paciente2_pass';
CREATE USER 'paciente3'@'localhost' IDENTIFIED BY 'paciente3_pass';

-- Creación de usuarios de doctores
CREATE USER 'doctor1'@'localhost' IDENTIFIED BY 'doctor1_pass';
CREATE USER 'doctor2'@'localhost' IDENTIFIED BY 'doctor2_pass';

-- Permisos para pacientes
GRANT SELECT, UPDATE ON ClinicaDentalDB.Cita TO 'paciente1'@'localhost';
GRANT SELECT, UPDATE ON ClinicaDentalDB.Cita TO 'paciente2'@'localhost';
GRANT SELECT,UPDATE ON ClinicaDentalDB.Historia_Clinica TO 'paciente3'@'localhost';

-- Permisos para doctores a los sp
GRANT EXECUTE ON PROCEDURE ClinicaDentalDB.InsertarTratamiento TO 'doctor1'@'localhost';
GRANT EXECUTE ON PROCEDURE ClinicaDentalDB.ActualizarCita TO 'doctor1'@'localhost';
GRANT EXECUTE ON PROCEDURE ClinicaDentalDB.InsertarCita TO 'doctor2'@'localhost';
GRANT EXECUTE ON PROCEDURE ClinicaDentalDB.EliminarTratamiento TO 'doctor2'@'localhost';

-- Asignación de permisos a las vistas
GRANT SELECT ON ClinicaDentalDB.reporte_dentistas_citas_asistentes TO 'paciente1'@'localhost';
GRANT SELECT ON ClinicaDentalDB.reporte_pacientes_citas_tratamientos TO 'doctor1'@'localhost';


-- Creación de índices
CREATE INDEX idxpaciente ON paciente(id_paciente,nombre,apellido);
CREATE INDEX idxdentista ON dentista(id_dentista,nombre,apellido);
CREATE INDEX idxtrata ON tratamiento(id_tratamiento,nombre);
CREATE INDEX idxcita ON cita(id_cita);
CREATE INDEX idxasis ON asistente(id_asistente);


