-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema smm
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `smm` ;

-- -----------------------------------------------------
-- Schema smm
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `smm` DEFAULT CHARACTER SET utf8 ;
USE `smm` ;

-- -----------------------------------------------------
-- Table `smm`.`players`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smm`.`players` ;

CREATE TABLE IF NOT EXISTS `smm`.`players` (
  `p_id` INT NOT NULL AUTO_INCREMENT,
  `player_id` VARCHAR(45) NOT NULL,
  `image` VARCHAR(100) NULL DEFAULT NULL,
  `flag` VARCHAR(3) NULL DEFAULT NULL,
  `player_name` VARCHAR(45) NULL DEFAULT NULL,
  PRIMARY KEY (`p_id`),
  UNIQUE INDEX `p_id` (`p_id` ASC))
ENGINE = InnoDB
AUTO_INCREMENT = 884394
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smm`.`difficulty`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smm`.`difficulty` ;

CREATE TABLE IF NOT EXISTS `smm`.`difficulty` (
  `difficulty_id` TINYINT(1) NOT NULL,
  `difficulty_type` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`difficulty_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `smm`.`style`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smm`.`style` ;

CREATE TABLE IF NOT EXISTS `smm`.`style` (
  `style_id` INT NOT NULL AUTO_INCREMENT,
  `style_name` VARCHAR(15) NOT NULL,
  PRIMARY KEY (`style_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `smm`.`courses`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smm`.`courses` ;

CREATE TABLE IF NOT EXISTS `smm`.`courses` (
  `m_id` INT NOT NULL,
  `map_id` VARCHAR(20) NOT NULL,
  `difficulty_id` TINYINT(1) NULL,
  `style_id` INT NULL,
  `maker` INT NULL DEFAULT NULL,
  `title` VARCHAR(45) NULL DEFAULT NULL,
  `thumbnail` VARCHAR(150) NULL DEFAULT NULL,
  `image` VARCHAR(150) NULL DEFAULT NULL,
  `creation` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`m_id`),
  UNIQUE INDEX `m_id` (`m_id` ASC),
  INDEX `maker` (`maker` ASC),
  INDEX `fk_courses_difficulty1_idx` (`difficulty_id` ASC),
  INDEX `fk_courses_style1_idx` (`style_id` ASC),
  CONSTRAINT `courses_ibfk_1`
    FOREIGN KEY (`maker`)
    REFERENCES `smm`.`players` (`p_id`),
  CONSTRAINT `fk_courses_difficulty1`
    FOREIGN KEY (`difficulty_id`)
    REFERENCES `smm`.`difficulty` (`difficulty_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_courses_style1`
    FOREIGN KEY (`style_id`)
    REFERENCES `smm`.`style` (`style_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 115056
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smm`.`course_meta`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smm`.`course_meta` ;

CREATE TABLE IF NOT EXISTS `smm`.`course_meta` (
  `catch` BIGINT(1) NOT NULL,
  `m_id` INT NOT NULL,
  `first_clear` INT NULL DEFAULT NULL,
  `game_tag` VARCHAR(20) NULL DEFAULT NULL,
  `stars` INT NULL DEFAULT NULL,
  `num_of_players` INT NULL DEFAULT NULL,
  `sharing_num` INT NULL DEFAULT NULL,
  `clears_num` INT NULL DEFAULT NULL,
  `attemps_num` INT NULL DEFAULT NULL,
  PRIMARY KEY (`catch`, `m_id`),
  INDEX `fk_courses_has_players1_players4_idx` (`first_clear` ASC),
  INDEX `fk_courses_has_players1_courses4_idx` (`m_id` ASC),
  CONSTRAINT `fk_courses_has_players1_courses4`
    FOREIGN KEY (`m_id`)
    REFERENCES `smm`.`courses` (`m_id`),
  CONSTRAINT `fk_courses_has_players1_players4`
    FOREIGN KEY (`first_clear`)
    REFERENCES `smm`.`players` (`p_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `smm`.`game_play_properties_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smm`.`game_play_properties_type` ;

CREATE TABLE IF NOT EXISTS `smm`.`game_play_properties_type` (
  `type_id` TINYINT(1) NOT NULL,
  `type_name` VARCHAR(10) NULL,
  PRIMARY KEY (`type_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `smm`.`game_play_properties`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `smm`.`game_play_properties` ;

CREATE TABLE IF NOT EXISTS `smm`.`game_play_properties` (
  `m_id` INT NOT NULL,
  `p_id` INT NOT NULL,
  `catch` DATETIME NULL,
  `record` INT NULL,
  `properties_type_id` TINYINT(1) NOT NULL,
  PRIMARY KEY (`m_id`, `p_id`, `properties_type_id`),
  INDEX `fk_courses_has_players_players1_idx` (`p_id` ASC),
  INDEX `fk_courses_has_players_courses1_idx` (`m_id` ASC),
  INDEX `fk_game_play_properties_game_play_properties_type1_idx` (`properties_type_id` ASC),
  CONSTRAINT `fk_courses_has_players_courses1`
    FOREIGN KEY (`m_id`)
    REFERENCES `smm`.`courses` (`m_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_courses_has_players_players1`
    FOREIGN KEY (`p_id`)
    REFERENCES `smm`.`players` (`p_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_game_play_properties_game_play_properties_type1`
    FOREIGN KEY (`properties_type_id`)
    REFERENCES `smm`.`game_play_properties_type` (`type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
