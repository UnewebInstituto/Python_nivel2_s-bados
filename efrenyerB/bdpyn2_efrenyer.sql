-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 23-11-2024 a las 23:03:32
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bdpyn2_efrenyer`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `personas`
--

CREATE TABLE `personas` (
  `id` int(11) NOT NULL,
  `cedula` varchar(10) DEFAULT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  `apellido` varchar(30) DEFAULT NULL,
  `direccion` text DEFAULT NULL,
  `fechanac` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `personas`
--

INSERT INTO `personas` (`id`, `cedula`, `nombre`, `apellido`, `direccion`, `fechanac`) VALUES
(1, 'V1234567', 'ANA', 'VAZQUEZ', 'SANTA FE', '1960-08-25'),
(2, 'V1234568', 'YOLANDA', 'TORTOZA', 'CATIA LA MAR', '1975-09-15'),
(3, 'V1234569', 'MARIA', 'PEREZ', 'EL HATILLO', '1975-09-29'),
(4, 'V1234565', 'LIBIA', 'COLS', 'GUARENAS', '1980-06-15'),
(5, 'E81001002', 'BRUCE', 'WILLIS', 'LOS ANGELES', '1950-02-01'),
(6, 'V9876543', 'NORMA', 'GAINFA', 'EL VALLE', '1972-07-17'),
(8, '30663550', 'Darlenis', 'Perez', 'Chacao', '2001-08-01'),
(9, '30878900', 'Jose', 'Ramirez', 'Palo Verde', '1960-07-05'),
(10, '29678076', 'Kerwin', 'Bencomo', 'Guatire', '2003-08-10');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `personas`
--
ALTER TABLE `personas`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `personas`
--
ALTER TABLE `personas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
