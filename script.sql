-- --------------------------------------------------------
-- Hôte:                         127.0.0.1
-- Version du serveur:           10.8.3-MariaDB - mariadb.org binary distribution
-- SE du serveur:                Win64
-- HeidiSQL Version:             12.0.0.6468
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- Listage de la structure de la base pour demo_cesi
CREATE DATABASE IF NOT EXISTS `demo_cesi` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `demo_cesi`;

-- Listage de la structure de table demo_cesi. books
CREATE TABLE IF NOT EXISTS `books` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(250) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4;

-- Listage des données de la table demo_cesi.books : ~0 rows (environ)
INSERT INTO `books` (`id`, `title`) VALUES
	(1, 'Les bases du hacking'),
	(2, '1984');

-- Listage de la structure de table demo_cesi. users
CREATE TABLE IF NOT EXISTS `users` (
  `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(50) NOT NULL,
  `password` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Index 2` (`login`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4;

-- Listage des données de la table demo_cesi.users : ~1 rows (environ)
INSERT INTO `users` (`id`, `login`, `password`) VALUES
	(4, 'toto', '$2b$12$9l.OpYaF8zkA.OZZcjnsE.f9kVTcq8XR5QdsFyH7g055S9p0fk39e');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

CREATE USER 'demo_cesi_user_bdd'@'localhost' IDENTIFIED BY 'demo_password';
GRANT USAGE ON *.* TO 'demo_cesi_user_bdd'@'localhost';
GRANT SELECT, DELETE, INSERT, UPDATE  ON `demo\_cesi`.* TO 'demo_cesi_user_bdd'@'localhost';
FLUSH PRIVILEGES;
