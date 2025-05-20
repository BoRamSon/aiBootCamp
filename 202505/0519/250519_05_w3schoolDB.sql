USE w3schools;
-- https://www.w3schools.com/ 
-- 도움을 많이 받을 수 있습니다.

SHOW DATABASES;

-- 확인하기 
SELECT * FROM orders LIMIT 10;


-- 주문내역, 고객이름, 판매자 이름 까지만 출력해봐라


SELECT * FROM Orders
LIMIT 10;
SELECT * FROM EMPLOYEES
LIMIT 10;
SELECT * FROM customers
LIMIT 10;
SELECT * FROM OrderDetails
LIMIT 10;

-- 직접 풀어보기 
-- SELECT CstomerName, title
-- FROM ORDERS A
-- JOIN film_actor B ON A.actor_id = B.actor_id
-- JOIN film C ON B.film_id = C.film_id
-- WHERE A.first_name = 'NICK' AND A.last_name = 'WAHLBERG'
-- LIMIT 10;

-- 같이 풀어보기 
SELECT A.*, B.customerName, concat(C.lastName, "  ", C.firstName) AS EmployeeName
FROM orders A
JOIN customers B ON A.customerId = B.customerId
JOIN EMPLOYEES C ON A.employeeId = C. employeeId;

-- 고치기 
SELECT A.orderID, B.customerName, concat(C.lastName, "  ", C.firstName) AS EmployeeName
FROM orders A
JOIN customers B ON A.customerId = B.customerId
JOIN EMPLOYEES C ON A.employeeId = C. employeeId;



-- ===========================================
-- join 안쓰고 서브쿼리로 바꾸기

SELECT orderId,
	(SELECT customerId = B.customerId FROM customers B
		WHERE A.customerId = B.customerId) AS customerName
,
(SELECT concat(C.lastName, "  ", C.firstName)
FROM employees C
WHERE  A.employeeId = C.employeeId) AS employeeName
FROM orders A;




-- ---------------------------------------------
-- 문제: 주문내역, 고객이름, 판매자 이름 까지만 출력해봐라
SELECT * FROM Orders LIMIT 10;   -- 이 내부에 customerID와 employeeID가 다 있습니다.
SELECT * FROM EMPLOYEES LIMIT 10; 
SELECT * FROM customers LIMIT 10;
-- chatGPT 제시한 내용  -------------------------
SELECT 
  A.orderId,
(SELECT B.customerName 
   	FROM customers B
   	WHERE A.customerId = B.customerId) AS customerName,    -- 고객 이름 가져오기
(SELECT CONCAT(C.lastName, ' ', C.firstName)
   	FROM employees C
   	WHERE A.employeeId = C.employeeId) AS employeeName    -- 직원 이름 (성 + 이름) 가져오기

FROM orders A;



-- 리눅스 MySQL 대소문자를 따집니다.







