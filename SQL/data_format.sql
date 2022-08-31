-- Active: 1661781168443@@127.0.0.1@3306@market_db
USE market_db;
CREATE TABLE hongong4 (
    tinyint_col TINYINT,
    smaillint_col SMALLINT,
    int_col INT,
    bigint_col BIGINT
);
INSERT INTO hongong4 VALUES(127, 32767, 2147483647, 9000000000000000000);
-- Error: INSERT INTO hongong4 VALUES(128, 32768, 2147483648, 90000000000000000000)
SELECT * FROM hongong4;
CREATE DATABASE netflix_db;
USE netflix_db;
CREATE TABLE movie(
    movie_id INT,
    movie_title VARCHAR(30),
    movie_director VARCHAR(20),
    movie_star VARCHAR(20),
    movie_script LONGTEXT,
    movie_film LONGBLOB
);
SELECT * FROM movie;

SET @myVar1 = 5;
SELECT @myVar1;
SET @txt = '가수이름 ==>';
SET @height = 166;
USE market_db;
SELECT @txt, mem_name FROM member WHERE height > @height;
SET @count = 3;
PREPARE mySQL FROM 'SELECT mem_name, height FROM member ORDER BY height LIMIT ?';
EXECUTE mySQL USING @count;
-- LIMIT에는 변수를 사용하지 못하기 떄문에 PREPARE / EXECUTE 문을 사용
SELECT AVG(price) AS '평균가격' FROM buy;
SELECT CAST(AVG(price) AS SIGNED) '평균가격' FROM buy;
SELECT CAST('2022$12$31' AS DATE);
SELECT num, CONCAT(CAST(price AS CHAR), 'X', CAST(amount AS CHAR), '=')
    '가격X수량', price * amount '구매액'
    FROM buy;
