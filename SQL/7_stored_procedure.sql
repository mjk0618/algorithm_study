-- 스토어드 프로시저(stored procedure):
-- SQL에 프로그래밍 기능을 추가해서 일반 프로그래밍 언어와 비슷한 효과를 냄

USE market_db;
DROP PROCEDURE IF EXISTS user_proc;
DELIMITER $
CREATE PROCEDURE user_proc()
BEGIN
    SELECT * FROM member;
END $
DELIMITER ;
CALL user_proc();
DROP PROCEDURE user_proc;

-- 입력 매개변수 활용
DROP PROCEDURE IF EXISTS user_proc1;
DELIMITER $
CREATE PROCEDURE user_proc1(IN userName VARCHAR(10))
BEGIN
    SELECT * FROM member WHERE mem_name = userName;
END $
DELIMITER ;
CALL user_proc1('에이핑크');

DROP PROCEDURE IF EXISTS user_proc2;
DELIMITER $
CREATE PROCEDURE user_proc2(
    IN userNumber INT,
    IN userHeight INT
)
BEGIN
    SELECT * FROM member
    WHERE mem_number > userNumber AND height > userHeight;
END $
DELIMITER ;
CALL user_proc2(6, 165);

-- 출력 매개변수 활용
DROP PROCEDURE IF EXISTS user_proc3;
DELIMITER $
CREATE PROCEDURE user_proc3(
    IN txtValue CHAR(10),
    OUT outValue INT
)
BEGIN 
    INSERT INTO noTable VALUES(NULL, txtValue);
    SELECT max(id) INTO outValue FROM noTable;
END $
DELIMITER ;

DESC noTable; -- 존재하지 않는 테이블, 하지만 이를 이용한 스토어드 프로시저는 문제없이 만들어졌다
-- CALL을 할때는 테이블이 있어야한다

CREATE TABLE IF NOT EXISTS noTable(
    id INT AUTO_INCREMENT PRIMARY KEY,
    txt CHAR(10)
);

CALL user_proc3('테스트1', @myValue);
SELECT * FROM noTable;
SELECT CONCAT('입력된 ID 값 ==>', @myValue);

-- SQL 프로그래밍의 활용
DROP PROCEDURE IF EXISTS ifelse_proc;
DELIMITER $
CREATE PROCEDURE ifelse_proc(
    IN memName VARCHAR(10)
)
BEGIN
    DECLARE debutYear INT;
    SELECT YEAR(debut_date) into debutYear FROM member
        WHERE mem_name = memName;
    IF (debutYear >= 2015) THEN
        SELECT '신인 가수네요. 화이팅 하세요.' AS '메시지';
    ELSE
        SELECT '고참 가수네요. 그동안 수고하셨어요' AS '메시지';
    END IF;
END $
DELIMITER ;
CALL ifelse_proc('오마이걸');

DROP PROCEDURE IF EXISTS while_proc;
DELIMITER $
CREATE PROCEDURE while_proc()
BEGIN
    DECLARE hap INT;
    DECLARE num INT;
    SET hap = 0;
    SET num = 1;

    WHILE (num <= 100) DO
        SET hap = hap + num;
        SET num = num + 1;
    END WHILE;
    SELECT hap as '1~100 합계';
END $
DELIMITER ;
CALL while_proc();

-- 동적 SQL 활용
DROP PROCEDURE IF EXISTS dynamic_proc;
DELIMITER $
CREATE PROCEDURE dynamic_proc(
    IN tableName VARCHAR(20)
)
BEGIN
    SET @sqlQuery = CONCAT('SELECT * FROM ', tableName);
    PREPARE myQuery FROM @sqlQuery;
    EXECUTE myQuery;
    DEALLOCATE PREPARE myQuery;
END $
DELIMITER ;
CALL dynamic_proc('member');

-- 스토어드 함수(stored function): 직접 만들어서 사용하는 함수
-- RETURNS문으로 반환값의 데이터 형식 지정
-- RETURN 문으로 하나의 값 반환
-- 입력 매개변수를 사용하고 IN은 붙이지 않음 (스토어드 프로시저와 차이점)
-- CALL이 아닌 SELECT로 호출, 내부에서는 SELECT문 사용 불가 (스토어드 프로시저와 차이점)

SET GLOBAL log_bin_trust_function_creators = 1;
-- 스토어드 함수 생성 권한 허용

DROP FUNCTION IF EXISTS sumFunc;
DELIMITER $
CREATE FUNCTION sumFunc(number1 INT, number2 INT)
    RETURNS INT
BEGIN
    RETURN number1 + number2;
END $
DELIMITER ;
SELECT sumFunc(100, 200) AS '합계';

