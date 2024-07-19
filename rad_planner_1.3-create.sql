-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema rad_planner
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `rad_planner` ;

-- -----------------------------------------------------
-- Schema rad_planner
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `rad_planner` ;
USE `rad_planner` ;

-- -----------------------------------------------------
-- Table `rad_planner`.`department`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`department` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`department` (
  `department_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `department_name` VARCHAR(200) NOT NULL,
  PRIMARY KEY (`department_id`),
  UNIQUE INDEX `department_name_UNIQUE` (`department_name` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`subject_code`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`subject_code` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`subject_code` (
  `subject_code_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `subject_code_string` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`subject_code_id`),
  UNIQUE INDEX `subject_code_string_UNIQUE` (`subject_code_string` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`course`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`course` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`course` (
  `course_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `course_code` VARCHAR(45) NOT NULL,
  `course_title` VARCHAR(45) NOT NULL,
  `course_credit_hrs` INT(2) NOT NULL,
  `course_url` VARCHAR(200) NULL,
  `department_id` INT UNSIGNED NOT NULL,
  `subject_code_id` INT UNSIGNED NOT NULL,
  `course_description` TEXT(42069) NULL,
  `course_grading_type` VARCHAR(45) NULL,
  `course_unique_requirements` TEXT(1069) NULL,
  `course_can_audit` TINYINT(1) NULL,
  `course_contact_hours` TEXT(690) NULL,
  `course_learning_outcomes` TEXT(5069) NULL,
  PRIMARY KEY (`course_id`),
  INDEX `fk_course_department1_idx` (`department_id` ASC) VISIBLE,
  INDEX `fk_course_subject_code1_idx` (`subject_code_id` ASC) VISIBLE,
  CONSTRAINT `fk_course_department1`
    FOREIGN KEY (`department_id`)
    REFERENCES `rad_planner`.`department` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_course_subject_code1`
    FOREIGN KEY (`subject_code_id`)
    REFERENCES `rad_planner`.`subject_code` (`subject_code_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`certificate`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`certificate` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`certificate` (
  `certificate_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `certificate_name` VARCHAR(45) NOT NULL,
  `certificate_code` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`certificate_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`degree_type`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`degree_type` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`degree_type` (
  `degree_type_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `degree_type_name` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`degree_type_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`degree`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`degree` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`degree` (
  `degree_id` INT NOT NULL,
  `degree_name` VARCHAR(45) NOT NULL,
  `degree_type_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`degree_id`),
  INDEX `fk_degree_degree_type1_idx` (`degree_type_id` ASC) VISIBLE,
  CONSTRAINT `fk_degree_degree_type1`
    FOREIGN KEY (`degree_type_id`)
    REFERENCES `rad_planner`.`degree_type` (`degree_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`prereq`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`prereq` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`prereq` (
  `prereq_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prereq_relationship` TINYINT(1) NOT NULL,
  `prereq_type` VARCHAR(45) NOT NULL,
  `prereq_amount_min` INT(8) NOT NULL,
  `prereq_specific` TINYINT(1) NOT NULL,
  `prereq_amount_max` INT(8) NULL,
  PRIMARY KEY (`prereq_id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`certificate_prereq`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`certificate_prereq` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`certificate_prereq` (
  `certificate_prereq_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prereq_id` INT UNSIGNED NOT NULL,
  `certificate_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`certificate_prereq_id`),
  INDEX `fk_certificate_prereq_prereq1_idx` (`prereq_id` ASC) VISIBLE,
  INDEX `fk_certificate_prereq_certificate1_idx` (`certificate_id` ASC) VISIBLE,
  CONSTRAINT `fk_certificate_prereq_prereq1`
    FOREIGN KEY (`prereq_id`)
    REFERENCES `rad_planner`.`prereq` (`prereq_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_certificate_prereq_certificate1`
    FOREIGN KEY (`certificate_id`)
    REFERENCES `rad_planner`.`certificate` (`certificate_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`prereq_to_parent`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`prereq_to_parent` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`prereq_to_parent` (
  `prereq_to_parent_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prereq_id` INT UNSIGNED NOT NULL,
  `course_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`prereq_to_parent_id`),
  INDEX `fk_prereq_to_parent_prereq1_idx` (`prereq_id` ASC) VISIBLE,
  INDEX `fk_prereq_to_parent_course1_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `fk_prereq_to_parent_prereq1`
    FOREIGN KEY (`prereq_id`)
    REFERENCES `rad_planner`.`prereq` (`prereq_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_prereq_to_parent_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `rad_planner`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`prereq_to_child`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`prereq_to_child` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`prereq_to_child` (
  `prereq_to_child_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prereq_id` INT UNSIGNED NOT NULL,
  `course_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`prereq_to_child_id`),
  INDEX `fk_prereq_to_child_prereq1_idx` (`prereq_id` ASC) VISIBLE,
  INDEX `fk_prereq_to_child_course1_idx` (`course_id` ASC) VISIBLE,
  CONSTRAINT `fk_prereq_to_child_prereq1`
    FOREIGN KEY (`prereq_id`)
    REFERENCES `rad_planner`.`prereq` (`prereq_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_prereq_to_child_course1`
    FOREIGN KEY (`course_id`)
    REFERENCES `rad_planner`.`course` (`course_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`module`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`module` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`module` (
  `module_id` INT NOT NULL,
  `degree_id` INT NOT NULL,
  PRIMARY KEY (`module_id`),
  INDEX `fk_module_degree1_idx` (`degree_id` ASC) VISIBLE,
  CONSTRAINT `fk_module_degree1`
    FOREIGN KEY (`degree_id`)
    REFERENCES `rad_planner`.`degree` (`degree_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`module_prereq`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`module_prereq` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`module_prereq` (
  `module_prereq_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prereq_id` INT UNSIGNED NOT NULL,
  `module_id` INT NOT NULL,
  PRIMARY KEY (`module_prereq_id`),
  INDEX `fk_module_prereq_prereq1_idx` (`prereq_id` ASC) VISIBLE,
  INDEX `fk_module_prereq_module1_idx` (`module_id` ASC) VISIBLE,
  CONSTRAINT `fk_module_prereq_prereq1`
    FOREIGN KEY (`prereq_id`)
    REFERENCES `rad_planner`.`prereq` (`prereq_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_module_prereq_module1`
    FOREIGN KEY (`module_id`)
    REFERENCES `rad_planner`.`module` (`module_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`module_certificate`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`module_certificate` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`module_certificate` (
  `module_certificate_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `certificate_id` INT UNSIGNED NOT NULL,
  `module_id` INT NOT NULL,
  PRIMARY KEY (`module_certificate_id`),
  INDEX `fk_module_certificate_certificate1_idx` (`certificate_id` ASC) VISIBLE,
  INDEX `fk_module_certificate_module1_idx` (`module_id` ASC) VISIBLE,
  CONSTRAINT `fk_module_certificate_certificate1`
    FOREIGN KEY (`certificate_id`)
    REFERENCES `rad_planner`.`certificate` (`certificate_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_module_certificate_module1`
    FOREIGN KEY (`module_id`)
    REFERENCES `rad_planner`.`module` (`module_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`prereq_subject_code`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`prereq_subject_code` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`prereq_subject_code` (
  `prereq_subject_code_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `subject_code_id` INT UNSIGNED NOT NULL,
  `prereq_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`prereq_subject_code_id`),
  INDEX `fk_prereq_subject_code_subject_code1_idx` (`subject_code_id` ASC) VISIBLE,
  INDEX `fk_prereq_subject_code_prereq1_idx` (`prereq_id` ASC) VISIBLE,
  CONSTRAINT `fk_prereq_subject_code_subject_code1`
    FOREIGN KEY (`subject_code_id`)
    REFERENCES `rad_planner`.`subject_code` (`subject_code_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_prereq_subject_code_prereq1`
    FOREIGN KEY (`prereq_id`)
    REFERENCES `rad_planner`.`prereq` (`prereq_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `rad_planner`.`prereq_to_prereq`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `rad_planner`.`prereq_to_prereq` ;

CREATE TABLE IF NOT EXISTS `rad_planner`.`prereq_to_prereq` (
  `prereq_to_prereq_id` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `prereq_parent_id` INT UNSIGNED NOT NULL,
  `prereq_child_id` INT UNSIGNED NOT NULL,
  PRIMARY KEY (`prereq_to_prereq_id`),
  INDEX `fk_prereq_to_prereq_prereq1_idx` (`prereq_parent_id` ASC) VISIBLE,
  INDEX `fk_prereq_to_prereq_prereq2_idx` (`prereq_child_id` ASC) VISIBLE,
  CONSTRAINT `fk_prereq_to_prereq_prereq1`
    FOREIGN KEY (`prereq_parent_id`)
    REFERENCES `rad_planner`.`prereq` (`prereq_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_prereq_to_prereq_prereq2`
    FOREIGN KEY (`prereq_child_id`)
    REFERENCES `rad_planner`.`prereq` (`prereq_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
