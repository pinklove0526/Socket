-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 26, 2021 at 01:47 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

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

CREATE TABLE `books` (
  `ID` int(11) NOT NULL,
  `Name` text NOT NULL,
  `Type` text NOT NULL,
  `Author` text NOT NULL,
  `Year` year(4) NOT NULL,
  `NoiDung` longtext NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4;

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

CREATE TABLE `users` (
  `ID` int(11) NOT NULL,
  `name` text NOT NULL,
  `hash` text NOT NULL,
  `avatar` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`ID`, `name`, `hash`, `avatar`) VALUES
(2, 'dangnhat', '123456', ''),
(3, 'spencer', 'adcdef', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `books`
--
ALTER TABLE `books`
  ADD PRIMARY KEY (`ID`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `books`
--
ALTER TABLE `books`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
