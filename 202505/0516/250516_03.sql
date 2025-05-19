use mydb;

desc emp;

-- empno 필드가 primary key로 되어있다.
insert into emp (empno, ename) values (8000, '홍길동');
insert into emp (empno, enaee) values (8000, '임꺽정');
-- 8000번이 이미 있어서 에러발생
-- Error Code: 1062. Duplicate entry '8000' for key 'emp.PRIMARY'

-- 테이블을 만들 때 