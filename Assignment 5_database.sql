CREATE DATABASE players_database;
USE players_database;

-- Creating table 
CREATE TABLE players (
  name VARCHAR(100),
  address VARCHAR(200)
);

-- Inserting palyers info
INSERT INTO players (name,address)
VALUES ('Carlos Alzaraz', 'Murcia, Span');
INSERT INTO players (name, address)
VALUES ('Jannik Sinner', 'San Candido, Italy');
INSERT INTO players (name, address)
VALUES ('Ben Shelton', 'Miami, Florida');
INSERT INTO players (name, address)
VALUES ('Diego Arzaluz', 'Puebla, Mexico');

-- Printing table
SELECT * FROM players
