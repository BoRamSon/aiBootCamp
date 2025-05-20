
/*

- join 속도를 빠르게 하려면, join 필드에 인덱스를 만들어줘야 한다.

- subQuery : 서브쿼리는 주 쿼리 옆에서 주워리보다 먼저 실행되서 결과를 가져온 다음에 주쿼리가 실행된다.

- 서브쿼리는 select 절, from 절, where, order, by 절 등 ek rksdmgkek.
  - select 절
    - 스칼라 서브 쿼리, 결과값이 null이거나 한개만 가져오는 쿼리
    - join을 대체할 수 있다. 우리가 볼 떄 편해보임, 조인이 일반적으로 더 빠르다.
    - 가급적 join으로 해결하고, join 안될 경우 서브쿼라를 사용하자!

*/




-- =============================================
-- 스칼라 서브쿼리 - select 

USE mydb;

-- 사원 번호, 사원 이름, 부서명을 가져오려고 한다.
SELECT empno, ename, deptno
FROM emp;

SELECT dname, deptno FROM dept WHERE deptno = 10;

SELECT * FROM address LIMIT 20;
SELECT * FROM city LIMIT 20;

-- SELECT empno, ename, deptno,
-- (SELECT dname, deptno FROM dept WHERE deptno = 10) AS dname
-- FROM emp;


SELECT empno, ename, deptno,
(SELECT dname FROM dept B WHERE A.deptno = B.deptno) AS dname
FROM emp A;

-- --------------------------------

USE sakila;

SELECT * FROM actor LIMIT 20;
SELECT * FROM film_actor LIMIT 20;
SELECT * FROM film LIMIT 20;

SELECT A.first_name, A.last_name, B.film_id
FROM actor A
LEFT OUTER JOIN film_actor B ON A.actor_id = B.actor_id;

-- join + 서브쿼리 select절 사용하기   (굳이 이렇게 사용하지 않습니다.)
SELECT A.first_name, A.last_name, B.film_id,
(SELECT title FROM film C WHERE B.film_id = C.film_id) AS title
,(SELECT length FROM film C WHERE B.film_id = C.film_id) AS length
FROM actor A
LEFT OUTER JOIN film_actor B ON A.actor_id = B.actor_id;




-- =============================================
-- from 절 : 다중행을 반환한다. 다중행 서브쿼리, 인라인뷰 

USE mydb;

SELECT * FROM dept LIMIT 10;  -- dname
SELECT * FROM emp LIMIT 10;  -- ename

SELECT * FROM emp WHERE deptno IN (10, 20);  -- 여기에서 사원이름, 부서명만 나오게 하고싶다. 

SELECT A.ename, dname
FROM (
							SELECT * FROM emp WHERE deptno IN (10, 20)
) AS A
JOIN dept B ON A.deptno = B.deptno			




-- =============================================
-- inline view

USE sakila;

-- film_id : ambigous
SELECT A.film_id, title, length, actor_id
FROM film A
LEFT OUTER JOIN film_actor B ON A.film_id = B.film_id;

-- ! 인라인 뷰 !!!!!
SELECT first_name, last_name, title
FROM actor A
LEFT OUTER JOIN (
						SELECT A.film_id, title, length, actor_id
						FROM film A
						LEFT OUTER JOIN film_actor B ON A.film_id = B.film_id
						-- 인라인뷰라고 부른다.
) B ON A.actor_id = B.actor_id




-- =============================================
-- where 절 

USE mydb;

-- emp 테이블에 smith라는 사람의 부서와 같은 부서에 있는 사람들 
SELECT * FROM dept LIMIT 10;  -- dname
SELECT * FROM emp LIMIT 21;  -- ename

SELECT deptno FROM emp WHERE ename ='ALLEN';


SELECT * FROM emp WHERE deptno = 20;

-- 여기 이렇게 했습니다. 
SELECT * FROM emp 
WHERE deptno = (SELECT deptno FROM emp WHERE ename = 'ALLEN');



-- =============================================
-- 같이푸는 문제: 부서 평균 급여보다 급여가 많은 사원 조회

SELECT * FROM emp LIMIT 10;

SELECT * FROM emp 
WHERE sal > (SELECT avg(sal) FROM emp);   -- 그냥 중첩문이라고 이해하면 편하겠습니다.



-- =============================================
-- 같이 푸는 문제: ALLEN 가 근무하는 부서의 급여 평균보다 급여를 받는 사람들 정보를  확인하고자 한다.

SELECT avg(sal) FROM emp WHERE deptno = (SELECT deptno FROM emp WHERE  ename = 'ALLEN');

-- 3중 쿼리 되어버림...
SELECT ename, sal FROM emp
WHERE sal > (SELECT avg(sal) 
														FROM emp WHERE deptno = (SELECT deptno FROM emp WHERE ename = 'ALLEN'));




