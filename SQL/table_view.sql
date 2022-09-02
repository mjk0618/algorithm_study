-- Active: 1661781168443@@127.0.0.1@3306@naver_db
DROP DATABASE IF EXISTS naver_db;
CREATE DATABASE naver_db;
USE naver_db;
DROP TABLE IF EXISTS member;
CREATE TABLE member
( mem_id        CHAR(8) NOT NULL PRIMARY KEY,
  mem_name      VARCHAR(10) NOT NULL,
  mem_number    TINYINT NOT NULL,
  addr          CHAR(2) NULL,
  phone1        CHAR(3) NULL,
  phone2        CHAR(8) NULL,
  height        TINYINT UNSIGNED NULL,
  debut_date    DATE NULL
);

USE naver_db;
DROP TABLE IF EXISTS buy;
CREATE TABLE buy
( num            INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  mem_id         CHAR(8) NOT NULL,
  prod_name      CHAR(6) NOT NULL,
  group_name     CHAR(4) NULL,
  price          INT UNSIGNED NOT NULL,
  amount         SMALLINT UNSIGNED NOT NULL,
  FOREIGN KEY(mem_id) REFERENCES member(mem_id)
);

INSERT INTO member VALUES('TWC', '트와이스', 9, '서울', '02', '11111111', 167, '2015-10-19');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남', '055', '22222222', 163, '2016-8-8');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기', '031', '33333333', 166, '2015-1-15');

INSERT INTO buy VALUES(NULL, 'BLK', '지갑', NULL, 30, 2);
INSERT INTO buy VALUES(NULL, "BLK", '맥북프로', '디지털', 1000, 1);
-- INSERT INTO buy VALUES(NULL, 'APN', '아이폰', '디지털', 200, 1);

-- 제약조건 Constraint: 데이터의 무결성을 지키기 위해 제한하는 조건
-- PRIMARY KEY/ FOREIGN KEY/ UNIQUE/ CHECK 제약조건 , DEFAULT 정의, NULL 값 허용 등

DESCRIBE member;
ALTER TABLE member
    ADD CONSTRAINT
    PRIMARY KEY (mem_id);

ALTER TABLE buy
    ADD CONSTRAINT
    FOREIGN KEY(mem_id)
    REFERENCES member(mem_id);

DESCRIBE buy;
SELECT M.mem_id, M.mem_name, B.prod_name
    FROM buy B
    INNER JOIN member M
    ON B.mem_id = M.mem_id;

-- PK-FK 관계 때문에 UPDATE, DELETE 불가
-- UPDATE member SET mem_id = 'PINK' WHERE mem_id = 'BLK';
-- DELETE FROM member WHERE mem_id = 'BLK';

-- 기준 테이블의 열이 변경되면 자동으로 참조 테이블의 열도 변경됨
DROP TABLE IF EXISTS buy;
CREATE TABLE buy
(   num         INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    mem_id      CHAR(8) NOT NULL,
    prod_name   CHAR(6) NOT NULL
);
DESC buy;

ALTER TABLE buy
    ADD CONSTRAINT
    FOREIGN KEY(mem_id) REFERENCES member(mem_id)
    ON UPDATE CASCADE
    ON DELETE CASCADE;

INSERT INTO buy VALUES(NULL, 'PINK', '지갑');
INSERT INTO buy VALUES(NULL, 'PINK', '맥북');

UPDATE member SET mem_id = 'BLK' WHERE mem_id = 'PINK';

SELECT * FROM buy;

SELECT M.mem_id, M.mem_name, B.prod_name
    FROM buy B
        INNER JOIN member M
        ON B.mem_id = M.mem_id;

-- 기타 제약 조건
-- 고유 키(Unique): 중복되지 않는 유일한 값 (NULL값 허용, NULL은 여러개여도 상관 없음)
DROP TABLE IF EXISTS buy, member;
CREATE TABLE member
( mem_id        CHAR(8) NOT NULL PRIMARY KEY,
  mem_name      VARCHAR(10) NOT NULL,
  height        TINYINT UNSIGNED NULL,
  email         CHAR(30) NULL UNIQUE
  );

INSERT INTO member VALUES('BLK', '블랙핑크', 163, 'pink@gmail.com');
INSERT INTO member VALUES('TWC', '트와이스', 167, NULL);
-- INSERT INTO member VALUES('APN', '에이핑크', 164, 'pink@gmail.com'); 오류

-- 체크(Check): 입력되는 데이터를 점검하는 기능
DROP TABLE IF EXISTS member;
CREATE TABLE member
(mem_id         CHAR(8) NOT NULL PRIMARY KEY,
 mem_name       VARCHAR(10) NOT NULL,
 height         TINYINT UNSIGNED NULL CHECK (height >= 100),
 phone1         CHAR(3) NULL
 );

INSERT INTO member VALUES('BLK', '블랙핑크', 163, NULL);
-- INSERT INTO member VALUES('TWC', '트와이스', 99, NULL); 오류

ALTER TABLE member
    ADD CONSTRAINT
    CHECK (phone1 IN ('02', '031', '032', '054', '055', '061'));

