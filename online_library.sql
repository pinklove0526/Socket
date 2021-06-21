-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Jun 21, 2021 at 08:11 AM
-- Server version: 8.0.21
-- PHP Version: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `online_library`
--

-- --------------------------------------------------------

--
-- Table structure for table `books`
--

DROP TABLE IF EXISTS `books`;
CREATE TABLE IF NOT EXISTS `books` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `Type` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `Author` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `Year` year NOT NULL,
  `NoiDung` longtext COLLATE utf8mb4_vietnamese_ci NOT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;

--
-- Dumping data for table `books`
--

INSERT INTO `books` (`ID`, `Name`, `Type`, `Author`, `Year`, `NoiDung`) VALUES
(1, 'Mein kampf', 'Political', 'Fuhrer', 1925, 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ut facilis error sapiente nisi id delectus atque eligendi libero, quo at provident voluptatum ipsam esse ratione! Neque in nesciunt vero aut.'),
(2, 'Metamorphosis', 'Drama', 'Shindo L', 2015, 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ut facilis error sapiente nisi id delectus atque eligendi libero, quo at provident voluptatum ipsam esse ratione! Neque in nesciunt vero aut.'),
(3, 'Theory of everything', 'Science', 'Stephen Hawking', 2002, 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ut facilis error sapiente nisi id delectus atque eligendi libero, quo at provident voluptatum ipsam esse ratione! Neque in nesciunt vero aut.'),
(4, 'Fate Zero', 'Light Novel', 'Gen Urobachi', 2009, 'Lorem ipsum dolor sit, amet consectetur adipisicing elit. Ut facilis error sapiente nisi id delectus atque eligendi libero, quo at provident voluptatum ipsam esse ratione! Neque in nesciunt vero aut.'),
(5, 'Grade 12 Chemistry', 'Education', 'Ministry of Education and Training', 2001, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Tempora et doloremque maxime ipsam culpa natus animi impedit, similique quas! Dolores modi molestias est, nostrum nisi sapiente ut unde accusamus doloribus.');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
CREATE TABLE IF NOT EXISTS `users` (
  `User ID` int NOT NULL,
  `User Name` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `User hash` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  `Avatar` text CHARACTER SET utf8mb4 COLLATE utf8mb4_vietnamese_ci NOT NULL,
  PRIMARY KEY (`User ID`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_vietnamese_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
