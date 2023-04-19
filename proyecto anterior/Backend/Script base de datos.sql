DROP DATABASE IF EXISTS ArSalud;
create database ArSalud;
use ArSalud;

CREATE TABLE `roles` (
  `id` int(3) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `tipo` varchar(50)
);

CREATE TABLE `especialidades` (
  `id` int(3) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `especialidad` varchar(150)
);

CREATE TABLE `medicos` (
  `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50),
  `apellido` varchar(50),
  `correo` varchar(100),
  `direccion` varchar(100),
  `telefono` varchar(100),
  `id_especialidad` int(3),
  CONSTRAINT fk_especialidad FOREIGN KEY (id_especialidad) REFERENCES especialidades (id)
);

CREATE TABLE `usuarios` (
  `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nombre` varchar(50),
  `apellido` varchar(50),
  `correo` varchar(100),
  `direccion` varchar(100),
  `telefono` varchar(40),
  `id_rol` int(3),
  CONSTRAINT fk_rol FOREIGN KEY (id_rol) REFERENCES roles (id)
);

CREATE TABLE `sanatorios` (
  `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100)
);

CREATE TABLE `turnos` (
  `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `id_usuarios` int(11),
  `id_medico` int(11),
  `id_sanatorio` int(11),
  `historial` varchar(250),
  CONSTRAINT fk_usuarios FOREIGN KEY (id_usuarios) REFERENCES usuarios (id),
  CONSTRAINT fk_medico FOREIGN KEY (id_medico) REFERENCES medicos (id),
  CONSTRAINT fk_sanatorio FOREIGN KEY (id_sanatorio) REFERENCES sanatorios (id)
);

CREATE TABLE `medicosSanatorio` (
  `id_medico` int(11) ,
  `id_sanatorio` int(11),
  CONSTRAINT fk_medico2 FOREIGN KEY (id_medico) REFERENCES medicos (id),
  CONSTRAINT fk_sanatorio2 FOREIGN KEY (id_sanatorio) REFERENCES sanatorios (id)
);

