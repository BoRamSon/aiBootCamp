
/*
- 상관쿼리 : 외부 쿼리의 값을내부 쿼리에서 참조하는 서브쿼리를 말한다.
- 외부 쿼리의 각 행마다 내부 쿼리가 실행되는 구조

- exists, any, all, in 등이 있다.

  - exists : 서브쿼리의  실행결과가 하나라고 있으면 True  / 1개라도 없으면 False 반환
    - 서브쿼리의 싱행 결과가 한건이라도 있으면 실행된다.  

  - Any
    - 조건을 만족하는게 하나라도 있으면 수행 
    - 부등호 or 부등호 or 부등호 or 부등호 or 부등호

  - all
    - 모든 조건을 만족하는 부등호 and 부등호 and 부등호 and 부등호 and

  - in 
    - 등호 or 등호 or 등호 or
*/




-- 부서별 평균 급여보다 높은 사원조회
-- 부서별 평균값이 필요
USE mydb;

SELECT avg(sal) FROM emp WHERE deptno = 10;
SELECT avg(sal) FROM emp WHERE deptno = 20;
SELECT avg(sal) FROM emp WHERE deptno = 30;
SELECT avg(sal) FROM emp WHERE deptno = 40;

SELECT empno, sal, deptno FROM emp;

SELECT empno, sal, deptno FROM emp
WHERE sal > (SELECT avg(sal)FROM emp WHERE deptno=10);

-- 이것을 상관쿼리라고 부릅니다. 
-- 외부의 A의 SubQuey(내부쿼리 )의 deptno가 서로 관계가 있었다.
SELECT empno, sal, deptno FROM emp A
WHERE sal > (SELECT avg(sal)FROM emp B WHERE B.deptno=A.deptno);




-- exists : 매니저가 존재하는 사원만 조회하려고 한다.

SELECT empno, ename, mgr FROM emp;

SELECT ename FROM emp WHERE mgr=7788;

-- 서브쿼리의 실행결과가 하나라도 있으면 외부쿼리를 실행한다.
-- SELECT	* FROM emp WHERE EXISTS (서브쿼리)  -- 서브쿼리의 결과 유무만 따집니다.

SELECT empno, ename, mgr FROM emp
WHERE EXISTS (
				SELECT ename FROM emp WHERE mgr=7788
);


-- 상관 쿼리 
SELECT empno, ename, mgr FROM emp A
WHERE EXISTS (
				SELECT 1 FROM emp B WHERE A.mgr = B.empno
);

