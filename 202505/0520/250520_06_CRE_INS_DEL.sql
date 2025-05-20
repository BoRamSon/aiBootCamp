-- INSERT & DELETE

USE mydb;

DESC dept;

SELECT * FROM dept;

-- 테이블 구조가 간당할 경우에는 필드명을 생략할 수 있다.
-- desc에 나온 필드 목록하고 동일한 구조로 저장해야 한다.
INSERT INTO dept VALUES(50, '개발 1부', '서울');
SELECT * FROM dept; -- 확인  

-- 필드명을 이렇게 정해줄 수 있음.  
INSERT INTO dept(deptno, dname) values(60, '개발 2부');
SELECT * FROM dept;  -- 확인  
-- 안 넣은 값은 null이 된다.

DESC emp;

INSERT INTO emp(empno) values(9000);
SELECT * FROM emp; -- 확인

--  규칙에 위배되는 데이터를 삭제하자.
DELETE FROM emp WHERE sal IS NULL;
-- 이거는 내가 테스트로 만들어놓은 것들만 삭제하게 됩니다. 
SELECT * FROM emp; -- 확인
-- delete 명령어 안전장치가 되어 있는 DBMS가 있다.  -  오라클!


-- !!!!!!! 'emp 테이블 수정'을 하고옴 !!!!!!
-- sal 필드와 ename 필드를 not null로 하기로  설정 및 저장 완
INSERT INTO emp(empno) values(9000);  -- error
-- error : SQL Error [1364] [HY000]: Field 'ename' doesn't have a default value

INSERT INTO emp(empno, ename, sal) 
VALUES(8000, '홍길동', 3300);  -- 설정했던 값들을 무조건 넣어주니 잘 들어간다.
SELECT * FROM emp; -- 확인

-- 한번에 여러명 넣기
INSERT INTO emp(empno, ename, sal) 
VALUES(8001, '둘리', 3200),
								(8002, '도우치', 3200),
								(8003, '또치', 3200);
SELECT * FROM emp; -- 확인


-- ==============================================
-- 데이터에 ' 가 들어가야 할 때  ==> ''
-- 'Tom's family'   ==>   'Tom''s family'    2개를 넣어준다.
-- 'Jane'   ===>    '''Jane'''                           3개를 양쪽으로 넣어준다???
INSERT INTO emp(empno, ename, sal) 
VALUES(8004, 'Tom''s fam', 3200),
								(8005, '''Jane''', 3200);
SELECT * FROM emp; -- 확인


-- 서버 : 서비스를 제공하는 측 (하드웨어 또는 소프트웨어)
-- 클라이언트 : 서비스를 제공받는 측(하드웨어 또는 소프트웨어) 
-- MS > (서버)  /  리눅스 > (Deamon) : 화면 UI 제공안하고 조용히 작동

