USE mydb;

SELECT * FROM EMP;
SELECT * FROM EMP WHERE empno=8005;

DELETE FROM emp WHERE empno=8005;

SELECT * FROM emp;
-- 위 쿼리를 순서대로 실행하면 empno = 8005인 데이터를 삭제하고, 복구는 불가능합니다.
-- 이유는 트랜잭션을 사용하지 않았기 때문입니다.


-- ====================================
-- Transaction 예시 

START transaction  -- 여기서부터 트랜잭션 시작 

DELETE FROM emp;

SELECT * FROM emp;

ROLLBACK;   -- 원상복구 

SELECT * FROM emp;  -- 원상복구 확인 완료 

/*
< 트랜잭션 완벽 이해 예시 >

1. A 계좌에서 1000원 출금
2. B 계좌에 1000원 입금

- 이 두 작업을 하나의 트랜잭션으로 묶어야 함
- 출금만 되고 입금이 실패하면? → 데이터 오류 발생
- 따라서 둘 다 성공하거나 둘 다 실패(롤백) 해야 함
*/


-- ====================================
-- Transaction 예시

UPDATE emp SET ename = '조승연'
WHERE empno = 8004;
COMMIT;  -- Transaction이라고 하더라도, commit을 해버리면 현재까지의 변경 사항을 영구 저장합니다.
SELECT * FROM emp;





-- ====================================
-- ====================================
-- ====================================
-- ====================================
-- 문제 1
CREATE TABLE tb_score(
					id bigint PRIMARY KEY AUTO_INCREMENT,
					sname varchar(20) NOT NULL,
					kor int NOT NULL,
					eng int NOT NULL,
					mat Int NOT NULL,
					regdate datetime
);


DROP TABLE tb_score;


INSERT INTO tb_score(sname, kor,  eng, mat, regdate)
values('홍길동', 90,90,90, now());


SELECT 
					sname, kor, eng, mat, (kor+eng+mat) AS total, 
					date_format(regdate, '%Y-%m-%d %H:%i') regdate
FROM tb_score;


-- ================
-- <문제 풀기>
-- 전체보기
-- 추가 : 입력 받아서
-- 수정
-- update 테이블명 set 필드1='값1', 필드2='값2' where절 
-- 삭제 
-- delete from 테이블명 where id = 1
-- 검색 



SELECT * FROM tb_score;


-- ===============================================
-- 문제 2
DROP TABLE tb_weekly_pay;

CREATE TABLE tb_weekly_pay(
					id bigint PRIMARY KEY AUTO_INCREMENT,
					wname varchar(20) NOT NULL,
					work_time int NOT NULL,
					per_pay int NOT NULL,
					overtime_pay Int NOT NULL,
					weekly_pay Int NOT NULL,
					regdate datetime
);


INSERT INTO tb_weekly_pay(wname, work_time,  per_pay, overtime_pay, weekly_pay, regdate)
values('홍길동', 10, 10000, 0, 100000, now());


SELECT 
					id, wname, work_time,  per_pay, overtime_pay, weekly_pay, 
					date_format(regdate, '%Y-%m-%d %H:%i') regdate
FROM tb_weekly_pay;
