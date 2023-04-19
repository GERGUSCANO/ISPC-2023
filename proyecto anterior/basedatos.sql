CREATE DATABASE  IF NOT EXISTS `turnero_sanatorio` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `turnero_sanatorio`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: turnero_sanatorio
-- ------------------------------------------------------
-- Server version	8.0.27

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cadastro_medico`
--

DROP TABLE IF EXISTS `cadastro_medico`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cadastro_medico` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `Direccion` varchar(150) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `Telefono` varchar(45) NOT NULL,
  `Especialidad` varchar(45) NOT NULL,
  `id_pagina_principal` int DEFAULT NULL,
  `nombre_usuario` varchar(40) NOT NULL,
  `contrasena` varchar(30) DEFAULT NULL,
  `confirmar_contrasena` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pagina_principal` (`id_pagina_principal`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadastro_medico`
--

LOCK TABLES `cadastro_medico` WRITE;
/*!40000 ALTER TABLE `cadastro_medico` DISABLE KEYS */;
INSERT INTO `cadastro_medico` VALUES (3,'daniel','sosa','avellaneda 145','daniel123@gmail.com','123456','cardiologista',NULL,'dani123','d123456','d123456');
/*!40000 ALTER TABLE `cadastro_medico` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cadastro_usuario`
--

DROP TABLE IF EXISTS `cadastro_usuario`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cadastro_usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Nombre` varchar(45) NOT NULL,
  `Apellido` varchar(45) NOT NULL,
  `Direccion` varchar(150) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `Telefono` varchar(45) NOT NULL,
  `id_pagina_princial` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_pagina_princial` (`id_pagina_princial`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cadastro_usuario`
--

LOCK TABLES `cadastro_usuario` WRITE;
/*!40000 ALTER TABLE `cadastro_usuario` DISABLE KEYS */;
INSERT INTO `cadastro_usuario` VALUES (1,'Juan','Moralles','San Juan 245','juan@gmail.com','123456789',NULL),(2,'mario','marquez','Rivadavia 111','mario@gmail.com','123456789',NULL);
/*!40000 ALTER TABLE `cadastro_usuario` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `especialidades`
--

DROP TABLE IF EXISTS `especialidades`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `especialidades` (
  `id` int NOT NULL AUTO_INCREMENT,
  `especialidad` varchar(150) DEFAULT NULL,
  `id_medicos` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_medicos` (`id_medicos`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `especialidades`
--

LOCK TABLES `especialidades` WRITE;
/*!40000 ALTER TABLE `especialidades` DISABLE KEYS */;
/*!40000 ALTER TABLE `especialidades` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paciente_x_especialidad`
--

DROP TABLE IF EXISTS `paciente_x_especialidad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `paciente_x_especialidad` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_especialidad` int DEFAULT NULL,
  `id_pacientes` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_especialidad` (`id_especialidad`),
  KEY `id_pacientes` (`id_pacientes`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paciente_x_especialidad`
--

LOCK TABLES `paciente_x_especialidad` WRITE;
/*!40000 ALTER TABLE `paciente_x_especialidad` DISABLE KEYS */;
/*!40000 ALTER TABLE `paciente_x_especialidad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pagina_principal`
--

DROP TABLE IF EXISTS `pagina_principal`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pagina_principal` (
  `id` int NOT NULL AUTO_INCREMENT,
  `usuario` varchar(40) NOT NULL,
  `contrasena` varchar(25) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pagina_principal`
--

LOCK TABLES `pagina_principal` WRITE;
/*!40000 ALTER TABLE `pagina_principal` DISABLE KEYS */;
/*!40000 ALTER TABLE `pagina_principal` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `turnero`
--

DROP TABLE IF EXISTS `turnero`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `turnero` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_paciente_x_especialidad` int DEFAULT NULL,
  `id_especialidad` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `id_paciente_x_especialidad` (`id_paciente_x_especialidad`),
  KEY `id_especialidad` (`id_especialidad`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `turnero`
--

LOCK TABLES `turnero` WRITE;
/*!40000 ALTER TABLE `turnero` DISABLE KEYS */;
/*!40000 ALTER TABLE `turnero` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-15 17:24:50