DROP FUNCTION IF EXISTS calcYearFunc;
DELIMITER $
CREATE FUNCTION calcYearFunc(dYear INT)
    RETURNS INT
BEGIN
    DECLARE runYear INT;
    SET runYear = YEAR(CURDATE()) - dYear;
    RETURN runYear;
END $
DELIMITER ;
SELECT calcYearFunc(2010) AS '활동 햇수';
SELECT calcYearFunc(2007) INTO @debut2007;
SELECT calcYearFunc(2013) INTO @debut2013;
SELECT @debut2007-@debut2013 AS '2007과 2013 차이';

SELECT mem_id, mem_name, calcYearFunc(YEAR(debut_date)) AS '활동 햇수' FROM member;

SHOW CREATE FUNCTION calcYearFunc; -- 기존에 작성된 함수 확인
DROP FUNCTION calcYearFunc;

-- 커서(cursor): 테이블에서 한 행씩 처리하기 위한 방식
USE market_db;
DROP PROCEDURE IF EXISTS cursor_proc;
DELIMITER $
CREATE PROCEDURE cursor_proc()
BEGIN
    DECLARE memNumber INT;
    DECLARE cnt INT DEFAULT 0;
    DECLARE totNumber INT DEFAULT 0;
    DECLARE endOfRow BOOLEAN DEFAULT FALSE;

    DECLARE memberCursor CURSOR FOR
        SELECT mem_number FROM member;

    DECLARE CONTINUE HANDLER
        FOR NOT FOUND SET endOfRow = TRUE;
    
    OPEN memberCursor;

    cursor_loop: LOOP
        FETCH memberCursor INTO memNumber;

        IF endOfRow THEN
            LEAVE cursor_loop;
        END IF;

        SET cnt = cnt + 1;
        SET totNumber = totNumber + memNumber;
    END LOOP cursor_loop;

    SELECT (totNumber / cnt) AS '회원의 평균 인원 수';

    CLOSE memberCursor;
END $

CALL cursor_proc();

-- 트리거(trigger): 자동으로 수행하여 사용자가 추가 작업을 잊어버리는 실수 방지
-- DML(Data Manipulation Language)문(INSERT, UPDATE, DELETE)의 이벤트가 발생할 때 작동

USE market_db;
CREATE TABLE IF NOT EXISTS trigger_table(id INT, txt VARCHAR(10));
INSERT INTO trigger_table VALUES(1, '레드벨벳');
INSERT INTO trigger_table VALUES(2, '잇지');
INSERT INTO trigger_table VALUES(3, '블랙핑크');
DROP TRIGGER IF EXISTS myTrigger;
DELIMITER $
CREATE TRIGGER myTrigger
    AFTER DELETE
    ON trigger_table
    FOR EACH ROW
BEGIN
    SET @msg = '가수 그룹이 삭제됨';
END $
DELIMITER ;
SET @msg = '';
INSERT INTO trigger_table VALUES(4, '마마무');
SELECT @msg;
UPDATE trigger_table SET txt ='블핑' WHERE id = 3;
SELECT @msg;
DELETE FROM trigger_table WHERE id = 4;
SELECT @msg;

-- 트리거 활용
CREATE TABLE singer (SELECT mem_id, mem_name, mem_number, addr FROM member);
CREATE TABLE backup_singer(
    mem_id          CHAR(8) NOT NULL,
    mem_name        VARCHAR(10) NOT NULL,
    mem_number      INT NOT NULL,
    addr            CHAR(2) NOT NULL,
    modType         CHAR(2),
    modDate         DATE,
    modUser         VARCHAR(30)
);

DROP TRIGGER IF EXISTS singer_updateTrg;
DELIMITER $
CREATE TRIGGER singer_updateTrg
    AFTER UPDATE
    ON singer
    FOR EACH ROW
BEGIN
    INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr, 
                                    '수정', CURDATE(), CURRENT_USER());
END $
DELIMITER ;

DROP TRIGGER IF EXISTS singer_deleteTrg;
DELIMITER $
CREATE TRIGGER singer_deleteTrg
    AFTER DELETE
    ON singer
    FOR EACH ROW
BEGIN
    INSERT INTO backup_singer VALUES(OLD.mem_id, OLD.mem_name, OLD.mem_number, OLD.addr,
                                    '삭제', CURDATE(), CURRENT_USER());
END $
DELIMITER ;
UPDATE singer SET addr = '영국' WHERE mem_id = 'BLK';
DELETE FROM singer WHERE mem_number >= 7;
SELECT * FROM backup_singer;
TRUNCATE TABLE singer;
SELECT * FROM backup_singer; -- DELETE 문에만 작동하므로 TRUNCATE에는 트리거 작동x

