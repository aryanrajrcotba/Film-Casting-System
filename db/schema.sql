CREATE DATABASE IF NOT EXISTS film_casting;
USE film_casting;

CREATE TABLE Film (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(100),
    release_year INT
);

CREATE TABLE Actor (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    gender VARCHAR(10),
    experience INT,
    contact_info VARCHAR(255)
);

CREATE TABLE Role (
    id INT AUTO_INCREMENT PRIMARY KEY,
    role_name VARCHAR(255),
    description TEXT,
    requirements TEXT
);

CREATE TABLE Casting (
    film_id INT,
    actor_id INT,
    role_id INT,
    audition_date DATE,
    status VARCHAR(50),
    PRIMARY KEY (film_id, actor_id, role_id),
    FOREIGN KEY (film_id) REFERENCES Film(id),
    FOREIGN KEY (actor_id) REFERENCES Actor(id),
    FOREIGN KEY (role_id) REFERENCES Role(id)
);

CREATE TABLE Director (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    contact_info VARCHAR(255)
);

CREATE TABLE Crew (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    department VARCHAR(100),
    role_in_production VARCHAR(255)
);
