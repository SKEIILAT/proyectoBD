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

-- CONSULTAS
-- 1. Pacientes con el mayor número de citas
SELECT p.nombre, p.apellido, COUNT(c.id_cita) AS numero_de_citas
FROM Paciente p
JOIN Cita c ON p.id_paciente = c.id_paciente
GROUP BY p.id_paciente
ORDER BY numero_de_citas DESC;

-- 2. Dentistas con el mayor número de citas asignadas
SELECT d.nombre, d.apellido, COUNT(c.id_dentista) AS cantidad_citas
FROM Dentista d
JOIN Cita c ON d.id_dentista = c.id_dentista
GROUP BY d.id_dentista
ORDER BY cantidad_citas DESC;

-- 3. Asistentes que trabajan con más dentistas
SELECT a.nombre, a.apellido, COUNT(DISTINCT a.id_dentista) AS cantidad_dentistas
FROM Asistente a
GROUP BY a.id_asistente
ORDER BY cantidad_dentistas DESC;

-- 4. Tratamientos con el costo promedio más alto
SELECT t.nombre AS tratamiento, AVG(c.costo) AS costo_promedio
FROM Tratamiento t
JOIN Cita c ON t.id_tratamiento = c.id_tratamiento
GROUP BY t.id_tratamiento
ORDER BY costo_promedio DESC; 

-- 5. Detalles de citas por estado
SELECT estado, COUNT(id_cita) AS cantidad_citas
FROM Cita
GROUP BY estado;

-- 6 Número total de citas por paciente
SELECT p.nombre, p.apellido, COUNT(c.id_cita) AS cantidad_citas
FROM Paciente p
JOIN Cita c ON p.id_paciente = c.id_paciente
GROUP BY p.id_paciente;

select * from paciente;
select * from dentista;

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