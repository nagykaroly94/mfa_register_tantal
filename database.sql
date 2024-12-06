CREATE DATABASE tantal;
USE DATABASE tantal;
CREATE TABLE `adatok` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nev` varchar(255) NOT NULL,
  `adoszam` varchar(50) NOT NULL,
  `felhasznalonev` varchar(255) NOT NULL,
  `jelszo` varchar(255) NOT NULL,
  `telefonszam` varchar(20) NOT NULL,
  `emailcim` varchar(255) DEFAULT NULL,
  `torlokod` varchar(50) DEFAULT NULL,
  `onlineszamla_nev` varchar(255) DEFAULT NULL,
  `onlineszamla_jelszo` varchar(255) DEFAULT NULL,
  `qr_kod` text,
  `ugyintezo` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
  );