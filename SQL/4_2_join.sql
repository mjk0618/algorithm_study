-- Active: 1661781168443@@127.0.0.1@3306@market_db
-- 일대 다 관계는 기본키(PK)와 외래키(FK) 관계 (PK-FK 관계)
USE market_db;
SELECT * 
    FROM buy
        INNER JOIN member
        ON buy.mem_id = member.mem_id;
        --WHERE buy.mem_id = 'GRL';

SELECT buy.mem_id, mem_name, prod_name, addr, CONCAT(phone1, phone2) '연락처'
    FROM buy
        INNER JOIN member
        ON buy.mem_id = member.mem_id;

-- 테이블을 명확하게 표시
SELECT buy.mem_id, member.mem_name, buy.prod_name, member.addr, CONCAT(member.phone1, member.phone2) '연락처'
    FROM buy
        INNER JOIN member
        ON buy.mem_id = member.mem_id;

-- 테이블 별칭 지정
SELECT B.mem_id, M.mem_name, B.prod_name, M.addr, CONCAT(M.phone1, M.phone2) '연락처'
    FROM buy B
        INNER JOIN member M
        ON B.mem_id = M.mem_id;

-- 내부 조인: 두 테이블에 모두 있는 내용만 조인되는 방식
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
    FROM buy B
        INNER JOIN member M
        ON B.mem_id = M.mem_id
    ORDER BY M.mem_id;

-- 중복된 결과 1개만 출력
SELECT DISTINCT M.mem_id, M.mem_name, M.addr
    FROM buy B
        INNER JOIN member M
        ON B.mem_id = M.mem_id
    ORDER BY M.mem_id;

-- 외부 조인: 양쪽 중에 한 곳이라도 내용이 있을 때 조인
SELECT M.mem_id, M.mem_name, B.prod_name, M.addr
    FROM member M
        LEFT OUTER JOIN buy B
        ON M.mem_id = B.mem_id
    ORDER BY M.mem_id;

SELECT DISTINCT M.mem_id, B.prod_name, M.mem_name, M.addr
    FROM member M
        LEFT OUTER JOIN buy B
        ON M.mem_id = B.mem_id
    WHERE B.prod_name IS NULL
    ORDER BY M.mem_id;

-- 상호 조인(cross join): 한쪽 테이블의 모든 행과 다른쪽 테이블의 모든 행을 조인되는
-- 결과는 의미가 없고, 테스트를 위한 대용량의 테이블을 생성할 때 사용
SELECT *
    FROM buy
    CROSS JOIN member;

SELECT COUNT(*) "데이터 개수"
    FROM sakila.inventory
        CROSS JOIN world.city;

CREATE TABLE cross_table
    SELECT *
        FROM sakila.actor
            CROSS JOIN world.country;

SELECT * FROM cross_table LIMIT 10;

-- 자체 조인(self join): 1개의 테이블이 자체로 조인
USE market_db;
CREATE TABLE emp_table (emp CHAR(4), manager CHAR(4), phone VARCHAR(8));

INSERT INTO emp_table VALUES('대표', NULL, '0000');
INSERT INTO emp_table VALUES('영업이사', '대표', '1111');
INSERT INTO emp_table VALUES('관리이사', '대표', '2222');
INSERT INTO emp_table VALUES('정보이사', '대표', '3333');
INSERT INTO emp_table VALUES('영업과장', '영업이사', '1111-1');
INSERT INTO emp_table VALUES('경리부장', '관리이사', '2222-1');
INSERT INTO emp_table VALUES('인사부장', '관리이사', '2222-2');
INSERT INTO emp_table VALUES('개발팀장', '정보이사', '3333-1');
INSERT INTO emp_table VALUES('개발주임', '정보이사', '3333-1-1');

SELECT A.emp '직원', A.phone '본인연락처', B.emp '직속상관', B.phone '직속상관연락처'
    FROM emp_table A
        INNER JOIN emp_table B
        ON A.manager = B.emp
    WHERE A.emp = '경리부장';