INSERT INTO member VALUES('TWC', '트와이스', 167, '02');
-- INSERT INTO member VALUES('OMY', '오마이걸', 167, '010'); 오류

-- 기본값 정의(Default): 값을 입력하지 않았을 때 자동으로 입력될 값을 미리 지정
DROP TABLE IF EXISTS member;
CREATE TABLE member
(mem_id     CHAR(8) NOT NULL PRIMARY KEY,
 mem_name   VARCHAR(10) NOT NULL,
 height     TINYINT UNSIGNED NULL DEFAULT 160,
 phone1     CHAR(3) NULL
 );

ALTER TABLE member
    ALTER COLUMN phone1 SET DEFAULT '02';

INSERT INTO member VALUES('RED', '레드벨벳', 161, '054');
INSERT INTO member VALUES('SPC', '우주소녀', default, default);
SELECT * FROM member;

-- 널 값 허용(NULL): NULL / NOT NULL 공백이나 0과는 다른 의미


-- 가상의 테이블- 뷰(view): 데이터베이스 개체 중 하나
USE market_db;
SELECT mem_id, mem_name, addr FROM member;

CREATE VIEW v_member
AS
    SELECT mem_id, mem_name, addr FROM member;

SELECT * FROM v_member;

SELECT mem_name, addr FROM v_member
    WHERE addr IN ('서울', '경기');

CREATE VIEW v_memberbuy
AS
    SELECT B.mem_id, M.mem_name, B.prod_name, M.addr, CONCAT(M.phone1, M.phone2) '연락처'
    FROM buy B
        INNER JOIN member M
        ON B.mem_id = M.mem_id;

SELECT * FROM v_memberbuy WHERE mem_name = '블랙핑크';

USE market_db;
CREATE VIEW v_viewtest1
AS
    SELECT B.mem_id 'Member ID', M.mem_name AS 'Member Name',
           B.prod_name "Product Name", CONCAT(M.phone1, M.phone2) AS "Office Phone"

           FROM buy B
                INNER JOIN member M
                ON B.mem_id = M.mem_id;

SELECT DISTINCT `Member ID`, `Member Name` FROM v_viewtest1;

ALTER VIEW v_viewtest1
AS
    SELECT B.mem_id '회원 아이디', M.mem_name AS '회원 이름',
        B.prod_name = "제품 이름", CONCAT(M.phone1, M.phone2) AS "연락처"
        FROM buy B
            INNER JOIN member M
            ON B.mem_id = M.mem_id;

SELECT DISTINCT `회원 아이디`, `회원 이름` FROM v_viewtest1;

DROP VIEW v_viewtest1;

CREATE OR REPLACE VIEW v_viewtest2
AS
    SELECT mem_id, mem_name, addr FROM member;
-- DROP VIEW와 CREATE VIEW를 연속으로 작성한 효과(REPLACE)

DESCRIBE v_viewtest2;
-- DESC v_viewtest2; 같음
-- view는 PK 등의 정보는 주지 않음

DESCRIBE member;

SHOW CREATE VIEW v_viewtest2;

UPDATE v_member SET addr = '부산' WHERE mem_id = 'BLK';
-- INSERT INTO v_member(mem_id, mem_name, addr) VALUES('BTS', '방탄소년단', '경기'); 오류
-- v_member(뷰)가 참조하는 member(테이블)의 number열은 NOT NULL이라 반드시 입력해줘야 하는데
-- mem_number 열을 참조하고 있지 않으므로 값을 입력할 방법이 없다
-- 따라서 뷰를 재정의 하거나, member 테이블에서 열의 속성을 NULL로 바꾸거나, 기본값(Default)를 설정해야 한다

CREATE VIEW v_height167
AS
    SELECT * FROM member WHERE height >= 167;

SELECT * FROM v_height167;
DELETE FROM v_height167 WHERE height < 167;
INSERT INTO v_height167 VALUES('TRA', '티아라', 6, '서울', NULL, NULL, 159, '2005-01-01');
-- 키가 167이하인데 행은 생성되었다?
SELECT * FROM v_height167;
-- SELECT로 확인해보면 찾을 수 없다

ALTER VIEW v_height167
AS
    SELECT * FROM member WHERE height >= 167
        WITH CHECK OPTION; -- 뷰에서 설정된 값의 범위가 벗어나는 값은 입력되지 않도록 한다

-- INSERT INTO v_height167 VALUES('TOB', '텔레토비', 4, '영국', NULL, NULL, 140, '1995-01-01'); 오류

-- 복합 뷰(두 개 이상의 테이블로 만든 뷰(조인))
-- 복합 뷰는 읽기 전용이며, 데이터를 입력/수정/삭제할 수 없음
CREATE VIEW v_complex
AS
    SELECT B.mem_id, M.mem_name, B.prod_name, M.addr
        FROM buy B
            INNER JOIN member M
            ON B.mem_id = M.mem_id;

DROP TABLE IF EXISTS buy, member;
-- SELECT * FROM v_height167; 오류(원본 테이블이 삭제되었기 때문)

CHECK TABLE v_height167;
-- 테이블은 뷰가 참조하고 있어도 삭제된다.