-- Active: 1661781168443@@127.0.0.1@3306@market_db
-- 인덱스(index): 데이터를 빠르게 찾을 수 있도록 도와주는 도구
-- 클러스터형 인덱스(clustured index): 기본키로 지정하면 자동 생성, 테이블 당 1개, 자동 정렬
-- 보조 인덱스(secondary index): 고유 키로 지정하면 자동 생성, 여러개 만들 수 있으나 자동정렬x

USE market_db;
SELECT * FROM member;

CREATE TABLE table1 (
    col1 INT PRIMARY KEY,
    col2 INT,
    col3 INT
);
SHOW INDEX FROM table1;

CREATE TABLE table2(
    col1 INT PRIMARY KEY,
    col2 INT UNIQUE,
    col3 INT UNIQUE
);
SHOW INDEX FROM table2;

DROP TABLE IF EXISTS buy, member;
CREATE TABLE member(
    mem_id      CHAR(8),
    mem_name    VARCHAR(10),
    mem_number  INT,
    addr        CHAR(2)
);

INSERT INTO member VALUES('TWC', '트와이스', 9, '서울');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기');
INSERT INTO member VALUES('OMY', '오마이걸', 7, '서울');
SELECT * FROM member;

ALTER TABLE member
    ADD CONSTRAINT
    PRIMARY KEY (mem_id);
SELECT * FROM member;

ALTER TABLE member DROP PRIMARY KEY;
ALTER TABLE member
    ADD CONSTRAINT
    PRIMARY KEY (mem_name);
SELECT * FROM member;

INSERT INTO member VALUES('GRL', '소녀시대', 8, '서울');
SELECT * FROM member;

DROP TABLE IF EXISTS member;
CREATE TABLE member(
    mem_id      CHAR(8),
    mem_name    VARCHAR(10),
    mem_number  INT,
    addr        CHAR(2)
);

INSERT INTO member VALUES('TWC', '트와이스', 9, '서울');
INSERT INTO member VALUES('BLK', '블랙핑크', 4, '경남');
INSERT INTO member VALUES('WMN', '여자친구', 6, '경기');
INSERT INTO member VALUES('OMY', '오마이걸', 7, '서울');
SELECT * FROM member;

ALTER TABLE member
    ADD CONSTRAINT
    UNIQUE (mem_id);
SELECT * FROM member;

ALTER TABLE member
    ADD CONSTRAINT
    UNIQUE (mem_name);
SELECT * FROM member;
INSERT INTO member VALUES('GRL', '소녀시대', 8, '서울');
SELECT * FROM member;

SHOW INDEX FROM member;


-- 인덱스의 내부 작동 원리
-- 균형 트리(Balanced-tree, B-tree)구조에서 데이터가 저장되는 공간은 노드(Node)
-- 루트 노드(Root Node), 리프 노드(Leaf Node), 중간 노드(Internal Node)
-- MySQL에서는 노드를 페이지(page)라고 부름
-- 최소한의 저장 단위로, 16Kbyte(16384byte)의 크기를 가짐
-- 데이터를 1 건만 입력해도 1페이지가 필요하다
-- 인덱스는 균형 트리로 구성되어 있어 SELECT의 속도를 향상시킬 수 있다
-- 하지만 데이터 변경 작업(INSERT, UPDATE, DELETE)시에는 느려질 수 있다
-- 페이지 분할: 새로운 페이지를 준비해서 데이터를 나누는 작업


-- 클러스터형 인덱스 구성하기
CREATE TABLE cluster(  -- 클러스터형 인덱스를 테스트하기 위한 테이블
    mem_id      CHAR(8),
    mem_name    VARCHAR(10)
);

INSERT INTO cluster VALUES('TWC', '트와이스');
INSERT INTO cluster VALUES('BLK', '블랙핑크');
INSERT INTO cluster VALUES('WMN', '여자친구');
INSERT INTO cluster VALUES('OMY', '오마이걸');
INSERT INTO cluster VALUES('GRL', '소녀시대');
INSERT INTO cluster VALUES('ITZ', '잇지');
INSERT INTO cluster VALUES('RED', '레드벨벳');
INSERT INTO cluster VALUES('APN', '에이핑크');
INSERT INTO cluster VALUES('SPC', '우주소녀');
INSERT INTO cluster VALUES('MMU', '마마무');
SELECT * FROM cluster;