-- =============================================
-- 문제 1

-- 가장 높은 급여를 받는 사원 정보 조회하기 MAX
SELECT * FROM emp LIMIT 20;


SELECT * FROM emp WHERE sal = MAX(sal);   -- 이것은 왜 잘 못된 것인지 모르겠지만....

SELECT ename, sal FROM emp 
WHERE sal = (SELECT MAX(sal) FROM emp);  


-- 매니저가 존재하는 원만 조회 
-- 나의 mgr 필드가 emp 테이블에 존재하느냐???
SELECT * 
FROM emp 
WHERE mgr IS NOT NULL;

SELECT * 
FROM emp 
WHERE mgr IN (SELECT empno FROM emp);  -- 이거 진짜 생각하기 어려운 것 같습니다....






-- ============================================
-- 기존 JOIN 문제를 서브쿼리로 바꾸는 문제 
-- ============================================
-- 문제 2
-- 고객의 이름과 고객이 대여 한 영화 제목을 모두 출력하자 
-- customer, rental, invetory, film
-- inventory_id, store_id, film_id

USE sakila;

SELECT * FROM customer LIMIT 20;   
SELECT * FROM rental LIMIT 20;     -- 3. 
SELECT * FROM inventory LIMIT 20;
SELECT * FROM film LIMIT 20;

 -- 내가 직접 못 풀었

-- 같이 풀어보기 (concat을 추가하고 테이블 명치까지변경하는 방법을 알게 되었습니다.)
SELECT concat(A.first_name, "  ", A.last_name) name,
	(SELECT title from film D where C.film_id = D.film_id) AS title
FROM customer A
LEFT OUTER JOIN rental B ON A.customer_id = B.customer_id
LEFT OUTER JOIN inventory C ON B.inventory_id = C.inventory_id
left outer join film D on D.film_id=C.film_id
LIMIT 10;




-- ========================================================
-- 문제 3 : NICK WAHLBERG 라는 배우가 출연한 영화의 제목 조회하기

/*
SELECT concat(A.first_name, "  ", A.last_name) name, C.title
FROM actor A
LEFT OUTER JOIN film_actor B ON A.actor_id = B.actor_id
LEFT OUTER JOIN film C ON B.film_id = C.film_id
WHERE A.first_name = 'NICK' AND A.last_name = 'WAHLBERG'
LIMIT 10;
*/

USE sakila

SELECT * FROM actor LIMIT 20;
SELECT * FROM film_actor LIMIT 20;
SELECT * FROM film LIMIT 20;

-- 같이 풀어보기 
SELECT (SELECT title FROM film C WHERE B.film_id = C.film_id) AS title
FROM actor AS 
INNER JOIN film_actor B ON A.actor_id = B.actor_id
WHERE A.first_name='NICK' and A.last_name='WAHLBERG';



-- 
SELECT CONCAT(A.first_name, ' ', A.last_name) AS name, C.title
FROM actor A
JOIN film_actor B ON A.actor_id = B.actor_id
JOIN film C ON B.film_id = C.film_id
WHERE A.actor_id = (
  SELECT actor_id
  FROM actor
  WHERE first_name = 'NICK' AND last_name = 'WAHLBERG'
  LIMIT 1
)
LIMIT 10;






-- ========================================================
-- ========================================================
-- ========================================================
-- ========================================================
-- ========================================================
-- sub query


USE mydb;

-- ------------------------------------
-- SELECT절에서 사용하는 서브쿼리
-- AVG와 컬럼개수가 안 맞는 문제까지 해결할 수 있는 구문인 것 같다. 
SELECT ename, sal, (SELECT AVG(sal) FROM emp) AS avg_sal
FROM emp;

-- ------------------------------------
-- FROM절에서 사용하는 서브쿼리
SELECT deptno, avg_sal
FROM (
    SELECT deptno, AVG(sal) AS avg_sal
    FROM emp
    GROUP BY deptno
) AS dept_avg;

-- ------------------------------------
-- WHERE절에서 사용하는 서브쿼리
SELECT ename, sal
FROM emp
WHERE sal > (SELECT AVG(sal) FROM emp);



-- ================================
USE w3schools;

SELECT * FROM products LIMIT 10;

-- 이해하기 쉬운 예
SELECT * FROM Products
WHERE Price < (SELECT AVG(Price) FROM Products)
ORDER BY Price;


-- 
SELECT
CategoryID, CategoryName, Description
FROM Categories
WHERE
CategoryID =
(SELECT CategoryID FROM Products
WHERE ProductName = 'Chais');  -- Chais CategoryId는 1이니까
-- CategoryId가 1인 것만 가져오겠습니다.

-- 
SELECT
CategoryID, CategoryName, Description 
FROM Categories
WHERE
CategoryID IN
(SELECT CategoryID FROM Products
WHERE Price > 50);









