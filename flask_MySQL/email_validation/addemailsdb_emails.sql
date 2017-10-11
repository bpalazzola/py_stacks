

--
-- Table structure for table `emails`
--

-- DROP TABLE IF EXISTS `emails`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emails` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emails`
--

LOCK TABLES `emails` WRITE;
/*!40000 ALTER TABLE `emails` DISABLE KEYS */;
INSERT INTO `emails` VALUES (1,'er1qjpeq@hotmail.com','2017-08-11 08:18:35','2017-08-11 08:18:35'),(2,'er1qjpeq@hotmail.com','2017-08-11 08:22:32','2017-08-11 08:22:32'),(3,'er1qjpeq@hotmail.com','2017-08-11 08:27:27','2017-08-11 08:27:27'),(4,'er1qjpeq@hotmail.com','2017-08-11 08:29:15','2017-08-11 08:29:15'),(5,'er1qjpeq@hotmail.com','2017-08-11 08:32:18','2017-08-11 08:32:18'),(6,'er1qjpeq@hotmail.com','2017-08-11 08:36:18','2017-08-11 08:36:18'),(7,'er1qjpeq@hotmail.com','2017-08-11 08:37:33','2017-08-11 08:37:33');
/*!40000 ALTER TABLE `emails` ENABLE KEYS */;
UNLOCK TABLES;