ALTER TABLE cluster
    ADD CONSTRAINT
    PRIMARY KEY (mem_id);
SELECT * FROM cluster;


-- 보조 인덱스 구성하기
CREATE TABLE second( -- 보조 인덱스를 테스트하기 위한 테이블
    mem_id      CHAR(8),
    mem_name    VARCHAR(10)
);

INSERT INTO second VALUES('TWC', '트와이스');
INSERT INTO second VALUES('BLK', '블랙핑크');
INSERT INTO second VALUES('WMN', '여자친구');
INSERT INTO second VALUES('OMY', '오마이걸');
INSERT INTO second VALUES('GRL', '소녀시대');
INSERT INTO second VALUES('ITZ', '잇지');
INSERT INTO second VALUES('RED', '레드벨벳');
INSERT INTO second VALUES('APN', '에이핑크');
INSERT INTO second VALUES('SPC', '우주소녀');
INSERT INTO second VALUES('MMU', '마마무');

ALTER TABLE second
    ADD CONSTRAINT
    UNIQUE (mem_id);
SELECT * FROM second;

-- 두 인덱스 모두 검색이 빠르기는 하지만, 클러스터형 인덱스가 조금 더 빠르다

SHOW TABLE STATUS LIKE 'member';
CREATE INDEX idx_member_addr
    ON member (addr);
SHOW INDEX FROM member;
ANALYZE TABLE member; -- 인덱스 검색 전에 분석해줘야 함
SHOW TABLE STATUS LIKE 'member';
CREATE UNIQUE INDEX idx_member_mem_number
    ON member (mem_number); -- 중복된 값이 있어서 오류

CREATE UNIQUE INDEX idx_member_mem_name
    ON member (mem_name);
SHOW INDEX FROM member;
INSERT INTO member VALUES('MOO', '마마무', 2, '태국', '001', '12341234', 155, '2020.10.10'); -- UNIQUE 오류
ANALYZE TABLE member;
SHOW INDEX FROM member;
SELECT * FROM member; -- 인덱스 사용x
SELECT mem_id, mem_name, addr FROM member; -- 인덱스 사용x
SELECT mem_id, mem_name, addr -- 인덱스 사용o
	FROM member
    WHERE mem_name = '에이핑크';
CREATE INDEX idx_member_mem_number
	ON member (mem_number);
ANALYZE TABLE member;
SELECT mem_name, mem_number -- 인덱스 사용o
	FROM member
    WHERE mem_number >= 7;
SELECT mem_name, mem_number -- WHERE문에서 '열'에 연산이 있을 때, 인덱스 사용x
    FROM member
    WHERE mem_number * 2 >= 14;
SELECT  mem_name, mem_number -- 이렇게 수정하면, 인덱스 사용o
    FROM member
    WHERE mem_number >= 14 / 2;

SHOW INDEX FROM member;
-- 인덱스 제거(보조 인덱스를 먼저 제거해줘야 좋음)
DROP INDEX idx_member_mem_name ON member;
DROP INDEX idx_member_addr ON member;
DROP INDEX idx_member_mem_number ON member;

ALTER TABLE member
    DROP PRIMARY KEY; -- 오류! 외래키가 있어서 클러스터형 인덱스 제거가 안됨

-- 외래 키를 조회
SELECT table_name, constraint_name
    FROM information_schema.referential_constraints
    WHERE constraint_schema = 'market_db';

ALTER TABLE buy
    DROP FOREIGN KEY buy_ibfk_1;
ALTER TABLE member
    DROP PRIMARY KEY;

-- 보조 인덱스 제거 -> 클러스터형 인덱스 제거
--                  (외래 키 제거 -> 기본 키 제거)

---- 인덱스를 효과적으로 사용하는 방법
-- WHERE절에서 사용되는 열, 그것도 자주 사용되는 열에 INDEX를 만들어야 가치가 있다
-- 데이터의 중복이 높은 열은 인덱스를 만들어도 효과가 별로 없다
-- 사용하지 않는 인덱스는 제거하라