-- 주의사항 :  리눅스 MySQL은 필드명이나 테이븡명의 대소문자를 따진다.

-- 그룹함수, avg, max, min, count, sum ....
-- COUNT(), MAX(), MIN(), SUM(), AVG()

USE mydb;

-- 에러 예시 
SELECT ename, sal, avg(sal) FROM emp LIMIT 10;
-- 이 코드는 에러가 납니다. 
-- 이유는 avg 내장함수는 ename, sal 보다 갯수가 적기 때문에 같이 나올 수가 없다.


-- 이럴 때 서브쿼리를 쓸 수 있습니다.
SELECT ename, sal,
(SELECT avg(sal) FROM emp) as avg_sal
FROM emp;

-- 부분합, 그룹별로 묶는게 가능하다.
-- 각 부서별로 급여 평균 을 확인하고 싶다.
-- 그룹함수는 group by 절에 온 필드는 사용가
SELECT deptno, avg(sal)
FROM emp
GROUP BY deptno;


-- 이름과 부서번호 급여 부서별 평균을 확인하고 싶다.
SELECT 
			ename, 
			deptno, 
			(SELECT avg(sal) FROM emp B WHERE A.deptno = B.deptno) AS dept_sal
FROM emp A;


-- 서브쿼리와 join 합치
SELECT ename, A.deptno
FROM emp A
LEFT OUTER JOIN
			(SELECT deptno, avg(sal) dept_sal, sum(sal) sum_sal, max(sal) max_sal, min(sal) min_sal
				FROM emp 
				GROUP BY deptno) B
ON A.deptno = B.deptno



-- orders 테이블에서 고객별 주문 개수를 구하고, 정렬 주문수가 많은 고객부터 내림차순
-- 고객이름, 주문카운트

USE w3schools;

SELECT * FROM Orders LIMIT 10;
SELECT * FROM EMPLOYEES LIMIT 10;
SELECT * FROM customers LIMIT 10;
SELECT * FROM OrderDetails LIMIT 10;


-- 같이 풀어보기 
SELECT customerId, count(customerId)
FROM orders
GROUP BY customerId
ORDER BY count(customerId) DESC;
-- where 절에는 group 함수 사용 못함.


-- 구매개수가 5개 이상만  
SELECT customerId, count(customerId)
FROM orders
GROUP BY customerId
-- WHERE count(customerId) >= 5      -- [중요]  where 절에는 group 함수 사용 못함.
HAVING count(customerId) >= 5          -- 순서도 중요합니다.  GROUP BY  =>  HAVING
ORDER BY count(customerId) DESC;






-- =======================================
-- =======================================
-- =======================================
-- =======================================
-- =======================================
-- GROUP BY 
USE mydb;

-- 전체 평균만 구할 경우엔 GROUP BY 필요 없음..
SELECT AVG(sal) AS avg_sal FROM emp;

-- 모든 사원의 평균 급여 하나만 보여줍니다.
SELECT AVG(sal) FROM emp;
-- 이건 전체를 하나의 그룹으로 본 것입니다.

-- 그런데 이렇게 값의 갯수 자체가 상이한 deptno(n개) 존재와 average(1개)는 GROUP이 반드시 필요.
-- 여기서 GROUP BY deptno는 사원들을 deptno 기준으로 그룹으로 나누고, AVG(sal)은 각 그룹 내의 평균 급여를 구하는 것입니다.
SELECT deptno, AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno;     -- 즉, 이 것을 기준으로 평균을 구하겠다~~

SELECT deptno, AVG(sal) AS avg_sal
FROM emp
GROUP BY deptno
HAVING AVG(sal) >= 2000;     -- OPTION :  HAVING - GROUP BY로 집계한 결과에 조건을 거는 것입니다.

SELECT deptno, COUNT(*) AS num_employees
FROM emp
GROUP BY deptno;


-- 이 경우는 2개의 조건이 똑같이 같은 다른 컬럼의 것과 묶어서 average를 낸다.
--      job	      deptno	    sal
-- CLERK	        10	       1000
-- CLERK	        10  	     1100     -- 이렇게 job과  deptno이 함께 같아야합니다.

SELECT job, deptno, AVG(sal) AS avg_salary
FROM emp
GROUP BY job, deptno;



-- -------------------------------------------
USE w3schools;

SELECT * FROM categories LIMIT 20;
SELECT * FROM products LIMIT 20;

SELECT CategoryId FROM products
GROUP BY categoryId;

-- 구매개수가 5개 이상만  
SELECT customerId, count(customerId)
FROM orders
GROUP BY customerId
-- WHERE count(customerId) >= 5      -- [중요]  where 절에는 group 함수 사용 못함.
HAVING count(customerId) >= 5          -- 순서도 중요합니다.  GROUP BY  =>  HAVING
ORDER BY count(customerId) DESC;


-- 기발한 예제
SELECT 
				PRODUCTID,
				sum(Quantity) AS QuantitySum
FROM OrderDetails
GROUP BY PRODUCTID 
ORDER BY QUANTITYSUM;   -- 재고를 알 수 있을 것 같습니다.






