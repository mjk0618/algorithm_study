-- Active: 1661781168443@@127.0.0.1@3306@market_db
USE market_db;
CREATE TABLE hongong1 (toy_id INT, toy_name CHAR(4), age INT);
INSERT INTO hongong1 VALUES(1, '우디', 25);
INSERT INTO hongong1 (toy_id, toy_name) VALUES (2, '버즈'); 
SELECT * FROM hongong1;
INSERT INTO hongong1 (toy_name, age, toy_id) VALUES ('제시', 20, 3);
CREATE TABLE hongong2 (
	toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
SELECT * FROM hongong2;
INSERT INTO hongong2 VALUES (NULL, '보핍', 25);
INSERT INTO hongong2 VALUES (NULL, '슬링키', 22);
INSERT INTO hongong2 VALUES (NULL, '렉스', 21);
SELECT LAST_INSERT_ID();
ALTER TABLE hongong2 AUTO_INCREMENT=100;
INSERT INTO hongong2 VALUES (NULL, '재남', 35);
SELECT * FROM hongong2;
CREATE TABLE hongong3 (
    toy_id INT AUTO_INCREMENT PRIMARY KEY,
    toy_name CHAR(4),
    age INT);
ALTER TABLE hongong3 AUTO_INCREMENT=1000;
SET @@auto_increment_increment=3;

SHOW GLOBAL VARIABLES;
INSERT INTO hongong3 VALUES (NULL, '토마스', 20);
INSERT INTO hongong3 VALUES (NULL, '제임스', 23);
INSERT INTO hongong3 VALUES (NULL, '고든', 25);
SELECT * FROM hongong3;
SELECT COUNT(*) FROM world.city;

DESC world.city;
SELECT * FROM world.city WHERE Population >= 500 ORDER BY Population DESC LIMIT 30;
CREATE TABLE city_popul (city_name CHAR(35), population INT);
INSERT INTO city_popul
    SELECT Name, population FROM world.city;
-- SELECT * FROM city_popul
UPDATE city_popul
    SET city_name = '서울'
    WHERE city_name = 'Seoul';
SELECT * FROM city_popul WHERE city_name = '서울';
UPDATE city_popul
    SET city_name = '뉴욕', population = 0
    WHERE city_name = 'New York';
SELECT * FROM city_popul WHERE city_name = '뉴욕';
UPDATE city_popul
    SET population = population / 10000;
SELECT * FROM city_popul LIMIT 5;
DELETE FROM hongong2 WHERE toy_name = '재남';

DELETE FROM city_popul
    WHERE city_name LIKE 'NEW ______';
DELETE FROM city_popul
    WHERE city_name LIKE 'NEW%';

CREATE TABLE big_table (SELECT * FROM world.city, sakila.country);
TRUNCATE TABLE big_table;
SELECT * FROM big_table;