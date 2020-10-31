


CREATE SCHEMA IF NOT EXISTS `museum` DEFAULT CHARACTER SET utf8 ;
USE `museum` ;

CREATE TABLE IF NOT EXISTS `museum`.`Curator` (
  `curatorNo` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `location` VARCHAR(64),
  PRIMARY KEY (`curatorNo`))
ENGINE = InnoDB;