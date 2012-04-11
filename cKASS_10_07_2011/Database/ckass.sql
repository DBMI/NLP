-- MySQL dump 10.13  Distrib 5.5.13, for Win64 (x86)
--
-- Host: localhost    Database: ckass
-- ------------------------------------------------------
-- Server version	5.5.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `concept`
--

DROP TABLE IF EXISTS `concept`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `concept` (
  `Concept_no` int(11) NOT NULL AUTO_INCREMENT,
  `Name` varchar(200) NOT NULL,
  `CUI` varchar(45) DEFAULT NULL COMMENT 'UMLS',
  `Category_no` int(11) NOT NULL,
  `Definition` varchar(600) DEFAULT NULL,
  `TID` int(12) NOT NULL,
  `Date` datetime DEFAULT NULL,
  `UID` int(10) DEFAULT NULL,
  PRIMARY KEY (`Concept_no`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `concept`
--

LOCK TABLES `concept` WRITE;
/*!40000 ALTER TABLE `concept` DISABLE KEYS */;
INSERT INTO `concept` VALUES (1,'Heart Failure','C00001',4,'Heart Failure',1,NULL,1),(3,'left ventricle',NULL,3,NULL,1,'2011-07-26 17:01:13',1),(4,'ejection fraction',NULL,2,NULL,1,'2011-07-26 17:01:27',1),(5,'BNP',NULL,6,NULL,1,'2011-07-26 17:01:40',1),(6,'Enoxaparin',NULL,1,NULL,1,'2011-07-26 17:03:07',1),(7,'Digoxin ',NULL,1,NULL,1,'2011-07-26 17:03:24',1),(8,'Angiotensin converting enzyme (ACE) inhibitors',NULL,1,NULL,1,'2011-07-26 17:03:37',1),(9,'heart transplant',NULL,5,NULL,1,'2011-07-26 17:23:18',1),(10,'edema',NULL,2,NULL,1,'2011-07-26 17:23:29',1),(11,'defibrillator implant',NULL,5,NULL,1,'2011-07-26 17:24:42',1),(12,'hematochezia',NULL,2,NULL,4,'2011-07-27 08:22:51',1),(13,'seizure',NULL,2,NULL,4,'2011-07-27 08:23:01',1),(14,'conjunctivitis',NULL,2,NULL,4,'2011-07-27 08:23:21',1),(15,'fever',NULL,2,NULL,4,'2011-07-27 08:23:31',1),(16,'dysentery',NULL,2,NULL,4,'2011-07-27 08:23:51',1),(17,'fever',NULL,2,NULL,5,'2011-07-27 08:48:52',1),(19,'fever',NULL,2,NULL,5,'2011-07-27 08:49:11',1),(20,'shortness of breath',NULL,2,NULL,5,'2011-07-27 08:49:26',1),(21,'flushed face',NULL,2,NULL,5,'2011-07-27 08:49:35',1),(22,'hoarseness',NULL,2,NULL,5,'2011-07-27 08:49:48',1);
/*!40000 ALTER TABLE `concept` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dx`
--

DROP TABLE IF EXISTS `dx`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dx` (
  `Concept_no` int(11) NOT NULL,
  `TID` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `Dx` varchar(100) NOT NULL,
  `Date` datetime DEFAULT NULL,
  PRIMARY KEY (`Concept_no`,`Dx`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dx`
--

LOCK TABLES `dx` WRITE;
/*!40000 ALTER TABLE `dx` DISABLE KEYS */;
/*!40000 ALTER TABLE `dx` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `regex`
--

DROP TABLE IF EXISTS `regex`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `regex` (
  `Concept_no` int(11) NOT NULL,
  `RegEx` varchar(200) NOT NULL,
  `TID` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `Date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`Concept_no`,`RegEx`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `regex`
--

LOCK TABLES `regex` WRITE;
/*!40000 ALTER TABLE `regex` DISABLE KEYS */;
/*!40000 ALTER TABLE `regex` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `syndrome`
--

DROP TABLE IF EXISTS `syndrome`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `syndrome` (
  `Concept_no` int(11) NOT NULL,
  `TID` int(11) NOT NULL,
  `UID` int(11) NOT NULL,
  `Syndrome` varchar(200) NOT NULL,
  `Date` datetime DEFAULT NULL,
  PRIMARY KEY (`Concept_no`,`Syndrome`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `syndrome`
--

LOCK TABLES `syndrome` WRITE;
/*!40000 ALTER TABLE `syndrome` DISABLE KEYS */;
/*!40000 ALTER TABLE `syndrome` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `task` (
  `TID` int(11) NOT NULL AUTO_INCREMENT,
  `UID` int(11) NOT NULL,
  `Name` varchar(100) NOT NULL,
  `Description` varchar(600) DEFAULT NULL,
  `Domain` varchar(100) DEFAULT NULL,
  `Date` datetime DEFAULT NULL,
  `Status` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`TID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,1,'Cardiology','Cardiology Disease Ontology','Cardiology','2011-07-22 15:12:51',0),(2,1,'pneumonia','pulmonary disease','Pulmonary','2011-07-24 21:05:36',0),(3,1,'Atrial Fibrillation','heart disease','Cardiology','2011-07-24 21:13:43',0),(4,1,'Shigellosis','The shigellosis knowledge base will be used for syndrome surveillance','Gastroenteritis','2011-07-27 08:21:59',0),(5,1,'Influenza Syndrome','Used for NLP-based Influenza surveillance system','Respiratory','2011-07-27 08:48:41',1),(6,1,'Heart Failure','The knowledge base will be used for the diagnosis of heart failure ','Cardiology','2011-07-27 09:00:29',0),(7,1,'puemonia','puemonia-oriented ontology','pulmonary','2011-08-30 13:42:10',0);
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `UID` int(10) NOT NULL AUTO_INCREMENT,
  `firstName` varchar(45) DEFAULT NULL,
  `lastName` varchar(45) DEFAULT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(45) NOT NULL,
  `userName` varchar(45) NOT NULL,
  PRIMARY KEY (`UID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Test','Test','test.test@utah.edu','123456','Jason'),(2,'null','null','null','null','null'),(3,'null','null','null','null','null'),(4,'null','null','null','null','null'),(5,'null','null','null','null','null'),(6,'null','null','null','null','null'),(7,'null','null','null','null','null'),(8,'null','null','null','null','null'),(9,'null','null','null','null','null'),(10,'null','null','null','null','null'),(11,'null','null','null','null','null'),(12,'Liqin','Wang','wlq.china@gmail.com','123456','bylinn');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vocab`
--

DROP TABLE IF EXISTS `vocab`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vocab` (
  `type_no` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `String` varchar(45) NOT NULL,
  PRIMARY KEY (`type_no`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vocab`
--

LOCK TABLES `vocab` WRITE;
/*!40000 ALTER TABLE `vocab` DISABLE KEYS */;
INSERT INTO `vocab` VALUES (1,'Medication'),(2,'Sign/Symptom'),(3,'Anatomical site'),(4,'Disease/Disorder'),(5,'Procedure'),(6,'Lab');
/*!40000 ALTER TABLE `vocab` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2011-09-14 21:38:46
