--CREACIÓN DE LA BD
CREATE DATABASE db_zapatos;

--CREACIÓN DE TABLAS
CREATE TABLE `db_zapatos`.`marcas` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `nombre_marca` VARCHAR(50) NOT NULL UNIQUE,
  PRIMARY KEY (`id`)
);

CREATE TABLE `db_zapatos`.`zapatos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `modelo` VARCHAR(50) NOT NULL ,
  `talla` INT NOT NULL,
  `fecha_fabricacion` DATETIME NOT NULL,
  `disponibilidad` BIT NOT NULL,
  `id_marca` INT,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_zapatos__marcas` FOREIGN KEY (`id_marca`) REFERENCES `marcas` (`id`)
);

--INSERCIONES EN LAS TABLAS
INSERT INTO `db_zapatos`.`marcas` (`nombre_marca`) 
VALUES
('Nike'),
('Adidas'),
('Puma'),
('Reebok'),
('Vans');

INSERT INTO `db_zapatos`.`zapatos` (`modelo`, `talla`, `fecha_fabricacion`, `disponibilidad`, `id_marca`)
VALUES
('Air Max', 42, '2023-03-01 12:30:00', 1, 1),
('Ultraboost', 44, '2023-04-15 10:00:00', 1, 2),
('RS-X', 41, '2023-01-25 09:45:00', 0, 3),
('Classic Leather', 43, '2023-05-10 14:20:00', 1, 4),
('Old Skool', 40, '2023-06-20 16:50:00', 1, 5),
('Air Jordan', 42, '2023-07-02 11:10:00', 0, 1),
('Superstar', 39, '2023-08-11 13:30:00', 1, 2),
('Suede Classic', 38, '2023-09-05 15:05:00', 1, 3),
('Club C', 45, '2023-02-12 08:20:00', 0, 4),
('Sk8-Hi', 42, '2023-07-19 17:40:00', 1, 5);

--PROCEDIMIENTOS ALMACENADOS
DELIMITER $$
CREATE PROCEDURE `db_zapatos`.`proc_select_zapatos`()	
BEGIN

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
    	DECLARE v_error_message VARCHAR(255);
        GET DIAGNOSTICS CONDITION 1 v_error_message = MESSAGE_TEXT;
        SELECT CONCAT('Error: ', v_error_message) AS ErrorMensaje;
    END;

	SELECT z.id,
       z.modelo,
       z.talla,
       z.fecha_fabricacion,
       z.disponibilidad,
       z.id_marca,
       m.nombre_marca
    FROM db_zapatos.zapatos z
    INNER JOIN db_zapatos.marcas m ON m.id = z.id_marca;
END$$ 

DELIMITER $$
CREATE PROCEDURE proc_insertar_zapato(
    IN modelo VARCHAR(50), 
    IN talla INT, 
    IN fecha_fabricacion DATETIME, 
    IN disponibilidad BIT, 
    IN id_marca INT,
    OUT p_resultado VARCHAR(255)
)
BEGIN
    DECLARE v_error INT DEFAULT 0;

    DECLARE CONTINUE HANDLER FOR SQLEXCEPTION 
    BEGIN
        GET DIAGNOSTICS CONDITION 1 @p_error_message = MESSAGE_TEXT;
        SET p_resultado = CONCAT('Error: ', @p_error_message);
        SET v_error = 1;
    END;

    INSERT INTO zapatos (modelo, talla, fecha_fabricacion, disponibilidad, id_marca)
    VALUES (modelo, talla, fecha_fabricacion, disponibilidad, id_marca);

    IF v_error = 0 THEN
        SET p_resultado = 'Zapato Ingresado Correctamente';
    END IF;
END$$
