create database `Python`;

use `Python`;



CREATE TABLE `pessoa` (
  `id` int(50) PRIMARY KEY NOT NULL AUTO_INCREMENT,
  `nome` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL
);


INSERT INTO `pessoa` (`id`, `nome`, `email`) VALUES
(1, 'Thiago', 'thiago@email'),
(2, 'Maria', 'maria@email'),
(3, 'Carla', 'carla@email');



create table `Vendas` (

    `produto` varchar(10),
    `valor` int(10)

);

insert into `Vendas` (`produto`,`valor`) values 
('CarroA', '30000'),
('CarroB', '40000'),
('MotoA', '3000'),
('MotoB', '2500'),
('MotoC', '5500');