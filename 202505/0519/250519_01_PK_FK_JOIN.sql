
-- =====================================================
-- < primary key >
-- emp 테이블의 정보를 확인하고 primary key가 존재하면 삭제하려고 한다.
USE mydb;

SELECT * FROM emp LIMIT 10;
DESC emp;  -- empno 가 PRIMARY임

INSERT INTO emp(empno, ename) VALUES (8011, '장길산');

ALTER TABLE emp DROP PRIMARY KEY;

DESC emp;  -- empno 가 PRIMARY임
INSERT INTO emp(empno, ename) VALUES (8011, '장길산');

SELECT * FROM emp;
 
-- primary key 지정은 불가능하다. 이유: empno 필드갑이 이미 중복 존
ALTER TABLE emp ADD CONSTRAINT pk_emp primary KEY (empno)
-- emp 테이블의 기본 키로 설정된 컬럼(예: empno)에 이미 8011이라는 값이 존재하는데,
-- 다시 동일한 값을 넣으려 해서 발생했습니다.

DELETE FROM emp WHERE empno = 8011 AND ename = '장길산';

SELECT * FROM emp;

ALTER TABLE emp ADD CONSTRAINT pk_emp PRIMARY key(empno);

-- 갑자기 설정을 변경???  edit - preference - sql editor - 하단에 safe updates 체크 해제하고 재시작
DELETE FROM emp WHERE empno = 8011 AND ename = '장길산';

SELECT * FROM emp;

ALTER TABLE emp ADD CONSTRAINT pk_emp PRIMARY KEY(empno);


-- ==========================
-- < foreign key (외부키) >
DESC dept;
ALTER TABLE 테이블명
ADD CONSTRAINT 외부키 이름
FOREIGN KEY (필드명)
REFERENCES 참조테이블명(참조필드명)
ON DELETE CASCADE  -- 부모 레코드 삭제 시 자식도 삭제
ON UPDATE CASCADE  -- 부모키값 변경 시 자식도 자동으로 변경

SELECT * FROM dept;

-- 1. 참조하는 테이블(dep)의 dept가 반드시 primary거나 unique조건을 만족해야 한다.
-- 2. 데이터 타입이 동일 해야한다.

ALTER TABLE emp ADD constraint fk_emp_dept
FOREIGN KEY (deptno) 
references dept(deptno);
-- 테이블 상호간에 제약조건이 방생한다.
-- SHOW CREATE TABLE emp\G;

SELECT * FROM dept;
DELETE FROM dept WHERE deptno = 10;  -- 오류가 맞음 / 외부키 때문에 삭제 불가



-- 홍길동한테 부서번호 부여하기 
SELECT * FROM emp;
UPDATE emp SET deptno =50 WHERE empno=8000;  -- 오류 나는 것이 맞음 


-- ==================================
-- join
-- JOIN은 두 개 이상의 테이블을 공통된 컬럼을 기준으로 연결하여 조회할 때 사용합니다.
-- inner / outer / full - ansi 표준
-- emp 테이블에는 부서번호만 있다.
-- dept 테이블에는 부번호와 부서명을 알고 싶다.
-- 두개 이상의 테이블을 묶어서 새로운 정보를 창출한다.

-- ---------------------------------
-- < inner join > : 두 테이블에서 서로 공통된 조건에 맞는 행(row)만 결합해서 보여주는 JOIN
-- 이거는 query 표준이 아니기 때문에 다른 DBMS에서는 에러가 날 수 있다. (oracle, mysql만 가)
SELECT A.empno, A.ename, A.demtno, B.dname
FROM emp A, dept B
WHERE A.deptno = B.deptno;   -- JOIN 조건이 동등조건  (equl 조건)


-- 표준 join 
SELECT A.empno, A.ename, A.demtno, B.dname
FROM emp A
INNER JOIN dept B ON A.deptno = B.deptno

SELECT * FROM emp;


-- 회원번호가 7566, 7788, 7902, 7934, 8000 
SELECT A.empno, A.ename, A.deptno, B.dname
FROM emp A, dept B
WHERE  A.deptno = B.deptno AND
A.empno IN (7566, 7788, 7902, 7934, 8000);
-- 단점 : 조인 조건과 검색조건이 구분이 안간다. 그래서 조인이 여러번 이뤄질 경우에 보기 안좋다.


-- inner join 은 양쪽 테이블에 값이 존재할 때 된다.
SELECT A.empno, A.ename, A.deptno, B.dname
FROM emp A
INNER JOIN dept B ON A.deptno = B.deptno
WHERE A.empno IN (7566, 7788, 7902, 7934, 8000);


-- ---------------------------------
-- < outer join > : left, right
-- from 절에 가까운 테이블 left (left 테이블의 데이터 다출력 )
-- form 절로부터 먼 테이블이 right  (right 테이블의 데이터 다 출력 )
SELECT A.empno, A.ename, A.deptno, B.dname
FROM emp A
LEFT OUTER JOIN dept B ON A.deptno = B.deptno;
-- GPT : 둘 다 한쪽 테이블의 모든 데이터는 무조건 출력하고, 다른 쪽 테이블의 데이터는 조건에 맞는 것만 출력


-- ---------------------------------
-- 중복성 배제  
-- right outer join
SELECT DISTINCT deptno FROM emp;

SELECT A.empno, A.ename, A.deptno, B.dname
FROM emp A
right OUTER JOIN dept B ON A.deptno = B.deptno;
-- 40번이 할당을 못 받은 것으로 나옵니다.



