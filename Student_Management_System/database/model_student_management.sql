-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: model
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `student_management`
--

DROP TABLE IF EXISTS `student_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_management` (
  `roll` int NOT NULL,
  `name` varchar(200) NOT NULL,
  `gender` varchar(200) NOT NULL,
  `dob` varchar(200) NOT NULL,
  `class` varchar(200) NOT NULL,
  `email` varchar(200) DEFAULT NULL,
  `contact` varchar(200) DEFAULT NULL,
  `country` varchar(200) NOT NULL,
  `city` varchar(200) NOT NULL,
  `address` varchar(200) NOT NULL,
  PRIMARY KEY (`roll`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `contact` (`contact`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_management`
--

LOCK TABLES `student_management` WRITE;
/*!40000 ALTER TABLE `student_management` DISABLE KEYS */;
INSERT INTO `student_management` VALUES (3,'ranjit','Male','1990/12/12','computing','vanka@xakke','1234562345','Nepal','Bidur','Bidur-123\n\n\n'),(4,'Krisha','Female','2000/01/01','computing','123@123','9090992309','Nepal','Dhading','Smajong\n\n\n'),(7,'Dhungana','Female','2000/12/12','Civil Engeneering','me@dgybga','990921123','Nepal','KTM','Dhumbaharai\n\n\n\n'),(10,'Aagya','Female','2000/12/12','Miss Nepal','me@aagya','910921123','Nepal','KTM','Dhumbaharai\n\n\n\n'),(11,'Saitama','male','1995/04/03','python','samtha@gmail.com','9843456825','nep','ktm','jpt'),(14,'Meena','Female','1998/01/10','BHM','me@meena','123983132','Nepal','KTM','Basundhara\n\n'),(33,'shankar','male','2000/10/12','python','p@p@','100000111','Nepa;','Ktm','Boudha\n\n'),(43,'Krisha','Female','1999/01/01','computing','123@101','889982934','Nepal','Dhading','Smajong\n\n\n\n\n'),(50,'shankar','male','2001/03/2','python','p@p01','100012212','Nepal','Ktm','Boudha\n');
/*!40000 ALTER TABLE `student_management` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-09-04 14:00:56
