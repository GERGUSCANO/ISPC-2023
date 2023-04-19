INSERT INTO roles VALUES (DEFAULT, "normal"), (DEFAULT, "advance");

INSERT INTO usuarios VALUES (DEFAULT, "Jose", "Perez", "joseperez@gmail.com", "Artigas 270", 0351155345789, 1);
INSERT INTO usuarios VALUES (DEFAULT, "Maria", "Gonzales", "mariag@gmail.com", "San Martín 150", 0351153278932, 2);
INSERT INTO usuarios VALUES (DEFAULT, "Lucas", "Sánchez", "lucassanchez@gmail.com", "Madrid 431", 0351154221358, 1);
INSERT INTO usuarios VALUES (DEFAULT, "Leandro", "Aguero", "leaaguero@gmail.com", "9 de julio 1310", 0351157616439, 1);
INSERT INTO usuarios VALUES (DEFAULT, "Patricia", "Acuña", "patriacu@gmail.com", "Av. Maipú 230", 0351152713952, 2);
INSERT INTO usuarios VALUES (DEFAULT, "Tamara", "Burgos", "tamiburgos@gmail.com", "Av. Colón 270", 0351157404493, 2);


UPDATE usuarios SET direccion="25 de mayo 400" WHERE id = 2;
UPDATE usuarios SET telefono=0351157757726 WHERE id = 3;
UPDATE usuarios SET id_rol=2 WHERE id = 4;

SELECT * FROM roles;
SELECT * FROM usuarios;
SELECT nombre, apellido, telefono FROM usuarios WHERE id_rol = 1;
SELECT nombre, apellido, telefono FROM usuarios WHERE id_rol = 2;

DELETE FROM usuarios WHERE id = 2;
DELETE FROM usuarios WHERE nombre = "Tamara";