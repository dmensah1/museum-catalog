SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';


CREATE SCHEMA IF NOT EXISTS `museum` DEFAULT CHARACTER SET utf8 ;
USE `museum` ;

CREATE TABLE IF NOT EXISTS `museum`.`Curator` (
  `curatorNo` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `location` VARCHAR(64) NULL,
  `theme` VARCHAR(64),
  PRIMARY KEY (`curatorNo`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`.`Museum` (
  `museumNo` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `location` VARCHAR(64) NOT NULL,
  `capacity` INT(5),
  PRIMARY KEY (`museumNo`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`.`Visitor` (
  `visitorNo` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `email` VARCHAR(64) NOT NULL,
  `password` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`visitorNo`),
  INDEX `visitorNo_idx` (`visitorNo` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`.`ArtifactDetails` (
`name` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE INDEX `name_UNIQUE` (`name` ASC),
  INDEX `name_idx` (`name` ASC))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`.`FavoriteDetails` (
  `dateAdded` DATE,
  `visitorNo` INT NOT NULL,
  `artifactName` VARCHAR(64) NOT NULL,
  PRIMARY KEY (`visitorNo`, `artifactName`),
  INDEX `visitorNo_idx` (`visitorNo` ASC),
  INDEX `artifactName_idx` (`artifactName` ASC),
  CONSTRAINT `visitorNo`
	FOREIGN KEY (`visitorNo`)
    REFERENCES `museum`.`Visitor` (`visitorNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `artifactName_FD`
	FOREIGN KEY (`artifactName`)
	REFERENCES `museum`.`ArtifactDetails` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`. `Theme` (
  `artifactName` VARCHAR(64) NOT NULL,
  `artifactTheme` VARCHAR(64),
  PRIMARY KEY (`artifactName`),
  INDEX `artifactName_idx` (`artifactName` ASC),
  CONSTRAINT `artifactName_Theme`
	FOREIGN KEY (`artifactName`)
    REFERENCES `museum`.`ArtifactDetails` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) 
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`. `Country` (
  `artifactName` VARCHAR(64) NOT NULL,
  `artifactCountry` VARCHAR(64),
  PRIMARY KEY (`artifactName`),
  INDEX `artifactName_idx` (`artifactName` ASC),
  CONSTRAINT `artifactName_Country`
	FOREIGN KEY (`artifactName`)
    REFERENCES `museum`.`ArtifactDetails` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) 
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS `museum`. `Time` (
  `artifactName` VARCHAR(64) NOT NULL,
  `timePeriod` VARCHAR(64),
  PRIMARY KEY (`artifactName`),
  INDEX `artifactName_idx` (`artifactName` ASC),
  CONSTRAINT `artifactName_Time` -- constraint name can't be same as primary key name
	FOREIGN KEY (`artifactName`)
    REFERENCES `museum`.`ArtifactDetails` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) 
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`. `AdmissionTicket` (
  `date` DATE NOT NULL,
  `admissionPrice` INT(4) NOT NULL,
  `museumNo` INT NOT NULL,
  `visitorNo` INT NOT NULL,
  PRIMARY KEY (`visitorNo`, `museumNo`),
  INDEX `visitorNo_idx` (`visitorNo` ASC),
  INDEX `museumNo_idx` (`museumNo` ASC),
  CONSTRAINT `musNo`
    FOREIGN KEY (`museumNo`)
    REFERENCES `museum`.`Museum` (`museumNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `visNo`
	FOREIGN KEY (`visitorNo`)
    REFERENCES `museum`.`Visitor` (`visitorNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) 
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`. `ExpositionDetails` (
  `dateAdded` DATE,
  `dateRemoved` DATE,
  `expoName` VARCHAR(64) NOT NULL,
  `artifactNo` INT NOT NULL,
  PRIMARY KEY (`expoName`, `artifactNo`),
  INDEX `artifactNo_idx` (`artifactNo` ASC),
  INDEX `exposition_idx` (`expoName` ASC),
  CONSTRAINT `expoName`
	FOREIGN KEY (`expoName`)
	REFERENCES `museum`. `Exposition` (`name`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `artifactNo`
	FOREIGN KEY (`artifactNo`)
    REFERENCES `museum`. `Artifact` (`artifactNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`. `Artifact` (
  `artifactNo` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(64) NOT NULL,
  `description` VARCHAR(128) NOT NULL,
  `country` VARCHAR(64),
  `theme` VARCHAR(64),
  `timePeriod` VARCHAR(64),
  PRIMARY KEY (`artifactNo`),
  CONSTRAINT `theme`
	FOREIGN KEY (`theme`)
	REFERENCES `museum`. `Theme` (`artifactName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `country`
	FOREIGN KEY (`country`)
    REFERENCES `museum`. `Country` (`artifactName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `timePeriod`
	FOREIGN KEY (`timePeriod`)
	REFERENCES `museum`. `Time` (`artifactName`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `museum`. `Exposition` (
  `name` VARCHAR(64) NOT NULL,
  `description` VARCHAR(120),
  `startDate` DATE,
  `endDate` DATE,
  `museumNo` INT,
  `curatorNo` INT,
  PRIMARY KEY (`name`),
  INDEX `exposition_idx` (`name` ASC),
  INDEX `curatorNo_idx` (`curatorNo` ASC),
  INDEX `museumNo_idx` (`museumNo` ASC),
  CONSTRAINT `curatorNo`
    FOREIGN KEY (`curatorNo`)
    REFERENCES `museum`.`Curator` (`curatorNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `museumNo`
    FOREIGN KEY (`museumNo`)
    REFERENCES `museum`.`Museum` (`museumNo`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;